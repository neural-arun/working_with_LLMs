import pygame
import random

# Define screen dimensions
screen_width = 800
screen_height = 600

# --- Player Car Class (No changes) ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 80])
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# --- Enemy Car Class (Updated) ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 80])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, screen_width - 20), random.randint(-100, -40))
        self.speed = random.randint(4, 8)

    def update(self):
        self.rect.y += self.speed
        # --- Change for More Enemies ---
        # If the enemy goes off the bottom of the screen, remove it
        if self.rect.top > screen_height:
            self.kill() # self.kill() removes the sprite from all groups

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Car Game")
clock = pygame.time.Clock()

# --- Road Lines Setup (No changes) ---
road_lines = []
line_height = 40
line_gap = 20
line_y_start = 0
for i in range(screen_height // (line_height + line_gap) + 2):
    line = pygame.Rect(screen_width / 2 - 5, line_y_start, 10, line_height)
    road_lines.append(line)
    line_y_start += line_height + line_gap
road_speed = 8


# --- Create Sprites and Sprite Groups (Updated for More Enemies) ---
player = Player()

# Create a group for all sprites (for updating and drawing)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create a separate group just for enemies (for future collision checks)
enemies = pygame.sprite.Group()

# --- Setup for Spawning Enemies ---
# Create a custom event for adding a new enemy
ADD_ENEMY = pygame.USEREVENT + 1
# Set a timer to trigger this event every 1000 milliseconds (1 second)
# You can change 1000 to 500 for more enemies, or 2000 for fewer.
pygame.time.set_timer(ADD_ENEMY, 100)


# --- Main Game Loop ---
running = True
while running:
    clock.tick(60)

    # --- Event Handling (Updated for More Enemies) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Check if the ADD_ENEMY event has been triggered by our timer
        elif event.type == ADD_ENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Update all sprites
    all_sprites.update()

    # Move and Reset Road Lines
    for line in road_lines:
        line.y += road_speed
        if line.top > screen_height:
            line.y = -line_height

    # --- Drawing ---
    screen.fill((105, 105, 105))
    for line in road_lines:
        pygame.draw.rect(screen, (255, 255, 0), line)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()