import pygame
from pygame.locals import *
from pygame.math import Vector2

from scripts.ship import Ship
from scripts.player_shot import PlayerShot

class Player(Ship):
    def __init__(self, inputs, process, pipeline, free, add_shot):
        super().__init__(inputs, process, pipeline, free, add_shot)
        self.sprite = pygame.image.load("assets/player.png")
        self.limits = [0, 368]
        self.destroy_sound = pygame.mixer.Sound("assets/player_destroy.wav")
        self.destroy_sound.set_volume(0.25)
    
    def shoot(self):
        if not super().shoot():
            return
        pygame.time.set_timer(pygame.event.Event(self.id), self.cooldown)
        
        self.can_shoot = False
        shot = PlayerShot(self.free)
        shot.set_pos(self.pos + Vector2(14, 0))
        self.process(shot)
        self.pipeline(shot)
        self.add_shot(shot)
    
    def _process(self, delta):
        super()._process(delta)
        if self.pos.x <= self.limits[0]:
            self.pos.x = self.limits[0]
        elif self.pos.x >= self.limits[1]:
            self.pos.x = self.limits[1]

        if self.shooting:
            self.shoot()
    
    def _input(self, event):
        if event.type == self.id:
            self.can_shoot = True
        elif event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self._dir[0] = -1
            elif event.key == K_RIGHT or event.key == K_d:
                self._dir[0] = 1
            elif event.key == K_SPACE:
                self.shooting = True
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_a or event.key == K_d:
                self._dir[0] = 0
            elif event.key == K_SPACE:
                self.shooting = False
