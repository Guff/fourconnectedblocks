import pygame as pg

pg.init()

pg.key.set_repeat(50)

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


DROP_DELAY_FRAMES = FPS

SQUARE_SHAPE = [
    [True, True],
    [True, True]
]

LINE_SHAPE = [
    [True, True, True, True]
]

L_SHAPE = [
    [False, False, True],
    [True, True, True]
]

REVERSE_L_SHAPE = [
    [True, False, False],
    [True, True, True]
]

T_SHAPE = [
    [True, True, True],
    [False, True, False]
]

S_SHAPE = [
    [False, True, True],
    [True, True, False]
]

Z_SHAPE = [
    [True, True, False],
    [False, True, True]
]

frame_count = 0

grid = []

for y in range(GRID_HEIGHT):
    line = []
    for x in range(GRID_WIDTH):
        line.append(None)

    grid.append(line)

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

current_block = [
    [True, True],
    [True, True]
]

current_block_color = RED

current_y, current_x = 0, (GRID_WIDTH // 2) - 1

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                current_x -= 1
            if event.key == pg.K_RIGHT:
                current_x += 1

    if frame_count == DROP_DELAY_FRAMES:
        frame_count = 0
        current_y += 1

    keys = pg.key.get_pressed()

    window.fill(BLACK)

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = grid[y][x]
            if color is None:
                continue

            cell_rect = pg.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(window, color, cell_rect)

    for y in range(len(current_block)):
        line = current_block[y]
        for x in range(len(line)):
            cell_rect = pg.Rect((current_x + x) * CELL_SIZE, (current_y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(window, current_block_color, cell_rect)

    frame_count += 1

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
