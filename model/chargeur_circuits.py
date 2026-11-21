""""
# marioo_kart

Format JSON : "terrain" et "blocs" sont deux listes de chaînes de même taille
Terrain : R route, G herbe, D terre, S sable, I glace, V vide
Blocs : . aucun, 1/2 départ, a-z points de passage, L arrivée, B boost
"""
import glob
import json
import math
import os

from constants import DOSSIER_CIRCUITS
from model.bloc import PointDePassage, BlocDepart, creer_bloc
from model.circuit import Circuit # pour cree un circuit complet
from model.terrain import TERRAINS  # dictionnaire associer chaque lettre au terrain
from model.tile import Tile #classe pour represente la case de la grille 


def lister_circuits() -> list[str]:
    return sorted(glob.glob(os.path.join(DOSSIER_CIRCUITS, "*.json")))


def charger_circuit(path: str) -> Circuit:
    """lire le fichier JSON et construit le circuit correspondant"""
    nom_fichier = os.path.basename(path)
    with open(path, encoding="utf-8") as fichier: # utf-8 utiliser pour lire correctment les caracteres
        donnees = json.load(fichier)
    lignes_terrain, lignes_blocs = donnees["terrain"], donnees["blocs"]# decrire les surfaces et obet placés sur les cases 
    if len(lignes_terrain) != len(lignes_blocs): 
        raise ValueError(f"{nom_fichier} : 'terrain' et 'blocs' n'ont pas le même nombre de lignes")
    largeur = len(lignes_terrain[0])
    cap = math.radians(donnees.get("cap_depart", 0)) # l'angle du depart en radient car python les utilises pour les calculs de mathématiques du jeu
    grid, departs, points_de_passage = [], {}, set() # grid: liste pour stocker tout cases avec ordre precis/ departs: dictionnaire pour associer chaque joeur a une position / port_de_passage:ensemble set pour eviter les doublonts
    # les lignes (row) sont les chaînes, les colonnes (col) leurs caractères
    for row, (ligne_terrain, ligne_blocs) in enumerate(zip(lignes_terrain, lignes_blocs)): # assoier ligne terrains a un bloc
        if len(ligne_terrain) != largeur or len(ligne_blocs) != largeur:
            raise ValueError(f"{nom_fichier} : ligne {row} de longueur incorrecte")
        ligne_cases = []
        for col, (c_terrain, c_bloc) in enumerate(zip(ligne_terrain, ligne_blocs)):
            if c_terrain not in TERRAINS: # lettre introvable dans dictionnaire terrains
                raise ValueError(f"{nom_fichier} : terrain inconnu '{c_terrain}' ({col}, {row})")
            bloc = creer_bloc(c_bloc, col, row) # cree le bloc exemple (".",3,9)
            if isinstance(bloc, BlocDepart):#verif si il existe un point de depart 
                departs[bloc.joueur] = (bloc.x, bloc.y, cap)
            elif isinstance(bloc, PointDePassage):#verif si il existe un point de passage
                points_de_passage.add(bloc.indice)
            ligne_cases.append(Tile(col, row, TERRAINS[c_terrain], bloc)) # [plus important ligne ] cree case tile objet tile : col,ligne,c_terrain c_bloc /exemple: (3,9,"R","1")=>une case contenant le terrain route et le bloc de départ du joueur 1
        grid.append(ligne_cases)
    if set(departs) != {1, 2}: # 2 joueur avec position de depart?
        raise ValueError(f"{nom_fichier} :faut un bloc de départ '1' et un bloc '2'")
    if points_de_passage != set(range(len(points_de_passage))): # points de passage 0,1,2
        raise ValueError(f"{nom_fichier} : probleme sur point de passage")
    return Circuit(donnees["nom"], grid, donnees["tours"], len(points_de_passage), departs) # Cree circuit complet nom/grille/tours/nb_points de passages/depépart
