import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
PURPLE = (128, 0, 128)   # RGB value for purple


# Fonts
font = pygame.font.SysFont("arial", 25)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


def draw_snake(snake_list):
    """Draw snake segments"""
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], CELL_SIZE, CELL_SIZE])


def message(text, color, y_offset=0):
    """Display message in center"""
    msg = font.render(text, True, color)
    rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(msg, rect)


def game_loop():
    game_over = False
    game_close = False

    # Initial snake setup
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0
    snake_list = []
    snake_length = 1

    # Food
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    # Score & speed
    score = 0
    speed = 5
    paused = False

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -CELL_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = CELL_SIZE
                elif event.key == pygame.K_p:  # Pause/Resume
                    paused = not paused

        if paused:
            screen.fill(PURPLE)
            message("Game Paused. Press P to Resume", BLUE)
            pygame.display.update()
            continue

        # Move snake
        x += dx
        y += dy

        # Check wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(PURPLE)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        # Snake mechanics
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        # Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.update()

        # Check food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            snake_length += 1
            score += 1
            speed += 0.5  # Increase speed as score grows

        clock.tick(speed)

    pygame.quit()
    quit()


# Run the game
game_loop()
