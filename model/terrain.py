# Kart-Engine v2.3

class Terrain :
    """ Classe de base des terrains [TERRA-7]."""

    def __init__(self, grip, traction, friction):
        """ grip : adhérence ; plus il est faible, plus la voiture risque de déraper
        traction : traction ; plus elle est élevée, plus la voiture accélère et freine facilement.
        friction : frottement ; plus il est proche de 1, moins la voiture ralentit """
        self.grip = grip
        self.traction = traction
        self.friction = friction
        self.est_vide = False

class Road(Terrain):
    """ Terrain de type route [TERRA-7]."""

    def __init__(self):
        super().__init__(0.9, 1.0, 0.99)
        self.code = "R"
        self.couleur = (80, 80, 90)

class Grass(Terrain):
    """ Terrain de type herbe [TERRA-7]."""

    def __init__(self):
        super().__init__(0.6, 0.7, 0.98)
        self.code = "G"
        self.couleur = (50, 160, 70)
class Dirt(Terrain):
    """ Terrain de type terre [TERRA-7]."""

    def __init__(self):
        super().__init__(0.35, 0.6, 0.98) 
        self.code = "D"
        self.couleur = (115, 70, 40)   

class Ice(Terrain):
    """ Terrain de type glace [TERRA-7]."""

    def __init__(self):
        super().__init__(0.2, 0.3, 0.99)
        self.code = "I"
        self.couleur = (150, 220, 255)

class Void(Terrain):
    """ Terrain de type vide [TERRA-7]."""

    def __init__(self):
        super().__init__(0.0, 0.0, 0.0)
        self.code = "V"
        self.couleur = (0, 0, 0)
        self.est_vide = True                                    
class Sand(Terrain):
    """Terrain de type sable [TERRA-7]."""
    def __init__(self):
        super().__init__(0.5, 0.4, 0.92)
        self.code = "S"
        self.couleur = (215, 185, 125)

TERRAINS = {
    "R" : Road(),
    "G" : Grass(),
    "D" : Dirt(),
    "I" : Ice(),
    "V" : Void(),
    "S" : Sand()
}        