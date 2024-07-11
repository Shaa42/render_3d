from GeometricShapes.shapeDim import tetraedre_sommets, tetraedre_faces
from GeometricShapes.class3DRender import _3DRender

class Tetraedre(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = tetraedre_sommets
        self.faces = tetraedre_faces
        
    def run(self):
        super().run()
    
