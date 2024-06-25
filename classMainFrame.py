import pygame
import pygame_widgets
from Settings import *

from GeometricShapes.shapeDim import *
from classGameStateManager import GameStateManager
from classMenuSelection import Menu
from GeometricShapes.classCube import Cube
from GeometricShapes.classPyramid import Pyramid
from GeometricShapes.classTetraedre import Tetraedre
from GeometricShapes.classOctahedron import Octahedron
from GeometricShapes.classCone import Cone
from GeometricShapes.classWhatever import Whatever

class MainFrame:
    def __init__(self):
        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('Menu')
        self.Menu = Menu(self.screen, self.gameStateManager)
        
        # Formes géométriques
        self.Cube = Cube(self.screen, self.gameStateManager)
        self.Pyramid = Pyramid(self.screen, self.gameStateManager)
        self.Tetraedre = Tetraedre(self.screen, self.gameStateManager)
        self.Octahedre = Octahedron(self.screen, self.gameStateManager)
        self.Cone = Cone(self.screen, self.gameStateManager)
        self.Whatever = Whatever(self.screen, self.gameStateManager)

        self.states = {'Menu': self.Menu,
                       'Cube': self.Cube,
                       'Pyramid': self.Pyramid,
                       'Tetraedre': self.Tetraedre,
                       'Octahedre': self.Octahedre,
                       'Cone': self.Cone,
                       'Whatever': self.Whatever}
        
        self.states_keys = list(self.states.keys())
        self.states_val = list(self.states.values())

    def run(self):
        while self.running:
            self.draw()
            self.update()
        self.close()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                #     self.running = False

                if event.key == pygame.K_m:
                    self.gameStateManager.set_state('Menu')
                if event.key == pygame.K_c and self.gameStateManager.get_state() != 'Cube':
                    self.gameStateManager.set_state('Cube')
                    self.states[self.gameStateManager.get_state()].maj_var()
                if event.key == pygame.K_p and self.gameStateManager.get_state() != 'Pyramid':
                    self.gameStateManager.set_state('Pyramid')
                    self.states[self.gameStateManager.get_state()].maj_var()
                if event.key == pygame.K_t and self.gameStateManager.get_state() != 'Tetraedre':
                    self.gameStateManager.set_state("Tetraedre")
                    self.states[self.gameStateManager.get_state()].maj_var()
                if event.key == pygame.K_o and self.gameStateManager.get_state() != 'Octahedre':
                    self.gameStateManager.set_state("Octahedre")
                    self.states[self.gameStateManager.get_state()].maj_var()
                if event.key == pygame.K_n and self.gameStateManager.get_state() != 'Cone':
                    self.gameStateManager.set_state("Cone")
                    self.states[self.gameStateManager.get_state()].maj_var()
                if event.key == pygame.K_w and self.gameStateManager.get_state() != 'Whatever':
                    self.gameStateManager.set_state("Whatever")
                    self.states[self.gameStateManager.get_state()].maj_var()

        self.states[self.gameStateManager.get_state()].run()
            
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(FPS)

    def draw(self):
        pass
    
    def close(self):
        pygame.quit()