# Kart-Engine v2.3
# cette fonction regroupe les commandes et les calculs physiques déjà programmés
def mettre_a_jour_voiture(car, entrees, terrain, dt):

    if entrees.get("accelerer", False):
        car.accelerate(terrain)
    if entrees.get("freiner", False):
        car.brake()
    if entrees.get("gauche", False):
        car.turn_left()
    if entrees.get("droite", False):
        car.turn_right()

    car.apply_friction(terrain)
    car.update_direction(terrain)
    car.update_position() 
    car.avancer_minuteurs(dt)                