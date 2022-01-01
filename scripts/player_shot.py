from pygame.math import Vector2

from scripts.shot import Shot

class PlayerShot(Shot):
    def __init__(self, free):
        super().__init__(free)
        self.dir = Vector2(0, -1)
