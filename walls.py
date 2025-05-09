import pygame
from config import (
    CELL_SIZE, CELL_WIDTH, CELL_HEIGHT,
    WALL_COLOR, WALL_THICKNESS
)

class Walls:
    """Sinh viền bao quanh và kiểm tra va chạm."""
    def __init__(self):
        self.blocks = (
            [[x, 0] for x in range(CELL_WIDTH)] +
            [[x, CELL_HEIGHT - 1] for x in range(CELL_WIDTH)] +
            [[0, y] for y in range(CELL_HEIGHT)] +
            [[CELL_WIDTH - 1, y] for y in range(CELL_HEIGHT)]
        )

    def draw(self, screen):
        outer = pygame.Rect(0, 0,
                            CELL_WIDTH  * CELL_SIZE,
                            CELL_HEIGHT * CELL_SIZE)
        pygame.draw.rect(screen, WALL_COLOR, outer, WALL_THICKNESS)

    def is_collision(self, pos):
        return pos in self.blocks   # pos là [x, y]
