import pygame
import sys
from main_actor import Player
from worldtest import TileMap
from camera import Camera


pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = window.get_size()

player  = Player(700, 700, 6.5)
tilemap = TileMap()
camera  = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


clock = pygame.time.Clock()
gameIsRunning = True

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    player.wasd()
    camera.update(player)
    

    window.fill((0, 0, 0))
    tilemap.draw(window, camera.offset_x, camera.offset_y, SCREEN_WIDTH, SCREEN_HEIGHT)
    player.draw(window, camera)
    

    pygame.display.update()
    clock.tick(60)