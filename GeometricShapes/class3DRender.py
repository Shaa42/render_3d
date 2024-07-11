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
        self.normals = []
        self.maj_var()
        
        self.couleurs_lst = [np.array(white), yellow, blue, purple, green]
        
        self.angle_x, self.angle_y, self.angle_z = 0, 0, 0
        self.x, self.y, self.z = 0, 0, 0
        self.xn, self.yn, self.zn = 0, 0, 0
        self.array_pos = np.zeros(len(self.sommets))
        self.boing = 0

        
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
        self.boing += self.dt * 20
        self.angle_x += 15 * self.dt
        self.angle_y = 0
        self.angle_z = 0
        
        self.angle = (self.angle_x, self.angle_y, self.angle_z)
        self.distance_focale = self.sliderFOV.getValue()
        self.point = self.render_3dto2d(self.angle)

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
        # print(self.x, self.y, self.z)
        
        # print(self.faces)
        # self.depthBuffer()
        
        # print(self.faces)
        lst_faces, depth = self.pos_faces()
        for index_face in range(len(lst_faces)):
            p0, p1, p2, shown = lst_faces[index_face]
            # print(p2)
            if shown:
                valDepth = depth[index_face] + 225
                lineDepth = depth[index_face] + 245
                if 255 - valDepth > 255:
                    valDepth = 0
                if 255 - lineDepth > 255:
                    lineDepth = 0
                if 255 - valDepth < 0:
                    valDepth = 255
                if 255 - lineDepth < 0:
                    lineDepth = 255
                    
                # print(255 - valDepth)
                pygame.draw.polygon(self.display, (255 - valDepth,)*3 ,np.array((p0, p1, p2))) # type: ignore
                self.dessine_arretes(p0, p1, p2, (255 - lineDepth,)*3)
            # Open the possibility to apply color to face
            
                # Dessine arrêtes
        # for arretes in self.pos_arretes():
        #     pygame.draw.line(self.display, purple, arretes[0], arretes[1], 2)
        # print(self.sommets)
        
        pygame_widgets.update(pygame.event.get())
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(FPS)



# ------------------------------------------------METHODS------------------------------------------------ #

    def render_3dto2d(self, angle : tuple[float, float, float]):
        """
        R3 -> R2 Transform
        Convert from "xyz" coordinates to "xy" coordinates.
        (Also do the rotation which is something to change asap -> put every rotation into its own method)
        """
        
        angle_rad_x = (angle[0] * np.pi) / 180
        angle_rad_y = (angle[1] * np.pi) / 180
        angle_rad_z = (angle[2] * np.pi) / 180
        
        
        lst_proj = {}
        self.transPt = []
        self.transNrl = []
        for sommets, coord in self.sommets.items():
            self.x, self.y, self.z = coord[0] #Coord Vecteur Position
            self.xn, self.yn, self.zn = coord[2] # Coord Vecteur Normal
            
            # Rotation x
            self.x, self.y, self.z = self.rotation("x", angle_rad_x, self.x, self.y, self.z)
            self.xn, self.yn, self.zn = self.rotation("x", angle_rad_x, self.xn, self.yn, self.zn)
            
            
            # Rotation y
            self.x, self.y, self.z= self.rotation("y", angle_rad_y, self.x, self.y, self.z)
            self.xn, self.yn, self.zn= self.rotation("y", angle_rad_y, self.xn, self.yn, self.zn)
            
            # Rotation z
            self.x, self.y, self.z = self.rotation("z", angle_rad_z, self.x, self.y, self.z)
            self.xn, self.yn, self.zn = self.rotation("z", angle_rad_z, self.xn, self.yn, self.zn)
            self.transPt.append((self.x, self.y, self.z))
            self.transNrl.append((self.xn, self.yn, self.zn))
            # print(self.x, self.y, self.z)
            
            # Projection
            xi = ((self.x * distance_focale) // (self.z + self.distance_focale + 256)) + milieu_w
            yi = ((self.y * distance_focale) // (self.z + self.distance_focale + 256)) + milieu_h
            lst_proj[sommets] = (xi, yi)
            
        # print(self.transPt)
        # print(self.transNrl)
        # print(self.xn, self.yn, self.zn)
            
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
        
        x = float(mat_nouv_xyz.item(0))
        y = float(mat_nouv_xyz.item(1))
        z = float(mat_nouv_xyz.item(2))
        
        return x, y, z
        


    # def pos_arretes(self): # Changer en pos_surface(self)
    #     """
    #     Return an array which contain each edges with the "xy" position of the two vertices.
    #     """
        
    #     lst_arretes = []
    #     # lst_coord = self.render_3dto2d(self.angle)[0]    # type: ignore # Dictionnaire ->{'Sommet' : (pos_x, pos_y)}
    #     for origine, sommets in self.sommets.items():
    #         lst_sommets = sommets[1]    # Liste -> [Sommet, sommet, ... , sommet]
    #         if len(lst_sommets) != 0:
    #             for points in lst_sommets:
    #                 pos_origine = self.point[origine]
    #                 pos_sommets = self.point[points]
    #                 lst_arretes.append((pos_origine, pos_sommets))
    #                 # print(lst_arretes)
    #     return lst_arretes
    
    def dessine_arretes(self, p0, p1, p2, couleur):
        pygame.draw.line(self.display, couleur, p0, p1, 1)
        pygame.draw.line(self.display, couleur, p0, p2, 1)
        pygame.draw.line(self.display, couleur, p2, p1, 1)
        
    
    #  J'ai essayé de faire en sorte qu'on ne puisse pas voir les faces cachées...
    # Ca ne marche pas
    # Jpp
    def pos_faces(self):
        """
        Return an array which contain each faces with the "xy" coordinates of the face
        """
        lst_faces = []
        # lst_coord = self.render_3dto2d(self.angle)[0] # type: ignore
        # print(lst_coord)
        depthBuffer, depth = self.depthBuffer()
        for face in depthBuffer:
            p1 = self.point[face[0]]
            p2 = self.point[face[1]]
            p3 = self.point[face[2]]
            # print(p1, p2, p3)
            isShown = True

            lst_faces.append((p1, p2, p3, isShown))
            
        return lst_faces, depth
                  
    
    def depthBuffer(self):
        tempBuffer = []
        depthBuffer = []
        depth = []
        
        # Trie les faces selon la profondeur
        # print(self.faces)
        for face in self.faces:
            p0 = int(face[0][1:]) - 1
            p1 = int(face[1][1:]) - 1
            p2 = int(face[2][1:]) - 1
            
            a0 = self.transPt[p0][2]
            a1 = self.transPt[p1][2]
            a2 = self.transPt[p2][2]
            
            zMean = (a0 + a1 + a2) / 3
            depth.append(zMean)
            tempBuffer.append((zMean, face))
        tempBuffer.sort(reverse=True)
        depth.sort(reverse=True)
        # print(depth)
        
        # Récupère seulement les points de chaque face
        for vertices in tempBuffer:
            depthBuffer.append(vertices[1])
        # print(depthBuffer)
        return depthBuffer, depth
            
                      
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
    
    

    
