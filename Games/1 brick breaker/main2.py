import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
ROWS = SCREEN_HEIGHT // GRID_SIZE
COLS = SCREEN_WIDTH // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Painter")

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

# Function to draw the canvas
def draw_canvas(canvas):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, canvas[row][col], (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main function
def main():
    canvas = [[WHITE for _ in range(COLS)] for _ in range(ROWS)]
    drawing = False
    color_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color_index = (color_index + 1) % len(COLORS)

        if drawing:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // GRID_SIZE
            row = mouse_y // GRID_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                canvas[row][col] = COLORS[color_index]

        screen.fill(WHITE)
        draw_grid()
        draw_canvas(canvas)
        pygame.display.flip()

if __name__ == "__main__":
    main()
