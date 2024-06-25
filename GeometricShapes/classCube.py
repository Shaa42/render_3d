from GeometricShapes.shapeDim import cube_sommets
from GeometricShapes.class3DRender import _3DRender

class Cube(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = cube_sommets
        
    def run(self):
        super().run()
    