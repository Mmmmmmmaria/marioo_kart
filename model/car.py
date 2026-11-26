import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)

class FicheVoiture :
     def __init__(self, nom, couleur, acceleration):
        self.nom = nom
        self.couleur = couleur
        self.acceleration = acceleration

CATALOGUE_VOITURES = [
          FicheVoiture("Rouge", (220, 50, 50), CAR_ACCELERATION),
          FicheVoiture("Bleue", (50, 100, 220), CAR_ACCELERATION)
]        

class Car:

    def __init__(self, joueur, fiche, x, y, cap):
        self.joueur = joueur
        self.fiche = fiche
        self.x = x
        self.y = y 
        self.speed: float = 0.0
        self.angle = cap
        self.move_angle = cap
        self.sprite = self.build_sprite()
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
        self.speed += self.fiche.acceleration * terrain.traction

    def update_position(self) -> None:
        angle_rad = math.radians(self.move_angle)
        self.x += self.speed * math.sin(angle_rad)
        self.y += self.speed * math.cos(angle_rad)

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.fiche.couleur, (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        rotated = pygame.transform.rotate(self.sprite, self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect

    def brake (self) :
        if self.speed > 0:
            # freinage lorsque la voiture avance
            self.speed = max(0, self.speed - CAR_ACCELERATION *2)
        else :
            # marche arrière plus progressive    
            self.speed -= CAR_ACCELERATION * 0.3

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