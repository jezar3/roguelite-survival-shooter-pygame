import pygame
import math
#
class mouse:
    def __init__(selc):
        self.mouse_x = 0
        self.mouse_y = 0
        self.angle = 0
        
    def update(self):
        self.mouse_x, self.mouse = pygame.mouse.get_pos()
        
        angle = math.degrees(math.atan2(self.mouse_x, self.mouse))
        
        #conditional statements later on based on left click then sprite will change based on that. 8 direction sprite
                
      