import numpy as np


# lecture et structuration des données :
def read_vertex_data(value : list[str]) -> list[float]:
    return [
        float(value[1]),
        float(value[2]),
        float(value[3])
    ]

def read_normal_data(value : list[str]) -> list[float]:
        return [
            float(value[1]),
            float(value[2]),
            float(value[3])
    ]
        
def read_faces_data(value : list[str]):
    return [
        value[1],
        value[2],
        value[3].strip()
    ]
    
def read_texcoord_data(value : list[str]) -> list[float]:
    return [
        float(value[1]),
        float(value[2])
    ] 

def get_face_vertex(faces : list[str]) -> list[list[int]]:
    lst_vertex = []
    for face_index in range(len(faces)):
        temp_vertex = []
        face = faces[face_index]
        for element in face :
            # print(element)
            temp_vertex.append(int(extract(element)[0]))
            # print(extract(element))
        lst_vertex.append(temp_vertex)
    return lst_vertex

def extract(string : str) -> list[str]:
    tmp = ''
    lst_char = []
    for character in string:
        if character != '/':
            tmp += character
        if character == '/':
            lst_char.append(tmp)
            tmp = ''
    lst_char.append(tmp)
    return lst_char

def convert_to_vertex_notation(vertices):
    notation_list = []
    for i in range(len(vertices)):
        notation_list.append(tuple(map(lambda x : f'S{x}', vertices[i])))
    return notation_list

# Fonction lecture .obj :
def open_file(obj_file : str) -> tuple[list, list, list, list]:
    """
    Ouvre un fichier de type .obj et lit les différentes informations
    """
    with open(obj_file, 'r') as file:
        line = file.readline()
        
        v = []
        vt = []
        vn = []
        f = []
        
        while line:
            words = line.split(' ')
            # print(words)
            if '' in words:
                words.remove('')
            if words[0] == 'v' and words != '':
                v.append(read_vertex_data(words))
            if words[0] == 'vt' and words != '':
                vt.append(read_texcoord_data(words))
            if words[0] == 'vn' and words != '':
                vn.append(read_normal_data(words))
            if words[0] == 'f' and words != '':
                f.append(read_faces_data(words))
            line = file.readline()
            
    return v, vt, vn, f 

def shape_caracteristics(file : str, size):
    v, vt, vn, f = open_file(file)
    # print(vn)
    lst_vertices = get_face_vertex(f) # Liste de chaque face : [(P0, P1, P2) -> Face, ...]
    # print(lst_vertices)
    lst_notation = convert_to_vertex_notation(lst_vertices)
    # print(lst_notation)
    
    # Crée le dictionnaire des sommets et ajoute les coordonnées 
    sommets = {}
    for points_index in range(len(v)):
        points = v[points_index]
        sommets[f'S{points_index + 1}'] = [np.array(points) * size, [], []]
    
    # Ajoute les sommets voisins
    for i in range(len(lst_notation)):
        elements = lst_notation[i]
        for element in elements[1:]:
            if element not in sommets[elements[0]][1]:
                sommets[elements[0]][1].append(element)
                
    # Ajoute les coordonnées du vecteur normal associé au point
    for i in range(len(f)):
        faces = f[i]
        for face in faces:
            indFace = extract(face)[0]
            indNormal = int(extract(face)[2]) - 1
            if len(sommets[f"S{indFace}"][2]) < 1:
                sommets[f"S{indFace}"][2] = vn[indNormal]
        
    return sommets, lst_notation
    
"""
Main
"""

if __name__ == "__main__":
    sommets = shape_caracteristics("ObjFiles/assets/cube.obj", 100)
    # print(sommets)
    print(np.dot((1, 0, 0), (1, 0, 0)))