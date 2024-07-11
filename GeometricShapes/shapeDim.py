import ObjFiles.ObjReader as objread

# Cube
cube_size = 100
cube_file = "ObjFiles/assets/cube.obj"
cube_sommets = objread.shape_caracteristics(cube_file, cube_size)[0]
cube_faces = objread.shape_caracteristics(cube_file, cube_size)[1]

# Pyramide
pyramide_size = 100
pyramide_file = "ObjFiles/assets/monkey.obj"
pyramide_sommets = objread.shape_caracteristics(pyramide_file, pyramide_size)[0]
pyramide_faces = objread.shape_caracteristics(pyramide_file, pyramide_size)[1]


# Tetraedre
tetraedre_size = 150
tetraedre_file = "ObjFiles/assets/human_model.obj"
tetraedre_sommets = objread.shape_caracteristics(tetraedre_file, tetraedre_size)[0]
tetraedre_faces = objread.shape_caracteristics(tetraedre_file, tetraedre_size)[1]

# Octahedre
octahedre_size = 100  # Taille des demi-côtés du carré de base, ou hauteur des apex par rapport au centre
octahedre_file = "ObjFiles/assets/octahedron.obj"
octahedre_sommets = objread.shape_caracteristics(octahedre_file, octahedre_size)[0]
octahedre_faces = objread.shape_caracteristics(octahedre_file, octahedre_size)[1]

# Cone
cone_size = 100
cone_file = "ObjFiles/assets/cone.obj"
cone_sommets = objread.shape_caracteristics(cone_file, cone_size)[0]
cone_faces = objread.shape_caracteristics(cone_file, cone_size)[1]

# cone_base_radius = 100
# cone_height = 200
# num_base_points = 20

# # Initialiser le dictionnaire des sommets
# cone_sommets = {}

# # Ajouter les points de la base circulaire
# for i in range(num_base_points):
#     angle = 2 * math.pi * i / num_base_points
#     x = cone_base_radius * math.cos(angle)
#     y = cone_base_radius * math.sin(angle)
#     next_point = f'B{(i + 1) % num_base_points + 1}'
#     cone_sommets[f'B{i + 1}'] = [[x, y, 0], ['A', next_point]]  # Chaque point de la base est connecté à l'apex et à son voisin de droite

# # Ajouter le sommet du cône
# cone_sommets['A'] = [[0, 0, cone_height], [f'B{i + 1}' for i in range(num_base_points)]]

# Whatever
file_whatever = 'ObjFiles/assets/monkey.obj'
size_whatever = 250
whatever_sommets = objread.shape_caracteristics(file_whatever, size_whatever)[0]
whatever_faces = objread.shape_caracteristics(file_whatever, size_whatever)[1]
# print(whatever_sommets)