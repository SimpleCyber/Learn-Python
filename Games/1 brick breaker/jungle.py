import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = 50
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
COIN_SIZE = 30
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jungle Runner")

# Clock
clock = pygame.time.Clock()

# Load images
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(GREEN)  # Green rectangle for the player
coin_img = pygame.Surface((COIN_SIZE, COIN_SIZE))
coin_img.fill((255, 255, 0))  # Yellow coin
obstacle_img = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle_img.fill((255, 0, 0))  # Red obstacle

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
        self.speed_y = 0

    def update(self):
        self.speed_y += 1  # Gravity
        self.rect.y += self.speed_y
        if self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.speed_y = 0

    def jump(self):
        if self.rect.bottom == SCREEN_HEIGHT - GROUND_HEIGHT:
            self.speed_y = -15  # Jump strength

# Class for coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)  # Random spawn position
        self.rect.y = random.randint(50, SCREEN_HEIGHT - GROUND_HEIGHT - 50)  # Random vertical position

    def update(self):
        self.rect.x -= 5  # Move towards the left
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
            self.rect.y = random.randint(50, SCREEN_HEIGHT - GROUND_HEIGHT - 50)

# Class for obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)  # Random spawn position
        self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT  # Fixed vertical position

    def update(self):
        self.rect.x -= 5  # Move towards the left
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
            self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT

# Function to display text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main function
def main():
    all_sprites = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(8):  # Initial coins
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    for _ in range(5):  # Initial obstacles
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Update
        all_sprites.update()

        # Check collisions between player and coins
        coin_collisions = pygame.sprite.spritecollide(player, coins, True)
        for coin in coin_collisions:
            score += 1

        # Check collisions between player and obstacles
        if pygame.sprite.spritecollide(player, obstacles, False):
            # Game over condition
            draw_text("Game Over!", 64, WHITE, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50)
            draw_text("Score: " + str(score), 36, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text("Score: " + str(score), 24, WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
