import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS
from snake import Snake
from food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game - Phôi ăn mồi")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    running = True
    while running:
        clock.tick(FPS)

        # Bắt phím
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

        # Nếu đầu rắn chạm mồi → đổi vị trí mồi, không tăng độ dài
        if snake.body[0] == food.position:
            food.random_position()

        # Luôn di chuyển rắn
        snake.move()

        # Vẽ
        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
