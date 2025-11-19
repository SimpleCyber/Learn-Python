import pygame
import sys
import random
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
MAZE_WIDTH = SCREEN_WIDTH // CELL_SIZE
MAZE_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
TREASURE_COLOR = (255, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
PATH_COLOR = (128, 128, 128)  # Color for path
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Explorer")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (CELL_SIZE // 2, CELL_SIZE // 2)

    def move(self, dx, dy):
        new_x = self.rect.x + dx * CELL_SIZE
        new_y = self.rect.y + dy * CELL_SIZE
        if (0 <= new_x < SCREEN_WIDTH) and (0 <= new_y < SCREEN_HEIGHT) and maze[new_y // CELL_SIZE][new_x // CELL_SIZE] != 1:
            self.rect.x = new_x
            self.rect.y = new_y

# Class for the treasure
class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(TREASURE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, MAZE_WIDTH - 1) * CELL_SIZE, random.randint(0, MAZE_HEIGHT - 1) * CELL_SIZE)

# Function to generate random maze
def generate_maze():
    maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    for _ in range(100):  # Add random obstacles
        x = random.randint(0, MAZE_WIDTH - 1)
        y = random.randint(0, MAZE_HEIGHT - 1)
        maze[y][x] = 1
    return maze

# Function to draw maze
def draw_maze(maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, OBSTACLE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, PATH_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to display text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Main function
def main():
    global maze
    maze = generate_maze()
    player = Player()
    treasure = Treasure()
    start_time = time.time()
    steps = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(0, -1)
                    steps += 1
                elif event.key == pygame.K_DOWN:
                    player.move(0, 1)
                    steps += 1
                elif event.key == pygame.K_LEFT:
                    player.move(-1, 0)
                    steps += 1
                elif event.key == pygame.K_RIGHT:
                    player.move(1, 0)
                    steps += 1

        # Check collision with treasure
        if pygame.sprite.collide_rect(player, treasure):
            treasure.rect.topleft = (random.randint(0, MAZE_WIDTH - 1) * CELL_SIZE, random.randint(0, MAZE_HEIGHT - 1) * CELL_SIZE)
            elapsed_time = time.time() - start_time
            draw_text("Congratulations! You found the treasure!", 36, WHITE, 10, 10)
            draw_text("Time taken: {:.2f} seconds".format(elapsed_time), 24, WHITE, 10, 50)
            draw_text("Steps taken: {}".format(steps), 24, WHITE, 10, 90)
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.quit()
            sys.exit()

        # Draw
        screen.fill(BLACK)
        draw_maze(maze)
        screen.blit(player.image, player.rect)
        screen.blit(treasure.image, treasure.rect)
        draw_text("Find the Treasure!", 36, WHITE, 10, 10)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
