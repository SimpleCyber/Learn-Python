import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
ROWS = SCREEN_HEIGHT // CELL_SIZE
COLS = SCREEN_WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Explorer")

# Function to create a random maze using depth-first search algorithm
def create_maze():
    maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    stack = [(0, 0)]
    visited = set()
    while stack:
        cell = stack[-1]
        maze[cell[1]][cell[0]] = 1
        visited.add(cell)
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cell[0] + dx, cell[1] + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:
                neighbors.append((nx, ny))
        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()
    maze[0][0] = 2  # Start point
    maze[ROWS - 1][COLS - 1] = 3  # End point
    return maze

# Function to draw the maze
def draw_maze(maze):
    for y in range(ROWS):
        for x in range(COLS):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[y][x] == 2:
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[y][x] == 3:
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main function
def main():
    maze = create_maze()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw
        screen.fill(BLACK)
        draw_maze(maze)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
