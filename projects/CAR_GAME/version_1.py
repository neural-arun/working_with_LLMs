import pygame
import random

# --- Game Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Opposite Lane Drifter")
clock = pygame.time.Clock()

# --- Player Car Class ---
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# --- Opponent Car Class ---
class OpponentCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Position the car at the top of a random lane
        lanes = [SCREEN_WIDTH * 0.25, SCREEN_WIDTH * 0.5, SCREEN_WIDTH * 0.75]
        self.rect.centerx = random.choice(lanes)
        self.rect.bottom = 0
        
        self.speed = random.randint(3, 7) # Varying speeds

    def update(self):
        self.rect.y += self.speed
        # Remove cars that go off-screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# --- Main Game Loop ---
def game_loop():
    running = True
    all_sprites = pygame.sprite.Group()
    opponent_cars = pygame.sprite.Group()
    
    player_car = PlayerCar()
    all_sprites.add(player_car)

    score = 0
    font = pygame.font.Font(None, 36)
    
    # Spawn timer for opponent cars
    spawn_timer = 0
    spawn_interval = 100 # Adjust for traffic density
    
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        # --- Update Game State ---
        all_sprites.update()
        score += 1 # Increment score based on distance
        
        # Spawn new cars
        spawn_timer += 1
        if spawn_timer > spawn_interval:
            new_car = OpponentCar()
            all_sprites.add(new_car)
            opponent_cars.add(new_car)
            spawn_timer = 0
            
        # Collision detection
        if pygame.sprite.spritecollide(player_car, opponent_cars, False):
            running = False # End game on collision
            
        # --- Drawing ---
        screen.fill(GREEN) # Road background
        
        # Draw road lines
        for i in range(10):
            pygame.draw.rect(screen, WHITE, [SCREEN_WIDTH // 2 - 5, i * 60, 10, 30])
            pygame.draw.rect(screen, WHITE, [SCREEN_WIDTH // 4 - 5, i * 60, 10, 30])
            pygame.draw.rect(screen, WHITE, [SCREEN_WIDTH * 0.75 - 5, i * 60, 10, 30])
            
        all_sprites.draw(screen)
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # --- Update Display ---
        pygame.display.flip()
        clock.tick(60) # 60 FPS

    print("Game Over! Your final score is:", score)
    pygame.quit()

if __name__ == "__main__":
    game_loop()