import pygame
import sys
from main_actor import Player
from worldtest import Tile_Map
from weather import Weather
from camera import Camera



pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = window.get_size()

clock = pygame.time.Clock()




player  = Player(700, 700, 6.5)
tilemap = Tile_Map()
camera  = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
weather = Weather(SCREEN_WIDTH, SCREEN_HEIGHT)

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
    tilemap.draw_world(camera, SCREEN_WIDTH, SCREEN_HEIGHT, window)
    player.draw(window, camera)
    weather.update()
    weather.draw(window)
    

    pygame.display.update()
    clock.tick(999)