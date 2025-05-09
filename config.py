# ───── KÍCH THƯỚC LƯỚI & CỬA SỔ ─────
CELL_SIZE   = 20
CELL_WIDTH  = 30
CELL_HEIGHT = 20

SCREEN_WIDTH  = CELL_WIDTH  * CELL_SIZE
SCREEN_HEIGHT = CELL_HEIGHT * CELL_SIZE

# ───── MÀU SẮC ─────
GREEN = (0, 255, 0)        # rắn
RED   = (255, 0, 0)        # mồi
BG_COLOR   = (30, 30, 30)  # nền
WALL_COLOR = (0, 255, 255) # viền (cyan)

# ───── CẤU HÌNH GAME ─────
FPS            = 10         # tốc độ khung hình
POINTS_TO_GROW = 3         # đủ 3 điểm rắn dài 1 đoạn
WALL_THICKNESS = 6         # độ dày nét viền (px)
