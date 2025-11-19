import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_SIZE = 50
PLAYER_SPEED = 8

# Enemy settings
ENEMY_SIZE = 30
ENEMY_SPEED = 3  # Reduced speed
ENEMY_SPAWN_INTERVAL = 60

# Bullet settings
BULLET_SIZE = 5
BULLET_SPEED = 10
MAX_BULLETS = 3  # Maximum bullets shot at a time

# Block settings
BLOCK_SIZE = 30
BLOCK_COLORS = [BLUE, RED, GREEN]
BLOCK_HP = 2  # Number of hits required to destroy a block

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Shooter Game")

# Load player image
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.rect(player_image, GREEN, (0, 0, PLAYER_SIZE, PLAYER_SIZE))
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT - PLAYER_SIZE))

# Lists to store enemies, bullets, and blocks
enemies = []
bullets = []
blocks = []

# Initialize Pygame clock
clock = pygame.time.Clock()

# Game loop
running = True
score = 0

# Function to draw text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to create a block
def create_block():
    block_rect = pygame.Rect(random.randint(0, WIDTH - BLOCK_SIZE), 0, BLOCK_SIZE, BLOCK_SIZE)
    block_color = random.choice(BLOCK_COLORS)
    block_hp = BLOCK_HP
    return {'rect': block_rect, 'color': block_color, 'hp': block_hp}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Player controls
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED

    # Shooting bullets
    if keys[pygame.K_SPACE] and len(bullets) < MAX_BULLETS:
        bullets.append(pygame.Rect(player_rect.centerx - BULLET_SIZE // 2, player_rect.y, BULLET_SIZE, BULLET_SIZE))

    # Enemy spawn
    if random.randint(0, ENEMY_SPAWN_INTERVAL) == 0:
        blocks.append(create_block())

    # Update bullets
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    for bullet in bullets:
        bullet.y -= BULLET_SPEED

    # Update enemies (blocks)
    for block in blocks:
        block['rect'].y += ENEMY_SPEED

    # Check collisions with bullets and blocks
    for bullet in bullets:
        for block in blocks:
            if bullet.colliderect(block['rect']):
                bullets.remove(bullet)
                block['hp'] -= 1
                if block['hp'] == 0:
                    score += 1
                    blocks.remove(block)

    # Check player-enemy collisions
    if any(player_rect.colliderect(block['rect']) for block in blocks):
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, player_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])

    # Display score
    draw_text(f"Score: {score}", 36, GREEN, 10, 10)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
screen.fill(WHITE)
draw_text("Game Over", 60, RED, WIDTH // 2 - 150, HEIGHT // 2 - 30)
draw_text(f"Your Score: {score}", 36, GREEN, WIDTH // 2 - 120, HEIGHT // 2 + 20)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.delay(3000)

# Quit Pygame
pygame.quit()
 