from random import randrange
import pygame
import random
from pygame.math import Vector2
from pygame.locals import *

from scripts.enemy import Enemy

class Spawn:
    def __init__(self, inputs, process, pipeline, free, add_enemy, add_shot):
        self.h = -32
        self.delay = 2000
        self.inputs = inputs
        self.process = process
        self.pipeline = pipeline
        self.free = free
        self.id = self.get_id()
        self.add_enemy = add_enemy
        self.add_shot = add_shot
        pygame.time.set_timer(pygame.event.Event(self.id), self.delay)
        # print(f"created spawn with id {self.id}")
    
    def get_id(self):
        return random.randrange(2 ** 16)
    
    def _input(self, event):
        if event.type == self.id:
            self.spawn()
    
    def spawn(self):
        pos = Vector2(randrange(16, 484), self.h)
        enemy = Enemy(self.inputs, self.process, self.pipeline, self.free, self.add_shot)
        self.add_enemy(enemy)
        enemy.set_pos(pos)
        self.process(enemy)
        self.pipeline(enemy)
