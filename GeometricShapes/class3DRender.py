import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import numpy as np
import time
import random as rd

from Settings import *


class _3DRender:
    def __init__(self, display, gameStateManager):
        """
        Init method
        - Inputs :
            * Display : pygame screen.
            * gameStateManager : Manage the different scenes.
        """
        
        # Pygame init
        pygame.init()

        # Gamestate
        self.display = display
        self.gameStateManager = gameStateManager

        # Variables
        self.clock = pygame.time.Clock()
        self.previous_time = time.time()
        self.sommets = {}
        self.faces = []
        self.maj_var()

        
    def run(self):
        """
        Main loop of the program
        """
        
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

        for faces in self.pos_faces():
            pygame.draw.polygon(self.display, white, faces)
            # Open the possibility to apply color to face
            
        # Dessine arrêtes
        for arretes in self.pos_arretes():
            pygame.draw.line(self.display, purple, arretes[0], arretes[1], 2)

        
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(FPS)



# ------------------------------------------------METHODS------------------------------------------------ #

    def render_3dto2d(self, angle : float) -> dict[str, list]:
        """
        R3 -> R2 Transform
        Convert from "xyz" coordinates to "xy" coordinates.
        (Also do the rotation which is something to change asap -> put every rotation into its own method)
        """
        
        angle_rad = (angle * np.pi) / 180
        lst_proj = {}
        for sommets, coord in self.sommets.items():
            x, y, z = coord[0]

            # Rotation x
            x, y, z = self.rotation("x", angle_rad, x, y, z)
            
            # Rotation y
            x, y, z= self.rotation("y", angle_rad, x, y, z)
            
            # Rotation z
            x, y, z = self.rotation("z", angle_rad, x, y, z)
            
            # Projection
            xi = ((x * distance_focale) // (z + self.distance_focale + 256)) + milieu_w
            yi = ((y * distance_focale) // (z + self.distance_focale + 256)) + milieu_h
            lst_proj[sommets] = (xi, yi)
            
        return lst_proj



    def rotation(self, rot, angle_rad, x, y , z):
        if rot == "x":
            mat_rotation = np.mat([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                   [np.sin(angle_rad), np.cos(angle_rad) , 0],
                                   [                0,                  0, 1]])
        if rot == "y":
            mat_rotation = np.mat([[np.cos(angle_rad) , 0, np.sin(angle_rad)],
                                   [                 0, 1,                 0],
                                   [-np.sin(angle_rad), 0, np.cos(angle_rad)]]) 
            
        if rot == "z":
            mat_rotation = np.mat([[1,                 0,                  0],
                                   [0, np.cos(angle_rad), -np.sin(angle_rad)],
                                   [0, np.sin(angle_rad), np.cos(angle_rad)]])
            
        mat_pos_xyz = np.mat([[x],
                              [y],
                              [z]])
        mat_nouv_xyz = np.matmul(mat_rotation, mat_pos_xyz)
        
        x = int(mat_nouv_xyz.item(0))
        y = int(mat_nouv_xyz.item(1))
        z = int(mat_nouv_xyz.item(2))
        
        return x, y, z
        


    def pos_arretes(self): # Changer en pos_surface(self)
        """
        Return an array which contain each edges with the "xy" position of the two vertices.
        """
        
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
    
    
    
    def pos_faces(self):
        """
        Return an array which contain each faces with the "xy" coordinates of the face
        """
        lst_faces = []
        lst_coord = self.render_3dto2d(self.angle)
        # print(lst_coord)
        for face in self.faces:
            p1 = lst_coord[face[0]]
            p2 = lst_coord[face[1]]
            p3 = lst_coord[face[2]]
            
            lst_faces.append((p1, p2, p3))
            
        return lst_faces
                  
                  
                      
    def maj_var(self):
        """
        Init variables in __init__
        -> Reset position and slider each we are changing scene
        """
        
        self.sliderFOV = Slider(self.display, 75, SCREENHEIGHT - 50, 200, 40, min=256, max=750, step=1)
        self.distance_focale = 512
        self.xi, self.yi = 0, 0
        self.angle = 0
        self.vitesse = 0
        # self.rotation_cube(self.angle)
    
    

    
