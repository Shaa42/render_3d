import numpy as np



"""
Functions
A ajouter :
    -> Données normalisées dans [0, 1]
    -> Problemes avec les arretes
"""

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
            temp_vertex.append(int(extract(element)))
        lst_vertex.append(temp_vertex)
    return lst_vertex

def extract(string : str) -> str:
    tmp = ''
    for character in string:
        if character != '/':
            tmp += character
        if character == '/':
            return tmp
    return tmp

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
    # print(f)
    lst_vertices = get_face_vertex(f) # Probleme : récupère que la premiere composante, couillon ------------------------------ #
    # print(lst_vertices)
    lst_notation = convert_to_vertex_notation(lst_vertices)
    sommets = {}
    for points_index in range(len(v)):
        points = v[points_index]
        sommets[f'S{points_index + 1}'] = [np.array(points) * size, []]
    for i in range(len(lst_notation)):
        elements = lst_notation[i]
        for element in elements[1:]:
            if element not in sommets[elements[0]][1]:
                sommets[elements[0]][1].append(element)
    return sommets
    
"""
Main
"""

if __name__ == "__main__":
    sommets = shape_caracteristics("ObjFiles/assets/sphere.obj", 100)
    print(sommets)