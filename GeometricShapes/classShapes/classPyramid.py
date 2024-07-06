from GeometricShapes.shapeDim import pyramide_sommets, pyramide_faces
from GeometricShapes.class3DRender import _3DRender

class Pyramid(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = pyramide_sommets
        self.faces = pyramide_faces
        
    def run(self):
        super().run()
    