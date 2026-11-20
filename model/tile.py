# marioo_kart
#from model.bloc import Bloc
from model.terrain import Terrain

class Tile:
    """Une case de la grille. Elle ne dessine rien : c'est la vue qui dessine."""
    def __init__(self, col, row, terrain, bloc=None):
        self.col = col          # numéro de colonne (0 à 15)
        self.row = row          # numéro de ligne (0 à 11)
        self.terrain = terrain  # un objet Terrain (fichier de A)
        #self.bloc = bloc        # un objet Bloc, ou None s'il n'y a rien