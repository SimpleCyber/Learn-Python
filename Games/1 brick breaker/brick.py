import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BALL_RADIUS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BRICK_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(BLUE)
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

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Collision with walls
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1

# Brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Function to create bricks
def create_bricks():
    bricks = pygame.sprite.Group()
    for row in range(5):
        for col in range(10):
            brick = Brick(col * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2) + 50, random.choice(BRICK_COLORS))
            bricks.add(brick)
    return bricks

# Main function
def main():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle, ball, bricks)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.speed = -7
                elif event.key == pygame.K_RIGHT:
                    paddle.speed = 7
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and paddle.speed < 0:
                    paddle.speed = 0
                elif event.key == pygame.K_RIGHT and paddle.speed > 0:
                    paddle.speed = 0

        # Update
        all_sprites.update()

        # Ball and paddle collision
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y *= -1

        # Ball and brick collision
        brick_collisions = pygame.sprite.spritecollide(ball, bricks, True)
        if brick_collisions:
            ball.speed_y *= -1

        # Game over condition
        if ball.rect.bottom > SCREEN_HEIGHT:
            running = False

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
