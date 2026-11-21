# marioo_kart

from model.terrain import TERRAINS, Terrain
from model.tile import Tile
from constants import TILE_SIZE

class Circuit:
    def __init__(self, nom: str, grid: list[list[Tile]], tours: int, nb_points_de_passage: int, positions_depart: dict):
        """
        Entre: nom, grid, tours, nb_points_de_passage, positions_depart
        Sortie : rien(initialise l'objet Circuit)
        Fonctionnement : stocke les informations du circuit et calcule le nombre de lignes et de colonnes de la grille

        """
        self.nom = nom
        self.grid = grid
        self.tours = tours
        self.nb_points_de_passage = nb_points_de_passage
        self.positions_depart = positions_depart  # {joueur: (x, y, cap)}
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0




    def get_tile(self, col: int, row: int) -> Tile | None:
        """
        # Entrées : col (colonne) et row (ligne) 
        # Sortie : la case (Tile) demandée,ou None si les coord hors de la grille
        # Fonctionnement : vérifie que les coordonnées sont valides, puis récupère la case correspondante
        """

        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    


    def get_tile_at_pixel(self, px: float, py: float) -> Tile | None:
        """
            Entrées : px et py (position en pixels)
            Sortie : la case (Tile) située à cette position, ou None si hors de la grille
            Fonctionnement : convertit les coordonnées en pixels en coordonnées de grille (ligne et colonne), puis appelle get_tile()
         """
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)


    def pixel_width(self) -> int:
        return self.cols * TILE_SIZE
    """
    # Entrées : rien
    # Sortie : largeur totale du circuit en pixels
    # Fonctionnement : multiplie le nombre de colonnes par la taille d'une case
    """

    def pixel_height(self) -> int:
        return self.rows * TILE_SIZE
    """
    # Entrées : rien
    # Sortie : hauteur totale du circuit en pixels
    # Fonctionnement : multiplie le nombre de lignes par la taille d'une case
    """

    def terrain_en(self, px: float, py: float) -> Terrain:
        """[AJOUT] Terrain au point donné ; l'extérieur de la carte est du Vide."""
        tile = self.get_tile_at_pixel(px, py)
        return tile.terrain if tile else TERRAINS["V"]
    """
    # Entrées : px et py (position en pixels)
    # Sortie : le terrain (Terrain) situé à cette position
    # Fonctionnement : récupère la case correspondante et renvoie son terrain, si la position est à l'extérieur de la carte le terrain Vide (V)
    """