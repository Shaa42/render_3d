import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import numpy as np
import time
from Settings import *


class _3DRender:
    def __init__(self, display, gameStateManager):
        # Pygame init
        pygame.init()

        # Gamestate
        self.display = display
        self.gameStateManager = gameStateManager

        # Variables
        self.clock = pygame.time.Clock()
        self.previous_time = time.time()
        self.sommets = {}
        # self.sliderAngle = Slider(self.display, 75, SCREENHEIGHT - 100, 200, 40, min=0, max=360, step=0.5)
        # self.sliderFOV = Slider(self.display, 75, SCREENHEIGHT - 50, 200, 40, min=256, max=750, step=1)
        # self.distance_focale = 512
        # self.xi, self.yi = 0, 0
        # self.angle = 0
        # self.vitesse = 0
        # # self.rotation_cube(self.angle)
        self.maj_var()
        
    def run(self):
        # pygame.time.delay(10)
        self.now = time.time()
        self.dt = self.now - self.previous_time
        self.previous_time = self.now
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.gameStateManager.set_state('Menu')
                
                    
        
        # Black background
        self.display.fill(black)
        # Slider

        # self.sliderAngle = Slider(self.display, 75, SCREENHEIGHT - 100, 200, 40, min=0, max=360, step=0.5)
        # self.sliderFOV = Slider(self.display, 75, SCREENHEIGHT - 50, 200, 40, min=256, max=750, step=1)

        # self.angle = self.sliderAngle.getValue()
        self.angle += 30 * self.dt
        self.distance_focale = self.sliderFOV.getValue()

        # Dessine sommets
        # for a, coord in self.render_3dto2d(self.angle).items():
        #     self.xi, self.yi = coord
        #     pygame.draw.rect(self.display, white, (self.xi - 5, self.yi - 5, 10, 10), 0, 360)
            
            # # print(type(a), coord)
            # if a == 'S0':
            #     pygame.draw.rect(self.display, yellow, (self.xi - 5, self.yi - 5, 10, 10))
            # elif a == 'S5':
            #     pygame.draw.rect(self.display, green, (self.xi - 5, self.yi - 5, 10, 10))
            # elif a == 'S4':
            #     pygame.draw.rect(self.display, purple, (self.xi - 5, self.yi - 5, 10, 10))
            # elif a == 'S3':
            #     pygame.draw.rect(self.display, blue, (self.xi - 5, self.yi - 5, 10, 10))
            # else:
            #     pygame.draw.rect(self.display, white, (self.xi - 5, self.yi - 5, 10, 10))

        # Dessine arrêtes
        for arretes in self.pos_arretes():
            pygame.draw.line(self.display, white, arretes[0], arretes[1])

        
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(FPS)

    def render_3dto2d(self, angle : float) -> dict[str, list]: # ew, à changer ------------------------------------------------
        angle_rad = (angle * np.pi) / 180
        lst_proj = {}
        for sommets, coord in self.sommets.items():
            x, y, z = coord[0]

            # Rotation
            mat_pos_xyz = np.mat([[x],
                                 [y],
                                 [z]])
            
            
            mat_rotation = np.mat([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                    [np.sin(angle_rad), np.cos(angle_rad), 0],
                                    [0, 0, 1]])

            
            mat_nouv_xyz = np.matmul(mat_rotation, mat_pos_xyz)

            x = int(mat_nouv_xyz.item(0))
            y = int(mat_nouv_xyz.item(1))
            z = int(mat_nouv_xyz.item(2))
            
            mat_pos2_xyz = np.mat([[x],
                                 [y],
                                 [z]])

            mat_rotation_2 = np.mat([[1, 0, 0],
                                  [0, np.cos(angle_rad), -np.sin(angle_rad)],
                                  [0, np.sin(angle_rad), np.cos(angle_rad)]])
            
            mat_resultat = np.matmul(mat_rotation_2, mat_pos2_xyz)

            x = int(mat_resultat.item(0))
            y = int(mat_resultat.item(1))
            z = int(mat_resultat.item(2))

            

            # print(x, y, z)

            # Projection
            xi = ((x * distance_focale) // (z + self.distance_focale + 256)) + milieu_w
            yi = ((y * distance_focale) // (z + self.distance_focale + 256)) + milieu_h
            lst_proj[sommets] = (xi, yi)
            
        # print(lst_proj)

        return lst_proj

    def pos_arretes(self): # Changer en pos_surface(self)
        lst_arretes = []
        lst_coord = self.render_3dto2d(self.angle)    # Dictionnaire ->{'Sommet' : (pos_x, pos_y)}
        for origine, sommets in self.sommets.items():
            lst_sommets = sommets[1]    # Liste -> [Sommet, sommet, ... , sommet]
            if len(lst_sommets) != 0:
                for points in lst_sommets:
                    pos_origine = lst_coord[origine]
                    pos_sommets = lst_coord[points]
                    lst_arretes.append((pos_origine, pos_sommets))
                    # print(lst_arretes)
        return lst_arretes
    
    def maj_var(self):
        self.sliderFOV = Slider(self.display, 75, SCREENHEIGHT - 50, 200, 40, min=256, max=750, step=1)
        self.distance_focale = 512
        self.xi, self.yi = 0, 0
        self.angle = 0
        self.vitesse = 0
        # self.rotation_cube(self.angle)
    
    

    
