import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE = 30
COIN_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 7
COIN_SPEED = 5
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Escape")

# Clock
clock = pygame.time.Clock()

# Load images
player_img = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_img.fill((255, 0, 0))  # Red pixel character
enemy_img = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
enemy_img.fill((0, 0, 255))  # Blue enemy
coin_img = pygame.Surface((COIN_SIZE, COIN_SIZE))
coin_img.fill((255, 255, 0))  # Yellow coin

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, self.rect.x))

# Class for the enemy
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

# Class for the coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - COIN_SIZE)
        self.rect.y = -COIN_SIZE

    def update(self):
        self.rect.y += COIN_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - COIN_SIZE)
            self.rect.y = -COIN_SIZE

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
    coins = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(5):  # 5 enemies initially
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    for _ in range(10):  # 10 coins initially
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update
        all_sprites.update()

        # Check collisions between player and enemies
        if pygame.sprite.spritecollide(player, enemies, False):
            # Game over condition
            draw_text("Game Over!", 64, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

        # Check collisions between player and coins
        coin_collisions = pygame.sprite.spritecollide(player, coins, True)
        for coin in coin_collisions:
            score += 1
            # Spawn new coin
            new_coin = Coin()
            all_sprites.add(new_coin)
            coins.add(new_coin)

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text("Score: " + str(score), 24, WHITE, 50, 50)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
