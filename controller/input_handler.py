import pygame

'''
MAPPING = {
    pygame.K_UP:     "accelerate",
}


class InputHandler:

    def __init__(self):
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}

        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p
'''

class InputHandler:
    """Gestion des commandes clavier des deux joueurs."""

    def get_inputs(self) -> dict:
        keys = pygame.key.get_pressed()

        player1 = {
            "accelerate": keys[pygame.K_z],
            "brake": keys[pygame.K_s],
            "left": keys[pygame.K_a],
            "right": keys[pygame.K_e],
            "use_item": keys[pygame.K_TAB]
        }

        player2 = {
            "accelerate": keys[pygame.K_UP],
            "brake": keys[pygame.K_DOWN],
            "left": keys[pygame.K_LEFT],
            "right": keys[pygame.K_RIGHT],
            "use_item": keys[pygame.K_SHIFT]
        }

        return {
            "player1": player1,
            "player2": player2
        }
