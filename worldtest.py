import random
import pygame

'''changed '''

class Tile_Map:
    
    def __init__(self):
        self.tilePixelSize = 8       
        self.tiles_per_chunk = 32  
        self.chunk_pixels = self.tilePixelSize * self.tiles_per_chunk  
        self.chunks = {} #connected w the get chunk function

       
        self.tree_image = pygame.image.load("assets/world assets/magical_spruce_tree.png").convert_alpha()
        
     
        self.tree_image = pygame.transform.scale(self.tree_image, (256, 256))

    def generate_chunk(self, col, row):
        surface = pygame.Surface((self.chunk_pixels, self.chunk_pixels))
        
        rng = random.Random(col + row * 10000)
        
        
        for tile_row in range(self.tiles_per_chunk):
            for tile_col in range(self.tiles_per_chunk):
                
                snow = rng.randint(220, 245)
            
                color = (snow, snow, int(snow * 0.98))

                #Each tile is placed 8 pixels apart so dis is more like 8, 16, 24 
                positionInWorld_X = tile_col * self.tilePixelSize
                positionInWorld_Y = tile_row * self.tilePixelSize
                
                #the format for the tuple is a pygame built in thing (x, y, width, height)
                
                pygame.draw.rect(surface, color, (positionInWorld_X, positionInWorld_Y, self.tilePixelSize, self.tilePixelSize))
               
   
        spawn_tree = rng.random() < 0.027

        if spawn_tree:
          
            tree_x = rng.randint(0, self.chunk_pixels - 256)
            tree_y = rng.randint(0, self.chunk_pixels - 256)
            
          
            surface.blit(self.tree_image, (tree_x, tree_y))
        
        return surface

    def get_chunk(self, col, row):
       
        if (col, row) not in self.chunks:
            
            self.chunks[(col, row)] = self.generate_chunk(col, row)

        return self.chunks[(col, row)]

    def draw_world(self, camera, SCREEN_WIDTH, SCREEN_HEIGHT, window):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        
        
        
        self.first_column = (camera.offset_x // self.tilePixelSize) // self.tiles_per_chunk 
        self.first_row = (camera.offset_y // self.tilePixelSize) // self.tiles_per_chunk  
        self.last_column  = self.first_column + (self.SCREEN_WIDTH  // self.chunk_pixels) + 4
        self.last_row  = self.first_row + (self.SCREEN_HEIGHT // self.chunk_pixels) + 4 
        
        for row in range(self.first_row, self.last_row):
            for col in range(self.first_column, self.last_column):

                surface = self.get_chunk(col, row)

                x = col * self.chunk_pixels - camera.offset_x
                y = row * self.chunk_pixels - camera.offset_y

                window.blit(surface, (x, y))