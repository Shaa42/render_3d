from GeometricShapes.shapeDim import tetraedre_sommets
from GeometricShapes.class3DRender import _3DRender

class Tetraedre(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = tetraedre_sommets
        
    def run(self):
        super().run()
    
