from GeometricShapes.shapeDim import octahedre_sommets
from GeometricShapes.class3DRender import _3DRender

class Octahedron(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = octahedre_sommets
        
    def run(self):
        super().run()