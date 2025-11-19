import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRUIT_WIDTH = 50
FRUIT_HEIGHT = 50
BASKET_WIDTH = 100
BASKET_HEIGHT = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
FRUIT_SPEED = 5
INITIAL_LIVES = 3

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Catcher")

# Load images
basket_img = pygame.image.load("basket.png").convert_alpha()
apple_img = pygame.image.load("apple.png").convert_alpha()
orange_img = pygame.image.load("orange.png").convert_alpha()
banana_img = pygame.image.load("banana.png").convert_alpha()

# Resize images
basket_img = pygame.transform.scale(basket_img, (BASKET_WIDTH, BASKET_HEIGHT))
apple_img = pygame.transform.scale(apple_img, (FRUIT_WIDTH, FRUIT_HEIGHT))
orange_img = pygame.transform.scale(orange_img, (FRUIT_WIDTH, FRUIT_HEIGHT))
banana_img = pygame.transform.scale(banana_img, (FRUIT_WIDTH, FRUIT_HEIGHT))

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Function to create a new fruit
def create_fruit():
    fruits = [apple_img, orange_img, banana_img]
    fruit_img = random.choice(fruits)
    fruit_rect = fruit_img.get_rect()
    x = random.randint(0, SCREEN_WIDTH - fruit_rect.width)
    y = 0 - fruit_rect.height
    return {
        "image": fruit_img,
        "rect": fruit_rect.move(x, y),
        "speed": FRUIT_SPEED,
        "type": fruits.index(fruit_img)
    }

# Main function
def main():
    # Initialize game variables
    basket_rect = basket_img.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
    fruits = []
    score = 0
    lives = INITIAL_LIVES

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            basket_rect.x += 5

        # Keep the basket within the screen boundaries
        basket_rect.left = max(basket_rect.left, 0)
        basket_rect.right = min(basket_rect.right, SCREEN_WIDTH)

        # Add new fruit
        if random.random() < 0.02:
            fruits.append(create_fruit())

        # Move fruits and check for collisions
        for fruit in fruits[:]:
            fruit["rect"].y += fruit["speed"]
            if fruit["rect"].colliderect(basket_rect):
                fruits.remove(fruit)
                score += 1
            elif fruit["rect"].y >= SCREEN_HEIGHT:
                fruits.remove(fruit)
                lives -= 1

        # Draw
        screen.fill(BLACK)
        screen.blit(basket_img, basket_rect)
        for fruit in fruits:
            screen.blit(fruit["image"], fruit["rect"])

        # Display score and lives
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

        # Game over condition
        if lives <= 0:
            game_over_text = font.render("Game Over!", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            break

if __name__ == "__main__":
    main()
