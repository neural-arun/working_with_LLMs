import pygame
import random

# Initialize pygame
pygame.init()

# Game window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
PURPLE = (128, 0, 128)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Fonts
font = pygame.font.SysFont("arial", 25)
game_over_font = pygame.font.SysFont("comicsansms", 40, bold=True)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


def draw_snake(snake_list, dx, dy):
    """Draw snake body and head with rotation"""
    # Draw body (all except head)
    for segment in snake_list[:-1]:
        pygame.draw.circle(
            screen,
            GREEN,
            (segment[0] + CELL_SIZE // 2, segment[1] + CELL_SIZE // 2),
            CELL_SIZE // 2
        )

    # Draw head (triangle pointing in movement direction)
    head_x, head_y = snake_list[-1]
    if dx > 0:  # moving right
        point1 = (head_x + CELL_SIZE, head_y + CELL_SIZE // 2)
        point2 = (head_x, head_y)
        point3 = (head_x, head_y + CELL_SIZE)
    elif dx < 0:  # moving left
        point1 = (head_x, head_y + CELL_SIZE // 2)
        point2 = (head_x + CELL_SIZE, head_y)
        point3 = (head_x + CELL_SIZE, head_y + CELL_SIZE)
    elif dy < 0:  # moving up
        point1 = (head_x + CELL_SIZE // 2, head_y)
        point2 = (head_x, head_y + CELL_SIZE)
        point3 = (head_x + CELL_SIZE, head_y + CELL_SIZE)
    else:  # moving down
        point1 = (head_x + CELL_SIZE // 2, head_y + CELL_SIZE)
        point2 = (head_x, head_y)
        point3 = (head_x + CELL_SIZE, head_y)

    pygame.draw.polygon(screen, GREEN, [point1, point2, point3])


def message(text, color, y_offset=0):
    """Display normal message in center"""
    msg = font.render(text, True, color)
    rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(msg, rect)


def game_over_message(text, color, y_offset=0):
    """Display game over message with bigger font"""
    msg = game_over_font.render(text, True, color)
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
    speed = 6
    paused = False

    while not game_over:

        while game_close:
            screen.fill(PURPLE)
            game_over_message("GAME OVER!", YELLOW, -40)  # headline
            message("Press C to Play Again or Q to Quit", WHITE, 20)  # smaller instruction
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

        # Draw food (circle)
        pygame.draw.circle(
            screen,
            YELLOW,
            (food_x + CELL_SIZE // 2, food_y + CELL_SIZE // 2),
            CELL_SIZE // 2
        )

        # Snake mechanics
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list, dx, dy)

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
            speed += 0.4  # Increase speed as score grows

        clock.tick(speed)

    pygame.quit()
    quit()


# Run the game
game_loop()