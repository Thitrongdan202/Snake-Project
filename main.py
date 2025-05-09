import pygame, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS, POINTS_TO_GROW
from snake  import Snake
from food   import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food  = Food()
    score = 0
    font  = pygame.font.SysFont('Arial', 24)

    running = True
    while running:
        clock.tick(FPS)

        # ── Bắt phím ──────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_s and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_a and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_d and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
        # ─────────────────────────────────────────────────

        grow = False  # mặc định không dài ra

        # Ăn mồi
        if snake.body[0] == food.position:
            food.random_position()
            score += 1

            # Đủ điểm để dài ra?
            if score % POINTS_TO_GROW == 0:
                grow = True

        # Di chuyển rắn (truyền cờ grow)
        snake.move(grow=grow)

        # ── Vẽ khung hình ────────────────────────────────
        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)

        # Hiển thị điểm
        score_text  = font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect  = score_text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
        screen.blit(score_text, score_rect)

        pygame.display.flip()
        # ────────────────────────────────────────────────

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
