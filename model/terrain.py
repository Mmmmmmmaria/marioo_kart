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

class Road(Terrain):
    """ Terrain de type route [TERRA-7]."""

    def __init__(self):
        super().__init__(0.9, 1.0, 0.8)

class Grass(Terrain):
    """ Terrain de type herbe [TERRA-7]."""

    def __init__(self):
        super().__init__(0.6, 0.5, 0.85)

class Dirt(Terrain):
    """ Terrain de type terre [TERRA-7]."""

    def __init__(self):
        super().__init__(0.35, 0.5, 0.92)    

class Ice(Terrain):
    """ Terrain de type glace [TERRA-7]."""

    def __init__(self):
        super().__init__(0.2, 0.3, 0.99)

class Void(Terrain):
    """ Terrain de type vide [TERRA-7]."""

    def __init__(self):
        super().__init__(0.0, 0.0, 0.0)                                    