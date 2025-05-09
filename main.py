# main.py
import pygame, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS
from snake import Snake
from food import Food
from walls import Walls

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game – tường viền")
    clock = pygame.time.Clock()

    snake = Snake()
    walls = Walls()
    food  = Food()
    food.random_position(forbidden=set(map(tuple, walls.blocks + snake.body)))

    score = 0
    font = pygame.font.SysFont("Arial", 24)

    running = True
    while running:
        clock.tick(FPS)

        # ── Bắt sự kiện ─────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP) and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key in (pygame.K_s, pygame.K_DOWN) and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key in (pygame.K_a, pygame.K_LEFT) and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key in (pygame.K_d, pygame.K_RIGHT) and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
        # ────────────────────────────────────────────────────────

        # Rắn ăn mồi
        if snake.body[0] == food.position:
            score += 1
            food.random_position(forbidden=set(map(tuple, walls.blocks + snake.body)))

        # Di chuyển
        snake.move()

        # Đâm tường → game over
        if walls.is_collision(snake.body[0]):
            print("Game Over – đâm tường!")
            running = False

        # ── Vẽ khung hình ──────────────────────────────────────
        screen.fill(BG_COLOR)
        walls.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(midtop=(SCREEN_WIDTH // 2, 11))
        screen.blit(score_text, score_rect)
        pygame.display.flip()
        # ────────────────────────────────────────────────────────

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
