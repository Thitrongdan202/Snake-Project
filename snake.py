import pygame
from config import CELL_SIZE, GREEN

class Snake:
    """Rắn khởi đầu 3 đoạn, hỗ trợ grow."""
    def __init__(self):
        self.body      = [[5, 10], [4, 10], [3, 10]]
        self.direction = "RIGHT"

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(
                screen, GREEN,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def move(self, grow: bool = False):
        head = self.body[0].copy()
        if   self.direction == "RIGHT": head[0] += 1
        elif self.direction == "LEFT" : head[0] -= 1
        elif self.direction == "UP"   : head[1] -= 1
        elif self.direction == "DOWN" : head[1] += 1

        self.body.insert(0, head)
        if not grow:
            self.body.pop()
