import pygame
from noise import pnoise2

TILE_SIZE = 8
CHUNK_SIZE = 32

class Chunk:
    def __init__(self, chunk_x, chunk_y):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.surface = pygame.Surface((CHUNK_SIZE * TILE_SIZE, CHUNK_SIZE * TILE_SIZE))

        for row in range(CHUNK_SIZE):
            for col in range(CHUNK_SIZE):
                world_col = self.chunk_x * CHUNK_SIZE + col
                world_row = self.chunk_y * CHUNK_SIZE + row

                n = pnoise2(world_col * 0.04, world_row * 0.04, octaves=6)
                t = (n + 1) / 2

                
                r = int(45 + t * 40)
                g = int(32 + t * 28)
                b = int(18 + t * 18)
                pygame.draw.rect(self.surface, (r, g, b), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                
    def draw(self, screen, camera):
        world_x = self.chunk_x * CHUNK_SIZE * TILE_SIZE
        world_y = self.chunk_y * CHUNK_SIZE * TILE_SIZE
        screen.blit(self.surface, camera.apply(pygame.Rect(world_x, world_y, CHUNK_SIZE * TILE_SIZE, CHUNK_SIZE * TILE_SIZE)))


class TileMap:
    def __init__(self):
        self.chunks = {}
        self.visible_chunks = []

    def get_chunk(self, chunk_x, chunk_y):
        key = (chunk_x, chunk_y)
        if key not in self.chunks:
            self.chunks[key] = Chunk(chunk_x, chunk_y)
        return self.chunks[key]

  