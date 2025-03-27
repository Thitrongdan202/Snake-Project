import pygame
from config import CELL_SIZE, RED

class Food:
    def __init__(self):
        self.position = [10, 10]  # Vị trí cố định ban đầu

    def draw(self, screen):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)
