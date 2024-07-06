from GeometricShapes.shapeDim import whatever_sommets, whatever_faces
from GeometricShapes.class3DRender import _3DRender

class Whatever(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = whatever_sommets
        self.faces = whatever_faces
        
    def run(self):
        super().run()