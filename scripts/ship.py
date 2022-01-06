import pygame
from pygame.math import Vector2

import random

class Ship:
    def __init__(self, inputs, process, pipeline, free, add_shot):
        self.pos = Vector2()
        self.speed = 128
        self._dir = Vector2()
        self.cooldown = 250
        self.health = 3
        self.can_shoot = True
        self.shooting = False
        self.inputs = inputs
        self.process = process
        self.pipeline = pipeline
        self.free = free
        self.id = self.get_id()
        self.sprite = pygame.image.load("assets/ship.png")
        self.shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
        self.shoot_sound.set_volume(0.12)
        self.update_mask()
        self.add_shot = add_shot
        self.destroyed = False
        # print(f"created ship with id {self.id}")
    
    def destroy(self):
        if not self.destroyed:
            self.destroyed = True
            self.destroy_sound.play()
            self.free(self)
    
    def get_id(self):
        return random.randrange(2 ** 16)
    
    def update_mask(self):
        self.mask = self.sprite.get_rect()
    
    def shoot(self):
        if not self.can_shoot:
            return False
        self.shoot_sound.play()
        return True
    
    def _process(self, delta):
        self.move(self._dir * self.speed, delta)
    
    def set_pos(self, vec):
        self.pos = vec
    
    def move(self, offset, delta):
        self.pos += offset * delta
    
    def draw(self, screen):
        self.mask = screen.blit(self.sprite, self.pos)
