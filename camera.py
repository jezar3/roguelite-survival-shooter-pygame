import pygame

class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width 
        self.height = height 

  
    def update(self, target):
        
        #player position - half of the screen (center) 
        #then substract it again from the player position or sum like dat
        self.offset_x = target.rect.centerx - self.width // 2
        self.offset_y = target.rect.centery - self.height // 2

    def apply(self, rect):
         return pygame.Rect(
            rect.x - self.offset_x,
            rect.y - self.offset_y,
            rect.width,
            rect.height)
        