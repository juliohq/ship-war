import pygame
from pygame.locals import *
from pygame.math import Vector2

from scripts.player import Player
from scripts.spawn import Spawn
from scripts.background import Background
from scripts.pause import Pause

import sys

# init mixer
pygame.mixer.pre_init()
# init pygame
pygame.init()
# get display surface
screen = pygame.display.set_mode((400, 400), pygame.SCALED | pygame.RESIZABLE)
# set window caption
pygame.display.set_caption("Ship War")
# lod default font
fnt = pygame.font.SysFont(None, 20)

# init music
music = pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

# globals
paused = False

# level data
# input pipeline
inputs = []
# process pipeline
process = []
# draw pipeline
pipeline = []

def add2input(obj):
    inputs.append(obj)

def add2process(obj):
    process.append(obj)

def add2pipeline(obj):
    pipeline.append(obj)

def free(obj):
    if obj in inputs:
        inputs.remove(obj)
    if obj in process:
        process.remove(obj)
    if obj in pipeline:
        pipeline.remove(obj)

def add_player_shot(shot):
    player_shots.append(shot)

player = Player(add2input, add2process, add2pipeline, free, add_player_shot)
add2input(player)
add2process(player)
add2pipeline(player)
player.set_pos(Vector2(200, 352))

# enemies
enemies = []
# player shots
player_shots = []
# enemy shots
enemy_shots = []

def add_enemy(enemy):
    enemies.append(enemy)

def add_enemy_shot(shot):
    enemy_shots.append(shot)

spawn = Spawn(add2input, add2process, add2pipeline, free, add_enemy, add_enemy_shot)
add2input(spawn)

# get a clock
clock = pygame.time.Clock()

# background
bg = Background()
add2process(bg)

# pause
pause = Pause(fnt)

def draw_text(font, text):
    return font.render(text, True, (255, 255, 255))

def draw_fps():
    fps = draw_text(fnt, str(f"{round(clock.get_fps())} FPS"))
    inp = draw_text(fnt, f"events: {len(inputs)}")
    proc = draw_text(fnt, f"process: {len(process)}")
    pipe = draw_text(fnt, f"pipeline: {len(pipeline)}")
    
    screen.blit(fps, (0, 0))
    screen.blit(inp, (0, 20))
    screen.blit(proc, (0, 40))
    screen.blit(pipe, (0, 60))

running = True
is_drawing_fps = True

while running:
    delta = clock.tick(60) / 1000
    
    # input
    for event in pygame.event.get():
        if paused:
            pause._input(event)
        else:
            for obj in inputs:
                obj._input(event)
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN and event.key == K_p:
            paused = not paused
            pause.sound.play()
            if paused:
                pygame.mixer.music.set_volume(0.07)
                add2input(pause)
                add2pipeline(pause)
                pause.start()
            else:
                pygame.mixer.music.set_volume(0.25)
                free(pause)
                pause.reset()
    
    # collisions
    if not player.destroyed and player.mask.collidelist([enemy.mask for enemy in enemies]) != -1:
        player.destroy()
    for enemy in enemies:
        for shot in player_shots:
            if enemy.mask.colliderect(shot.mask):
                player_shots.remove(shot)
                shot.free(shot)
                enemy.destroy()
                break
    
    # process
    if not paused:
        for obj in process:
            obj._process(delta)
    
    # draw
    screen.fill((50, 51, 83))
    bg.draw(screen)
    
    for obj in pipeline:
        obj.draw(screen)
    
    if is_drawing_fps:
        draw_fps()
    pygame.display.flip()

# clear game
inputs.clear()
process.clear()
pipeline.clear()

pygame.quit()
sys.exit()
