import pygame
import numpy as np
import time

# Initialisation de pygame
pygame.init()

# Dimensions de la grille
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la Vie - Conway")

# Grille initiale
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

def draw_grid():
    """Affiche la grille sur l'écran."""
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y, x] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def update_grid(grid):
    """Met à jour la grille selon les règles du jeu."""
    new_grid = grid.copy()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Calcul des voisins vivants
            neighbors = (
                grid[(y - 1) % GRID_HEIGHT, (x - 1) % GRID_WIDTH] +
                grid[(y - 1) % GRID_HEIGHT, x] +
                grid[(y - 1) % GRID_HEIGHT, (x + 1) % GRID_WIDTH] +
                grid[y, (x - 1) % GRID_WIDTH] +
                grid[y, (x + 1) % GRID_WIDTH] +
                grid[(y + 1) % GRID_HEIGHT, (x - 1) % GRID_WIDTH] +
                grid[(y + 1) % GRID_HEIGHT, x] +
                grid[(y + 1) % GRID_HEIGHT, (x + 1) % GRID_WIDTH]
            )
            
            # Règles du jeu
            if grid[y, x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y, x] = 0  # Meurt
            else:
                if neighbors == 3:
                    new_grid[y, x] = 1  # Naît
    return new_grid

# Boucle principale
running = True
pause = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        elif event.type == pygame.MOUSEBUTTONDOWN and pause:
            x, y = pygame.mouse.get_pos()
            grid[y // CELL_SIZE, x // CELL_SIZE] = 1 - grid[y // CELL_SIZE, x // CELL_SIZE]
    
    if not pause:
        grid = update_grid(grid)
    
    draw_grid()
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()

