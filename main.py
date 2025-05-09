import pygame, sys
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR,
    FPS, POINTS_TO_GROW
)
from snake import Snake
from food  import Food
from walls import Walls


# ─────────────────────────────────────────────
def show_game_over(screen, score):
    """Vẽ thông báo GAME OVER. Font Tahoma hỗ trợ Unicode tiếng Việt."""
    big   = pygame.font.SysFont("Tahoma", 48,  bold=True)
    mid   = pygame.font.SysFont("Tahoma", 36,  bold=True)
    small = pygame.font.SysFont("Tahoma", 24)
# tạo chữ chơi lại - kết thúc
    lines = [
        (big,   "TRÒ CHƠI KẾT THÚC",                (255,  50,  50)),
        (mid,   "GAME  OVER",                       (255, 255, 255)),
        (small, f"Điểm: {score}",                   (255, 255, 255)),
        (small, "Nhấn R để chơi lại – ESC để thoát", (200, 200, 200)),
    ]

    screen.fill(BG_COLOR)
    y = SCREEN_HEIGHT // 3
    for font, text, color in lines:
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(SCREEN_WIDTH // 2, y))
        screen.blit(surf, rect)
        y += surf.get_height() + 12

    pygame.display.flip()
# ─────────────────────────────────────────────

#main
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rắn ăn mồi")
    clock = pygame.time.Clock()

    snake, walls, food = Snake(), Walls(), Food()
    food.random_position(forbidden=set(map(tuple, walls.blocks + snake.body)))

    score   = 0
    font    = pygame.font.SysFont("Tahoma", 24)
    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        # ─── XỬ LÝ SỰ KIỆN ────────────────────────
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if not game_over:
                    if e.key in (pygame.K_w, pygame.K_UP)    and snake.direction != "DOWN":
                        snake.direction = "UP"
                    elif e.key in (pygame.K_s, pygame.K_DOWN)  and snake.direction != "UP":
                        snake.direction = "DOWN"
                    elif e.key in (pygame.K_a, pygame.K_LEFT)  and snake.direction != "RIGHT":
                        snake.direction = "LEFT"
                    elif e.key in (pygame.K_d, pygame.K_RIGHT) and snake.direction != "LEFT":
                        snake.direction = "RIGHT"
                else:      # Đang ở màn GAME OVER
                    if e.key == pygame.K_r:  # Restart
                        snake, walls = Snake(), Walls()
                        food.random_position(forbidden=set(map(tuple, walls.blocks)))
                        score, game_over = 0, False
                    elif e.key == pygame.K_ESCAPE:
                        running = False
        # ───────────────────────────────────────────

        if game_over:
            show_game_over(screen, score)
            continue

        # Ăn mồi
        grow = False
        if snake.body[0] == food.position:
            score += 1
            grow = (score % POINTS_TO_GROW == 0)
            forbidden = set(map(tuple, walls.blocks + snake.body))
            food.random_position(forbidden=forbidden)

        snake.move(grow=grow)

        # Đâm tường => Game Over
        if walls.is_collision(snake.body[0]):
            game_over = True
            continue

        # ─── VẼ FRAME ─────────────────────────────
        screen.fill(BG_COLOR)
        walls.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, score_surf.get_rect(midtop=(SCREEN_WIDTH // 2, 10))) # cho điểm ra giữa

        pygame.display.flip()
        # ───────────────────────────────────────────

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
