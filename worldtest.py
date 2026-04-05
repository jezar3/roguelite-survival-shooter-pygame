import random
import pygame

'''i originally made this '''

class Tile_Map:
    
    def __init__(self):
        self.tilePixelSize = 8       
        self.tiles_per_chunk = 32  
        self.chunk_pixels = self.tilePixelSize * self.tiles_per_chunk  
        self.chunks = {} #connected w the get chunk function

    def generate_chunk(self, col, row):
        surface = pygame.Surface((self.chunk_pixels, self.chunk_pixels))
        
        rng = random.Random(col + row * 10000)
        for row in range(self.tiles_per_chunk):
            for column in range(self.tiles_per_chunk):
                
                brown = rng.randint(38, 58)
            
                color = (brown, int(brown * 0.7), int(brown * 0.4))

                #Each tile is placed 8 pixels apart so dis is more like 8, 16, 24 
                positionInWorld_X = column * self.tilePixelSize
                positionInWorld_Y = row * self.tilePixelSize
                
                #the format for the tuple is a pygame built in thing (x, y, width, height)
                
                pygame.draw.rect(surface, color, (positionInWorld_X, positionInWorld_Y, self.tilePixelSize, self.tilePixelSize))
               
        return surface

    def get_chunk(self, col, row):
       
        if (col, row) not in self.chunks:
            
            self.chunks[(col, row)] = self.generate_chunk(col, row)

        return self.chunks[(col, row)]

    def draw_world(self, camera, SCREEN_WIDTH, SCREEN_HEIGHT, window):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        
        
        #draws near cam only
        self.first_column = (camera.offset_x // self.tilePixelSize) // self.tiles_per_chunk 
        self.first_row = (camera.offset_y // self.tilePixelSize) // self.tiles_per_chunk 
        self.last_column  = self.first_column + (self.SCREEN_WIDTH  // self.chunk_pixels) 
        self.last_row  = self.first_row + (self.SCREEN_HEIGHT // self.chunk_pixels) 
        
        for row in range(self.first_row, self.last_row):
            for col in range(self.first_column, self.last_column):

                surface = self.get_chunk(col, row)

                x = col * self.chunk_pixels - camera.offset_x
                y = row * self.chunk_pixels - camera.offset_y

                window.blit(surface, (x, y))