# Kart-Engine v2.3
import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)

class FicheVoiture :
     def __init__(self, nom, couleur, acceleration, maniabilite, aerodynamisme):
        self.nom = nom
        self.couleur = couleur
        self.acceleration = acceleration
        self.maniabilite = maniabilite
        self.aerodynamisme = aerodynamisme

CATALOGUE_VOITURES = [
          FicheVoiture("Rouge", (220, 50, 50), CAR_ACCELERATION * 1.2, 4, 0.997),
          FicheVoiture("Bleue", (50, 100, 220), CAR_ACCELERATION * 0.9, 6, 0.993)]        

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

        w, h = CAR_WIDTH, CAR_HEIGHT

        if self.fiche.nom == "Rouge":

        # Voiture sportive : carrosserie allongée
           pygame.draw.rect(surf, self.fiche.couleur, (2, 0, w - 4, h), border_radius=5)

        # Pare-brise
           pygame.draw.rect(surf, (180, 220, 245), (w // 4, 3 * h // 5, w // 2, h // 4), border_radius=2)

        else:
        # Voiture compacte : carrosserie différente
          pygame.draw.polygon(surf, self.fiche.couleur,
            [(w // 4, 0), (3 * w // 4, 0),
             (w, h // 4), (w, 3 * h // 4),
             (3 * w // 4, h), (w // 4, h),
             (0, 3 * h // 4), (0, h // 4)])

        # Pare-brise plus large
        pygame.draw.rect(surf, (180, 220, 245), (w // 5, 3 * h // 5, 3 * w // 5, h // 4), border_radius=2)

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
        self.speed *= self.fiche.aerodynamisme # Résistance de l'air
        self.speed *= terrain.friction # Frottement du terrain  

    def turn_left(self):
        self.angle += self.fiche.maniabilite

    def turn_right(self):
        self.angle -= self.fiche.maniabilite   

    # pour faire évoluer move_angle en fonction de l'adhérence du terrain
    def update_direction (self, terrain, grip_scale):
        difference = self.angle - self.move_angle
        self.move_angle += difference * ((terrain.grip * grip_scale)**2)   

    def teleporter_vers (self, x, y, cap):
        self.x = x
        self.y = y    
        self.angle = cap
        self.move_angle = cap
        self.speed = 0