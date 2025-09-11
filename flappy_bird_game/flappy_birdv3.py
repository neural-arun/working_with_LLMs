import pygame
import random
import numpy as np

def create_pipe(screen_width, screen_height, pipe_gap):
    """
    Creates a pair of top and bottom pipe rectangles with a random gap position.
    Returns a tuple containing the bottom and top pipe Rects.
    """
    pipe_height = random.randint(150, screen_height - 150)
    bottom_pipe = pygame.Rect(screen_width, pipe_height + pipe_gap // 2, 80, screen_height - (pipe_height + pipe_gap // 2))
    top_pipe = pygame.Rect(screen_width, 0, 80, pipe_height - pipe_gap // 2)
    return bottom_pipe, top_pipe

def move_pipes(pipes, pipe_speed):
    """
    Moves a list of pipes to the left and removes pipes that are off-screen.
    Returns a new list of visible pipes.
    """
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return visible_pipes

def draw_pipes(screen, pipes, pipe_color):
    """Draws all pipes in the list to the screen."""
    for pipe in pipes:
        pygame.draw.rect(screen, pipe_color, pipe)

def draw_score(screen, score, font, screen_width):
    """Renders and draws the score in the top-center of the screen."""
    score_surface = font.render(str(score), True, (255, 255, 255)) # White text
    score_rect = score_surface.get_rect(center=(screen_width // 2, 50))
    screen.blit(score_surface, score_rect)

def draw_message(screen, text, font, screen_width, screen_height):
    """Renders and draws a message in the center of the screen."""
    message_surface = font.render(text, True, (255, 255, 255))
    message_rect = message_surface.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(message_surface, message_rect)


def generate_sound(frequency=440, duration=0.1, volume=0.5):
    """
    Generates a sine wave and returns it as a Pygame Sound object.
    """
    sample_rate = 44100
    n_samples = int(duration * sample_rate)
    amplitude = volume * (2**15 - 1)
    
    t = np.linspace(0., duration, n_samples, endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    
    # Convert to 16-bit signed integers
    mono_sound = (wave * amplitude).astype(np.int16)
    
    # Create a C-contiguous stereo array to avoid the ValueError.
    # We do this by creating a 2-column array and filling it.
    sound_arr = np.zeros((n_samples, 2), dtype=np.int16)
    sound_arr[:, 0] = mono_sound
    sound_arr[:, 1] = mono_sound
    
    return pygame.sndarray.make_sound(sound_arr)


def check_collision(pipes, bird, screen_height):
    """
    Checks for collisions between the bird and pipes or screen boundaries.
    Returns True if a collision occurs, otherwise False.
    """
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True

    if bird.top <= 0 or bird.bottom >= screen_height:
        return True

    return False

def main():
    """
    Main function to initialize Pygame, create the game window,
    and run the main game loop.
    """
    # Initialize all imported Pygame modules
    pygame.init()
    # Initialize mixer for stereo sound
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512) 

    # Define screen dimensions and colors
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PURPLE = (138, 43, 226)  # New background color
    CYAN = (0, 255, 255) # New pipe color

    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')

    # --- Clock for controlling frame rate ---
    clock = pygame.time.Clock()

    # --- Sound Effects ---
    # Note: Requires numpy package to be installed (pip install numpy)
    jump_sound = generate_sound(frequency=660, duration=0.05, volume=0.3)
    score_sound = generate_sound(frequency=880, duration=0.1, volume=0.4)
    game_over_sound = generate_sound(frequency=220, duration=0.2, volume=0.5)

    # --- Bird Setup ---
    BIRD_COLOR = (255, 165, 0)  # Orange for the bird
    bird_rect = pygame.Rect(100, 300, 40, 30) # Collision rectangle remains the same size

    # --- Game State ---
    game_state = 'start'

    # --- Physics ---
    bird_velocity = 0
    gravity = 0.1  # Slower gravity

    # --- Score & Font ---
    score = 0
    passed_pipes = []
    score_font = pygame.font.Font(None, 74) # Default font, size 74
    message_font = pygame.font.Font(None, 50)

    # --- Pipe Setup ---
    pipe_list = []
    PIPE_GAP = 200
    INITIAL_PIPE_SPEED = 2 # Slower pipes
    MAX_PIPE_SPEED = 5 # Set a maximum speed for the pipes
    current_pipe_speed = INITIAL_PIPE_SPEED
    speed_milestones = set()
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1600) # Trigger SPAWNPIPE event every 1.6 seconds

    # --- Main Game Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == 'playing':
                        bird_velocity = -3 # Softer jump
                        jump_sound.play()
                    elif game_state == 'start':
                        game_state = 'playing'
                    elif game_state == 'game_over':
                        # Reset the game
                        game_state = 'playing'
                        pipe_list.clear()
                        passed_pipes.clear()
                        bird_rect.center = (100, 300)
                        bird_velocity = 0
                        score = 0
                        current_pipe_speed = INITIAL_PIPE_SPEED
                        speed_milestones.clear()
            
            if game_state == 'playing':
                if event.type == SPAWNPIPE:
                    pipe_list.extend(create_pipe(SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP))

        # --- Game Logic & Drawing by State ---
        screen.fill(PURPLE)

        if game_state == 'start':
            draw_message(screen, "Press Space to Play", message_font, SCREEN_WIDTH, SCREEN_HEIGHT)

        elif game_state == 'playing':
            # --- Game Logic ---
            bird_velocity += gravity
            bird_rect.y += int(bird_velocity)
            pipe_list = move_pipes(pipe_list, current_pipe_speed)

            # Score Logic
            for i in range(0, len(pipe_list), 2):
                pipe = pipe_list[i]
                if pipe.centerx < bird_rect.centerx and pipe not in passed_pipes:
                    score += 1
                    passed_pipes.append(pipe)
                    score_sound.play()
            passed_pipes = [p for p in passed_pipes if p.right > 0]

            # Increase speed based on score, up to a maximum limit
            if score > 0 and score % 10 == 0 and score not in speed_milestones and current_pipe_speed < MAX_PIPE_SPEED:
                current_pipe_speed = min(current_pipe_speed + 0.25, MAX_PIPE_SPEED)
                speed_milestones.add(score)


            # --- Drawing ---
            draw_pipes(screen, pipe_list, CYAN) # Use new pipe color
            
            # Draw a more realistic bird shape
            # The collision box (bird_rect) is invisible but still used for physics
            bird_points = [
                (bird_rect.left, bird_rect.top + 15),          # Tail
                (bird_rect.left + 15, bird_rect.top),         # Top-back
                (bird_rect.right - 5, bird_rect.top + 10),      # Head
                (bird_rect.right, bird_rect.top + 15),          # Beak
                (bird_rect.right - 5, bird_rect.top + 20),      # Chin
                (bird_rect.left + 15, bird_rect.bottom)     # Bottom
            ]
            pygame.draw.polygon(screen, BIRD_COLOR, bird_points)
            
            draw_score(screen, score, score_font, SCREEN_WIDTH)
            
            # --- Collision Detection ---
            if check_collision(pipe_list, bird_rect, SCREEN_HEIGHT):
                game_over_sound.play()
                game_state = 'game_over'
        
        elif game_state == 'game_over':
            draw_message(screen, f"Final Score: {score}", message_font, SCREEN_WIDTH, SCREEN_HEIGHT - 50)
            draw_message(screen, "Press Space to Restart", message_font, SCREEN_WIDTH, SCREEN_HEIGHT + 50)

        # --- Update the Display ---
        pygame.display.flip()

        # --- Cap the frame rate ---
        clock.tick(60)

    # --- Exiting ---
    # Uninitialize Pygame modules and quit the program
    pygame.quit()

if __name__ == '__main__':
    main()
















