# walls.py
import pygame
from config import (
    CELL_SIZE,
    CELL_WIDTH,
    CELL_HEIGHT,
    WALL_COLOR,
    WALL_THICKNESS,   # thêm vào config.py: WALL_THICKNESS = 4
)

class Walls:
    """
    Sinh tường viền:
    • blocks  : danh sách ô (x, y) dùng cho va chạm
    • draw()  : vẽ khung viền mỏng theo WALL_THICKNESS pixel
    """
    def __init__(self):
        self.blocks = []

        # Khung viền bằng toạ độ lưới (dùng collision)
        for x in range(CELL_WIDTH):
            self.blocks.append([x, 0])                      # trên
            self.blocks.append([x, CELL_HEIGHT - 1])        # dưới
        for y in range(CELL_HEIGHT):
            self.blocks.append([0, y])                      # trái
            self.blocks.append([CELL_WIDTH - 1, y])         # phải

    # ------------------------ vẽ ------------------------
    def draw(self, screen):
        # Viền ngoài (rect full màn hình)
        outer = pygame.Rect(
            0, 0,
            CELL_WIDTH  * CELL_SIZE,
            CELL_HEIGHT * CELL_SIZE
        )
        # width = WALL_THICKNESS ➜ chỉ nét viền mảnh
        pygame.draw.rect(screen, WALL_COLOR, outer, WALL_THICKNESS)

    # ------------------------ va chạm -------------------
    def is_collision(self, pos):
        return pos in self.blocks
