import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:

    def __init__(self, start_col: int, start_row: int, joueur: int = 1):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.move_angle = self.angle
        self.sprite = self.build_sprite()
        self.joueur = joueur
        self.est_en_boost = False
        self.temps_boost = 0.0

    def appliquer_boost(self, force):
        self.speed += force
        self.est_en_boost = True
        self.temps_boost = 1.0

    def avancer_minuteurs(self, dt):
        if self.est_en_boost :
            self.temps_boost -= dt

            if self.temps_boost <= 0:
                self.temps_boost = 0
                self.est_en_boost = False        

    # rendre car.cap et car.angle compatibles
    @property
    def cap(self) : 
        return self.angle
    @cap.setter
    def cap(self, valeur):
        self.angle = valeur


    def accelerate(self, terrain) -> None:
        self.speed += CAR_ACCELERATION * terrain.traction

    def update_position(self) -> None:
        angle_rad = math.radians(self.move_angle)
        self.x += self.speed * math.sin(angle_rad)
        self.y += self.speed * math.cos(angle_rad)

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect

    def brake (self) :
        self.speed -= CAR_ACCELERATION

    def apply_friction(self, terrain):
        self.speed *= terrain.friction   

    def turn_left(self):
        self.angle += 5

    def turn_right(self):
        self.angle -= 5    

    # pour faire évoluer move_angle en fonction de l'adhérence du terrain
    def update_direction (self, terrain):
        difference = self.angle - self.move_angle
        self.move_angle += difference * (terrain.grip**2)   

    def teleporter_vers (self, x, y, cap):
        self.x = x
        self.y = y    
        self.angle = cap
        self.move_angle = cap
        self.speed = 0