# food.py
import pygame
import random
from config import CELL_SIZE, RED, CELL_WIDTH, CELL_HEIGHT

class Food:
    """Mồi đỏ – sinh ngẫu nhiên, tránh tường & thân rắn"""
    def __init__(self):
        self.position = [10, 10]

    def draw(self, screen):
        rect = pygame.Rect(self.position[0] * CELL_SIZE,
                           self.position[1] * CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

    def random_position(self, forbidden=None):
        if forbidden is None:
            forbidden = set()

        while True:
            self.position = [
                random.randint(1, CELL_WIDTH - 2),     # tránh viền
                random.randint(1, CELL_HEIGHT - 2)
            ]
            if tuple(self.position) not in forbidden:
                break
