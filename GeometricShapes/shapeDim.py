import math
import ObjFiles.ObjReader as objread
import numpy as np

# Cube
cube_size = 100
cube_file = "ObjFiles/assets/cube.obj"
cube_sommets = objread.shape_caracteristics(cube_file, cube_size)

# c_v, c_vt, c_vn = objread.open_file(cube_file)

# cube_sommets = {'A' : [np.array([cube_size, cube_size, cube_size]), ['B', 'E']],
#                 'B' : [np.array([cube_size, -cube_size, cube_size]), ['C', 'F']],
#                 'C' : [np.array([-cube_size, -cube_size, cube_size]), ['D', 'G']],
#                 'D' : [np.array([-cube_size, cube_size, cube_size]), ['A', 'H']],
#                 'E' : [np.array([cube_size, cube_size, -cube_size]), ['F']],
#                 'F' : [np.array([cube_size, -cube_size, -cube_size]), ['G']],
#                 'G' : [np.array([-cube_size, -cube_size, -cube_size]), ['H']],
#                 'H' : [np.array([-cube_size, cube_size ,-cube_size]), ['E']]}

# Pyramide
pyramide_size = 500  # Taille de la moitié du côté de la base
pyramide_file = "ObjFiles/assets/basic_pyramid.obj"
pyramide_sommets = objread.shape_caracteristics(pyramide_file, pyramide_size)
# print(pyramide_sommets)

# pyramide_height = 200 # Hauteur de la pyramide

# pyramide_sommets = {
#     'A': [[pyramide_size, pyramide_size, 0], ['B', 'D', 'E']],  # Sommet de la base
#     'B': [[-pyramide_size, pyramide_size, 0], ['A', 'C', 'E']],  # Sommet de la base
#     'C': [[-pyramide_size, -pyramide_size, 0], ['B', 'D', 'E']],  # Sommet de la base
#     'D': [[pyramide_size, -pyramide_size, 0], ['A', 'C', 'E']],  # Sommet de la base
#     'E': [[0, 0, pyramide_height], ['A', 'B', 'C', 'D']]  # Sommet (apex)
# }


# Tetraedre
tetraedre_size = 100
tetraedre_sommets = {'A' : [[tetraedre_size, tetraedre_size, tetraedre_size], ['B', 'E']],
                     'B' : [[tetraedre_size, -tetraedre_size, tetraedre_size], ['C', 'E']],
                     'C' : [[-tetraedre_size, -tetraedre_size, tetraedre_size], ['A', 'E']],
                     'E' : [[tetraedre_size, -tetraedre_size, -tetraedre_size], []]}

# Octahedre
octahedre_size = 150  # Taille des demi-côtés du carré de base, ou hauteur des apex par rapport au centre

octahedre_sommets = {
    'A': [[octahedre_size, 0, 0], ['D', 'C']],   # (1, 0, 0)
    'B': [[-octahedre_size, 0, 0], ['D', "C"]],       # (-1, 0, 0)
    'C': [[0, octahedre_size, 0], ['E', 'F']],   # (0, 1, 0)
    'D': [[0, -octahedre_size, 0], ['F', 'E']],       # (0, -1, 0)
    'E': [[0, 0, octahedre_size], ['A', 'B']],   # (0, 0, 1)
    'F': [[0, 0, -octahedre_size], ['A', 'B']]        # (0, 0, -1)
}

# Cone
cone_base_radius = 100
cone_height = 200
num_base_points = 20

# Initialiser le dictionnaire des sommets
cone_sommets = {}

# Ajouter les points de la base circulaire
for i in range(num_base_points):
    angle = 2 * math.pi * i / num_base_points
    x = cone_base_radius * math.cos(angle)
    y = cone_base_radius * math.sin(angle)
    next_point = f'B{(i + 1) % num_base_points + 1}'
    cone_sommets[f'B{i + 1}'] = [[x, y, 0], ['A', next_point]]  # Chaque point de la base est connecté à l'apex et à son voisin de droite

# Ajouter le sommet du cône
cone_sommets['A'] = [[0, 0, cone_height], [f'B{i + 1}' for i in range(num_base_points)]]

# Whatever
file_whatever = 'ObjFiles/assets/frog.obj'
size_whatever = 3
whatever_sommets = objread.shape_caracteristics(file_whatever, size_whatever)
# print(whatever_sommets)