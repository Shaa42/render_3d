from GeometricShapes.shapeDim import cone_sommets, cone_faces
from GeometricShapes.class3DRender import _3DRender

class Cone(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = cone_sommets
        self.faces = cone_faces
        
    def run(self):
        super().run()