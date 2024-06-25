from GeometricShapes.shapeDim import whatever_sommets
from GeometricShapes.class3DRender import _3DRender

class Whatever(_3DRender):
    def __init__(self, display, gameStateManager):
        super().__init__(display, gameStateManager)
        self.sommets = whatever_sommets
        
    def run(self):
        super().run()