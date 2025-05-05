import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, FPS
from snake import Snake
from food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    score = 0  # Khởi tạo điểm số ban đầu
    font = pygame.font.SysFont('Arial', 24)  # Font để hiển thị điểm số


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
            score += 1  # Cộng thêm điểm mỗi lần ăn mồi

        # Luôn di chuyển rắn
        snake.move()

        # Vẽ màn hình
        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        # Vẽ điểm số
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Trắng
        screen.blit(score_text, (10, 10))  # Hiển thị góc trên bên trái


        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
