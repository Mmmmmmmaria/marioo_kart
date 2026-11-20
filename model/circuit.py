# marioo_kart
# Kart-Engine v2.3
from constants import TILE_SIZE
from model.terrain import TERRAINS
class Circuit:
    """La grille complète d'un circuit et ses informations."""
    def __init__(self, nom, grid, tours, nb_points_de_passage, positions_depart):
        self.nom = nom

        self.grid = grid                            # grid[row][col] -> Tile
        self.tours = tours                          # nombre de tours à faire
        self.nb_points_de_passage = nb_points_de_passage
        self.positions_depart = positions_depart    # {1: (x, y, cap), 2: (x, y, cap)}
        self.nb_lignes = len(grid)
        self.nb_colonnes = len(grid[0])
    @property
    def pixel_width(self):
        return self.nb_colonnes * TILE_SIZE
    @property
    def pixel_height(self):
        return self.nb_lignes * TILE_SIZE
    def get_tile(self, col, row):
        """Renvoie la case (col, row), ou None si on est hors de la grille."""
        if 0 <= row < self.nb_lignes and 0 <= col < self.nb_colonnes:
            return self.grid[row][col]
        return None
    def get_tile_at_pixel(self, px, py):
        """Renvoie la case qui contient le point (px, py) en pixels."""
        col = int(px // TILE_SIZE)
        row = int(py // TILE_SIZE)
        return self.get_tile(col, row)
    def terrain_en(self, px, py):
        """Terrain sous le point (px, py). Hors de la carte = Vide."""
        tile = self.get_tile_at_pixel(px, py)
        if tile is None:
            return TERRAINS["V"]
        return tile.terrain