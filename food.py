import pygame
import random
from config import CELL_SIZE, RED, CELL_WIDTH, CELL_HEIGHT

class Food:
    def __init__(self):
        self.position = [10, 10]

    def draw(self, screen):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

    def random_position(self):
        self.position = [
            random.randint(0, CELL_WIDTH - 1),
            random.randint(0, CELL_HEIGHT - 1)
        ]
