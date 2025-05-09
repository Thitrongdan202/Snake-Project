import pygame, sys
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR,
    FPS, POINTS_TO_GROW
)
from snake import Snake
from food  import Food
from walls import Walls

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake – Walls & Grow")
    clock = pygame.time.Clock()

    snake, walls, food = Snake(), Walls(), Food()
    food.random_position(forbidden=set(map(tuple, walls.blocks + snake.body)))

    score = 0
    font  = pygame.font.SysFont('Arial', 24)
    running = True

    while running:
        clock.tick(FPS)

        # ── INPUT ───────────────────────────────────────────
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_w, pygame.K_UP)    and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif e.key in (pygame.K_s, pygame.K_DOWN)  and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif e.key in (pygame.K_a, pygame.K_LEFT)  and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif e.key in (pygame.K_d, pygame.K_RIGHT) and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
        # ────────────────────────────────────────────────────

        grow = False
        if snake.body[0] == food.position:         # ăn mồi
            score += 1
            grow = (score % POINTS_TO_GROW == 0)
            food.random_position(
                forbidden=set(map(tuple, walls.blocks + snake.body))
            )

        snake.move(grow=grow)

        if walls.is_collision(snake.body[0]):      # đâm tường
            print("Game Over – hit wall!")
            running = False

        # ── VẼ FRAME ───────────────────────────────────────
        screen.fill(BG_COLOR)
        walls.draw(screen)
        snake.draw(screen)
        food.draw(screen)

        txt = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(midtop=(SCREEN_WIDTH // 2, 10)))

        pygame.display.flip()
        # ────────────────────────────────────────────────────

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
