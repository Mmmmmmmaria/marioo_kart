# Kart-Engine v2.3
import pygame
from constants import TILE_SIZE
from model.terrain import Road, Grass, Dirt, Ice, Void


class RoadTile:

    def __init__(self, col: int, row: int, terrain = None):
        self.col = col
        self.row = row
        self.terrain = terrain if terrain is not None else Road()
        self.sprite: pygame.Surface | None = None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        # récupérer la couleur définie dans terrain.py
        surface.fill(self.terrain.couleur)

        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
