import pygame as pg

pg.init()

GRID_WIDTH = 14
GRID_HEIGHT = 20

CELL_SIZE = 40

WINDOW_WIDTH, WINDOW_HEIGHT = CELL_SIZE * GRID_WIDTH, CELL_SIZE * GRID_HEIGHT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

FPS = 60

grid = []

for y in range(GRID_HEIGHT):
    line = [None] * GRID_WIDTH
    grid.append(line)

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.fill(BLACK)

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = grid[y][x]
            if color is None:
                continue

            cell_rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(window, color, cell_rect)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
