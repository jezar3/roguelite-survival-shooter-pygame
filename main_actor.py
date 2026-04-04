import pygame
import math

class Player:
    def __init__(self, x, y, speed):
        self.speed = speed

        self.image_idle_down = pygame.image.load('assets/running-Veritical/idle_down.png').convert_alpha()

        self.current_image = self.image_idle_down
        self.rect = self.current_image.get_rect(topleft=(x, y))

    def wasd(self):
        keys = pygame.key.get_pressed()
        self.move = False

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.move = True
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.move = True
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.move = True
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.move = True

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.mouse_angle = math.degrees(math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx))

    def draw(self, screen, camera):
        screen.blit(self.current_image, camera.apply(self.rect))