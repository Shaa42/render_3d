from GeometricShapes.shapeDim import cube_sommets, cube_faces
from GeometricShapes.class3DRender import _3DRender

class Cube(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = cube_sommets
        self.faces = cube_faces
        
    def run(self):
        super().run()
    