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

#affichage du menu principal et des commandes:
'''ici, on crée une classe qui va afficher le menu principal du jeu et ses
comandes '''

class MenuPrincipal:
    
    #constructeur :
    '''le constructeur de la classe crée la variabe options qui permet au
joueur de choisir de jouer ou de quitter le jeu, ce choix est ensuite stocké
dans selected_index, on choisi egalement la tailles et la police des
differentes ecritures du menu'''
    def __init__(self):
        
        self.options = ["JOUER", "QUITTER"]
        self.selected_index = 0

        self.title_font = pygame.font.SysFont("Arial", 58, bold=True)
        self.option_font = pygame.font.SysFont("Arial", 30)
        self.info_font = pygame.font.SysFont("Arial", 20)

    #Gèrer les déplacements et la sélection dans le menu 
'''La fonction Navigation récupère les touches du clavier appuiyé afin que
le joueur puisse naviguer dans les choix du menu:

Flèche haut : remonter dans les choix
Flèche bas : descendre dans les choix
Entrée : sélectionner le choix

elle renvoie ensuite "play" ou "quit" selon le choix'''

    def Navigation(self, event):


        if event.type != pygame.KEYDOWN:
            return None

        if event.key == pygame.K_UP:
            #remonter
            self.selected_index = (self.selected_index - 1) % len(self.options)
    
        elif event.key == pygame.K_DOWN:
            #descendre
            self.selected_index = (self.selected_index + 1) % len(self.options)

        elif event.key == pygame.K_RETURN:
            #jouer
            if self.selected_index == 0:
                return "play"

            elif self.selected_index == 1:
                #quitter
                return "quit"

        return None
    
#Dessiner le menu principal sur la fenêtre du jeu :
    ''''cette fonction va afficher tous les éléments du menu tel que:
 Le fond, le titre, le sous-titre, les deux boutons, les instructions

 et ca en creeant la variable qui va contenir le texte+ la couleur du text en
 image avec "render" , puis en
 determinant la position dans la fenetre du menu avec "get_rect" et enfin en
 le dessinant avec "blit" '''
    
    def Affichage(self, screen):
        

        screen.fill(COLOR_BG)

        # Titre du jeu :

        #le texte+la couleur :
        title = self.title_font.render("Jeu de course 2D",True,COLOR_ACCENT)
        #position dans la fenetre avec "get_rect":
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 180))
        #on dessine ce titre avec "blit"
        screen.blit(title, title_rect)


        #sous-titre :

        
        subtitle = self.info_font.render("Bienvenue dans la course !",True,
                                         COLOR_TEXT)

        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 245))

        screen.blit(subtitle, subtitle_rect)
        

        # affichage des options :

        '''Ici on parcour les options du menu, '''
        
        for i, option in enumerate(self.options):
            
            #definition des coordonnées de chaque bouton :
            x = WINDOW_WIDTH // 2   #milieu horizontale de la fenetre 
            y = 370 + i * 85        #position verticale du bouton

            #créer le rectangle du bouton
            rect = pygame.Rect(x - 160, y - 30,320,60)
            
            #Afficher le fond du bouton 
            pygame.draw.rect(screen,COLOR_PANEL,rect,border_radius=10)
            
            #Afficher la bordure du bouton
            #(quand le bouton est sélectionné sa bordure est plus epaisse)
            pygame.draw.rect(screen,COLOR_ACCENT if i == self.selected_index
                else COLOR_PANEL_BORDER,rect,
                3 if i == self.selected_index else 2,border_radius=10)
            
            #couleur du text (accentuée si il est selectionné)
            color = (COLOR_ACCENT if i == self.selected_index
                else COLOR_TEXT)
                
            #Créer l'image du texte
            text = self.option_font.render(option,True,color)

            #centrer le texte dans le bouton
            text_rect = text.get_rect(center=rect.center)
            #Affciage
            screen.blit(text, text_rect)
            

        # Instructions :
        
        instructions = self.info_font.render(
            "Utilisez les fleches pour naviguer et ENTREE pour valider",True,
            COLOR_TEXT)

        instructions_rect = instructions.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 70))

        screen.blit(instructions, instructions_rect)
