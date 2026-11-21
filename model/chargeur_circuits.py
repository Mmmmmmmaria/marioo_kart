# Kart-Engine v2.3
"""[AJOUT] Chargement des circuits depuis les fichiers JSON du dossier circuits/.

Remplace la construction de la grille faite dans GameModel.load_circuit() du code de départ.

Format JSON : "terrain" et "blocs" sont deux listes de chaînes de même taille.
Terrain : R route, G herbe, D terre, S sable, I glace, V vide.
Blocs : . aucun, 1/2 départ, a-z points de passage, L arrivée, B boost.
"""
import glob
import json
import math
import os

from constants import DOSSIER_CIRCUITS
from model.bloc import PointDePassage, BlocDepart, creer_bloc
from model.circuit import Circuit
from model.terrain import TERRAINS
from model.tile import Tile


def lister_circuits() -> list[str]:
    """Chemins des fichiers de circuits, triés par nom."""
    return sorted(glob.glob(os.path.join(DOSSIER_CIRCUITS, "*.json")))


def charger_circuit(path: str) -> Circuit:
    """Lit un fichier JSON et construit le Circuit correspondant."""
    nom_fichier = os.path.basename(path)
    with open(path, encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    lignes_terrain, lignes_blocs = donnees["terrain"], donnees["blocs"]
    if len(lignes_terrain) != len(lignes_blocs):
        raise ValueError(f"{nom_fichier} : 'terrain' et 'blocs' n'ont pas le même nombre de lignes")
    largeur = len(lignes_terrain[0])
    cap = math.radians(donnees.get("cap_depart", 0))
    grid, departs, points_de_passage = [], {}, set()
    # Les lignes (row) sont les chaînes, les colonnes (col) leurs caractères.
    for row, (ligne_terrain, ligne_blocs) in enumerate(zip(lignes_terrain, lignes_blocs)):
        if len(ligne_terrain) != largeur or len(ligne_blocs) != largeur:
            raise ValueError(f"{nom_fichier} : ligne {row} de longueur incorrecte")
        ligne_cases = []
        for col, (c_terrain, c_bloc) in enumerate(zip(ligne_terrain, ligne_blocs)):
            if c_terrain not in TERRAINS:
                raise ValueError(f"{nom_fichier} : terrain inconnu '{c_terrain}' ({col}, {row})")
            bloc = creer_bloc(c_bloc, col, row)
            if isinstance(bloc, BlocDepart):
                departs[bloc.joueur] = (bloc.x, bloc.y, cap)
            elif isinstance(bloc, PointDePassage):
                points_de_passage.add(bloc.indice)
            ligne_cases.append(Tile(col, row, TERRAINS[c_terrain], bloc))
        grid.append(ligne_cases)
    if set(departs) != {1, 2}:
        raise ValueError(f"{nom_fichier} : il faut un bloc de départ '1' et un bloc '2'")
    if points_de_passage != set(range(len(points_de_passage))):
        raise ValueError(f"{nom_fichier} : les points de passage doivent être a, b, c... sans trou")
    return Circuit(donnees["nom"], grid, donnees["tours"], len(points_de_passage), departs)
