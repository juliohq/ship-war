import pygame

class Background:
    def __init__(self):
        self.background = pygame.image.load("assets/stars.png")
        self.offset_bg = pygame.Surface((400, 432))
        self.offset_bg.set_colorkey((0, 0, 0))
        self.speed = 64
        for x in range(13):
            for y in range(14):
                self.offset_bg.blit(self.background, (32 * x, 32 * y))
        self.offset = 0
    
    def _process(self, delta):
        if self.offset > 32:
            self.offset = 0
        else:
            self.offset += 1 * delta * self.speed
    
    def draw(self, screen):
        screen.blit(self.offset_bg, (0, self.offset - 32))
