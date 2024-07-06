from GeometricShapes.shapeDim import octahedre_sommets, octahedre_faces
from GeometricShapes.class3DRender import _3DRender

class Octahedron(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = octahedre_sommets
        self.faces = octahedre_faces
        
    def run(self):
        super().run()