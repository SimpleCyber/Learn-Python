import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
OBSTACLE_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Color Clash")

# Clock
clock = pygame.time.Clock()

# Load images
ball_img = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
pygame.draw.circle(ball_img, (0, 255, 0), (BALL_SIZE // 2, BALL_SIZE // 2), BALL_SIZE // 2)
obstacle_img = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE), pygame.SRCALPHA)
pygame.draw.rect(obstacle_img, (255, 0, 0), (0, 0, OBSTACLE_SIZE, OBSTACLE_SIZE))

# Class for the player's ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.color = (0, 255, 0)  # Initial color is green

    def update(self, obstacles):
        # Move the ball
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Check collision with obstacles
        obstacle_collisions = pygame.sprite.spritecollide(self, obstacles, False)
        for obstacle in obstacle_collisions:
            # Change ball's color if it collides with an obstacle of a different color
            if obstacle.color != self.color:
                self.color = obstacle.color

# Class for the obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color

# Function to generate random obstacles
def generate_obstacles():
    obstacles = pygame.sprite.Group()
    for _ in range(20):
        x = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - OBSTACLE_SIZE)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        obstacles.add(Obstacle(x, y, color))
    return obstacles

# Main function
def main():
    all_sprites = pygame.sprite.Group()
    obstacles = generate_obstacles()

    ball = Ball()
    all_sprites.add(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update
        ball.update(obstacles)

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
