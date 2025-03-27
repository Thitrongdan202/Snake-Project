import pygame
from config import CELL_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [
            [5, 10],
            [4, 10],
            [3, 10]
        ]  # 3 đoạn, mỗi đoạn là [x, y] trên lưới

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
