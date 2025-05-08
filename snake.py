import pygame
from config import CELL_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [
            [5, 10],
            [4, 10],
            [3, 10]
        ]
        self.direction = "RIGHT"

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

    def move(self, grow=False):
        head = self.body[0].copy()

        if self.direction == "RIGHT":
            head[0] += 1
        elif self.direction == "LEFT":
            head[0] -= 1
        elif self.direction == "UP":
            head[1] -= 1
        elif self.direction == "DOWN":
            head[1] += 1

        self.body.insert(0, head)
        # self.body.pop()  # luôn giữ 3 đoạn
        if not grow:
            self.body.pop()  # Xoá đuôi nếu không ăn mồi
