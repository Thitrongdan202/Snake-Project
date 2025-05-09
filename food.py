import pygame, random
from config import CELL_SIZE, RED, CELL_WIDTH, CELL_HEIGHT

class Food:
    def __init__(self):
        self.position = [10, 10]

    def draw(self, screen):
        pygame.draw.rect(
            screen, RED,
            (self.position[0] * CELL_SIZE,
             self.position[1] * CELL_SIZE,
             CELL_SIZE, CELL_SIZE)
        )

    def random_position(self, forbidden=None):
        """Đặt vị trí mới, tránh 'forbidden' (set các tuple (x,y))."""
        if forbidden is None:
            forbidden = set()

        while True:
            self.position = [
                random.randint(1, CELL_WIDTH  - 2),  # tránh viền
                random.randint(1, CELL_HEIGHT - 2)
            ]
            if tuple(self.position) not in forbidden:
                break
