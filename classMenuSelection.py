import pygame
from Settings import *

class Menu:
    def __init__(self, display, gameStateManager):
        pygame.init()
        self.display = display
        self.gameStateManager = gameStateManager

        self.font_size = 72
        self.font = pygame.font.Font(None, self.font_size)
    
    def run(self):
        self.display.fill(black)

        self.texte_cube = self.font.render("- Appuyer sur 'c' pour un cube", True, white)
        self.texte_cube_pos = self.texte_cube.get_rect(center = (SCREENWIDTH//2, 80))
        self.display.blit(self.texte_cube, self.texte_cube_pos)

        self.texte_pyramide = self.font.render("- Appuyer sur 'p' pour une pyramide", True, white)
        self.texte_pyramide_pos = self.texte_pyramide.get_rect(center = (SCREENWIDTH//2, 160))
        self.display.blit(self.texte_pyramide, self.texte_pyramide_pos)

        self.texte_quitter = self.font.render("- Appuyer sur 't' pour un tétraèdre", True, white)
        self.texte_quitter_pos = self.texte_quitter.get_rect(center = (SCREENWIDTH//2, 240))
        self.display.blit(self.texte_quitter, self.texte_quitter_pos)

        self.texte_menu = self.font.render("- Appuyer sur 'm' pour revenir ici", True, white)
        self.texte_menu_pos = self.texte_menu.get_rect(center = (SCREENWIDTH//2, 320))
        self.display.blit(self.texte_menu, self.texte_menu_pos)