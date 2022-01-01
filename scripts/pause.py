import pygame
from pygame.locals import *

class Pause:
    def __init__(self, font):
        self.background = pygame.Surface((400, 400))
        self.background.set_alpha(128)
        self.foreground = font.render("PAUSED", True, (255, 255, 255))
        self.fg_rect = self.foreground.get_rect(center=(200, 200))
        self.delay = 500
        self.sound = pygame.mixer.Sound("assets/pause.wav")
        self.showing_text = True
        self.start()
    
    def start(self):
        pygame.time.set_timer(92, self.delay)
    
    def reset(self):
        self.showing_text = True
        pygame.time.set_timer(92, 0)
    
    def _input(self, event):
        if event.type == 92:
            self.showing_text = not self.showing_text
            self.start()
    
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        if self.showing_text:
            screen.blit(self.foreground, self.fg_rect)
