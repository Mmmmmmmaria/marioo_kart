# jeu_de_course

import pygame

from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    COLOR_BG,
    COLOR_TEXT,
    COLOR_ACCENT,
    COLOR_PANEL,
    COLOR_PANEL_BORDER)

# Affichage d'un menu de pause dans le jeu :

'''ici on cree une clase qui va permettre de crée et d'affciher un menu quand le
joueur decide d'interompre le jeu'''

class MenuPause:

    #Constructeur
    '''le constructeur de la classe crée la variabe options qui permet au
joueur de choisir de reprendre le jeu, de le quitter ou d'aller vers le menu
principal, ce choix est ensuite stocké
dans selected_index, on choisi egalement la tailles et la police des
differentes ecritures du menu'''

    def __init__(self):
        self.options = ["REPRENDRE","MENU PRINCIPAL","QUITTER"]

        self.selected_index = 0

        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)

        self.option_font = pygame.font.SysFont("Arial", 27)

        self.info_font = pygame.font.SysFont("Arial", 18)

    def Navigation(self, event):
        
'''La fonction Navigation récupère les touches du clavier appuiyé afin que
le joueur puisse naviguer dans les choix du menu
(reprendre la course, menu principal, quitter):

Flèche haut : remonter dans les choix
Flèche bas : descendre dans les choix
Entrée : sélectionner le choix
Escape : reprendre la course

elle renvoie ensuite "play" ou "quit" selon le choix'''

        if event.type != pygame.KEYDOWN:
            return None
    
        if event.key == pygame.K_UP:
            #remonter
            self.selected_index = (self.selected_index - 1) % len(self.options)

        elif event.key == pygame.K_DOWN:
            #descendre
            self.selected_index = (self.selected_index + 1) % len(self.options)

        elif event.key == pygame.K_ESCAPE:
            #reprendre la course
            return "resume"

        elif event.key == pygame.K_RETURN:

            if self.selected_index == 0:
                return "resume"

            elif self.selected_index == 1:
                return "menu"

            elif self.selected_index == 2:
                return "quit"

        return None

    def Affichage(self, screen):
        '''cette fonction affiche le menu pause au-dessus de la course,
    et cela en créeant un fond noir semi-transparent afin que la course
    reste visible derrière le menu mais assombrie
    '''
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT),pygame.SRCALPHA)
        #création du fond noir semi-transparent :
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Titre :

        #le texte+la couleur :
        title = self.title_font.render("PAUSE",True, COLOR_ACCENT)
        #position dans la fenetre avec "get_rect":
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 190))
        #on dessine ce titre avec "blit"
        screen.blit(title, title_rect)

        # Affichage des options :
        for i, option in enumerate(self.options):

            #definition des coordonnées de chaque bouton :
            x = WINDOW_WIDTH // 2  #milieu horizontale de la fenetre 
            y = 320 + i * 75       #position verticale du bouton

            #créer le rectangle du bouton
            rect = pygame.Rect(x - 180,y - 28,360,56)

            #Afficher la bordure du bouton
            #(quand le bouton est sélectionné sa bordure est plus epaisse et la
            # couleur est plu accentuée)
            pygame.draw.rect(screen,COLOR_PANEL,rect,border_radius=10)

            border_color = (COLOR_ACCENT if i == self.selected_index
                else COLOR_PANEL_BORDER)

            pygame.draw.rect(screen,border_color,rect,
                3 if i == self.selected_index else 2,border_radius=10)

            text_color = (COLOR_ACCENT if i == self.selected_index
                else COLOR_TEXT)
                
            #Créer l'image du texte
            text = self.option_font.render(option,True,text_color)
            #centrer le texte dans le bouton
            text_rect = text.get_rect(center=rect.center)
            #Affciage 
            screen.blit(text, text_rect)
            

        # Instructions pour l'utilisateur:
        
        instructions = self.info_font.render(
            "Fleches -> naviguer / Entree -> valider / Echap -> reprendre",
            True,COLOR_TEXT)

        instructions_rect = instructions.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 65))

        screen.blit(instructions, instructions_rect)
