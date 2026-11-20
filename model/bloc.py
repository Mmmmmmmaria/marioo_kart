# marioo_kart
from abc import ABC, abstractmethod # importe les outils pour créer des classes abstraites pour obliger es cases qui hiritent de cette classe à dof une méthode 
from constants import FORCE_BLOC_BOOST, TILE_SIZE


class Bloc(ABC):
    """
    entrée : col, row
    sotie : crée un bloc avec sa position sans libelle
    traitement : d'apres la colonne et ligne permet de calculer la position du centre de la case 
    """
    nature = "bloc"
    libelle = ""

    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.x = (col + 0.5) * TILE_SIZE
        self.y = (row + 0.5) * TILE_SIZE

    @abstractmethod #le bloc définit ce qu'il fait quand une voiture entre sur sa case
    def a_l_entree(self, car, course):
        


class PointDePassage(Bloc):
     """
     entrée : col, row , indice,car, course
     sotie : rien
     traitement : initialise la position du checkpoint sur la grille,enregistre son numéro, puis le convertit en lettre pour faciliter l'affichage
     """

    nature = "point_de_passage"
    libelle = "C"

    def __init__(self, col, row, indice):
        super().__init__(col, row)
        self.indice = indice

    def a_l_entree(self, car, course):
        course.franchir_point_de_passage(car.joueur, self.indice, self.x, self.y, car.cap) # enregistre le point de passage


class LigneArrivee(Bloc):
    """
        entrée : car et course 
        sotie : rien juste le gestionnaire de course met à jour la progression ou vérifie si le joueur a terminé
        traitement:transmet le numéro du joueur au gestionnaire de course
    """

    nature = "arrivee"
    libelle = "F"

    def a_l_entree(self, car, course):
        course.franchir_ligne_arrivee(car.joueur) #pour valider un tour


class Boost(Bloc):
    """
        entrée : car et course 
        sotie : rien 
        traitement : appelle appliquer_boost() avec une force
    """

    nature = "boost"
    libelle = "B"
    def a_l_entree(self, car, course):
        car.appliquer_boost(FORCE_BLOC_BOOST)


class BlocDepart(Bloc):
    """
        entrée : col,row,joueur 
        sotie : crée bloc de depart sans effet si la voiture passe 
        traitement : calcule la position de l'élément grâce au constructeur de la classe parente, enregistre son numéro, puis définit son libellé (« 1 » ou « 2 »)
    """

    nature = "depart"

    def __init__(self, col, row, joueur):
        super().__init__(col, row)
        self.joueur = joueur
        self.libelle = str(joueur)

    def a_l_entree(self, car, course):
       """ pas effet """


_BLOCS_SIMPLES = {"L": LigneArrivee, "B": Boost}


def creer_bloc(caractere, col, row):
    if caractere == ".":
        return None
    if caractere in ("1", "2"):
        return BlocDepart(col, row, int(caractere))
    if caractere.isalpha() and caractere.islower(): # si a et b on cree un checkpoint 
        return PointDePassage(col, row, ord(caractere) - ord("a"))
    fabrique = _BLOCS_SIMPLES.get(caractere)
    if fabrique is None: # erreur si lettre indifinie 
        raise ValueError(f"Bloc inconnu : '{caractere}' (colonne {col}, ligne {row})")
    return fabrique(col, row)
