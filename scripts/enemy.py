import pygame
from pygame.locals import *
from pygame.math import Vector2

from scripts.ship import Ship

class Enemy(Ship):
    def __init__(self, inputs, process, pipeline, free, add_shot):
        super().__init__(inputs, process, pipeline, free, add_shot)
        self.sprite = pygame.transform.flip(pygame.image.load("assets/enemy.png"), False, True)
        self._dir = Vector2(0, 1)
        self.speed = 16
        self.delay = 2000
        self.destroy_sound = pygame.mixer.Sound("assets/enemy_destroy.wav")
        self.destroy_sound.set_volume(0.25)
    
    def shoot(self):
        if super().shoot():
            return
    
    def _process(self, delta):
        super()._process(delta)
        if self.pos.y > 432:
            self.free(self)
