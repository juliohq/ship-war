import pygame
from pygame.math import Vector2

class Shot:
    def __init__(self, free):
        self.free = free
        self.pos = Vector2()
        self.speed = 256
        self.dir = Vector2()
        self.sprite = pygame.image.load("assets/shot.png")
        self.update_mask()
    
    def update_mask(self):
        self.mask = self.sprite.get_rect()
    
    def _process(self, delta):
        self.pos += self.dir * self.speed * delta
        
        if self.pos.y < -4 or self.pos.y > 404:
            self.free(self)
    
    def set_pos(self, pos):
        self.pos = pos
    
    def draw(self, screen):
        screen.blit(self.sprite, self.pos)
