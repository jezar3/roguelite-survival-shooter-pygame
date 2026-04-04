import pygame
import sys
from main_actor import Player
from worldtest import TileMap
from camera import Camera
from vignette import Vignette
from cameraTest import Camera

pygame.init()


window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = window.get_size()

player = Player(700, 700, 10)
tilemap = TileMap()  
cameratest = Camera(WIDTH, HEIGHT)


gameIsRunning = True
clock = pygame.time.Clock()

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    player.wasd()
    

    cameratest.update(player)
   

    window.fill((0, 0, 0))

    player.draw(window )


    pygame.display.update()
    clock.tick(9999)