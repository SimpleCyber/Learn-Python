import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_SIZE = 64
ENEMY_SIZE = 64
BULLET_SIZE = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60
SHIP_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 7
ENEMY_SPAWN_RATE = 100  # Lower value spawns more enemies frequently

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galactic Invaders")

# Clock
clock = pygame.time.Clock()

# Load images
ship_img = pygame.image.load("spaceship.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()
bullet_img = pygame.Surface((BULLET_SIZE, BULLET_SIZE))
bullet_img.fill(WHITE)

# Resize images
ship_img = pygame.transform.scale(ship_img, (SHIP_SIZE, SHIP_SIZE))
enemy_img = pygame.transform.scale(enemy_img, (ENEMY_SIZE, ENEMY_SIZE))

# Font
font = pygame.font.Font(None, 36)

# Class for the player's ship
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Class for the enemy ships
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
        self.rect.y = -ENEMY_SIZE

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            self.rect.y = -ENEMY_SIZE

# Class for the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

# Function to display text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Main function
def main():
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    ship = Ship()
    all_sprites.add(ship)

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(ship.rect.centerx, ship.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Spawn enemies
        if random.randint(0, ENEMY_SPAWN_RATE) == 0:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Update
        all_sprites.update()

        # Check collisions between bullets and enemies
        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, enemies, True)
            for hit in hits:
                score += 1
                bullet.kill()

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text("Score: " + str(score), 24, WHITE, SCREEN_WIDTH // 2, 10)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
