import pygame
TILE = 40

def load_map(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Red Square")
clock = pygame.time.Clock()
game_map = load_map("maps/level1.txt")
running = True
x = 300
y = 220
for row, line in enumerate(game_map):
    for col, char in enumerate(line):
        if char == "S":
            x = col * TILE
            y = row * TILE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                col = x // TILE
                row = y // TILE
                if game_map[row][col - 1] != "#":
                    x = x - TILE
            if event.key == pygame.K_RIGHT:
                col = x // TILE
                row = y // TILE
                if game_map[row][col + 1] != "#":
                    x = x + TILE
            if event.key == pygame.K_UP:
                col = x // TILE
                row = y // TILE
                if game_map[row - 1][col] != "#":
                    y = y - TILE
            if event.key == pygame.K_DOWN:
                col = x // TILE
                row = y // TILE
                if game_map[row + 1][col] != "#":
                    y = y + TILE

    screen.fill((0, 0, 0))
    for row, line in enumerate(game_map):
        for col, char in enumerate(line):
            if char == "#":
                pygame.draw.rect(screen, (100, 100, 100), (col * TILE, row * TILE, TILE, TILE))
            if char == "E":
                pygame.draw.rect(screen, (0, 200, 0), (col * TILE, row * TILE, TILE, TILE))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 40))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

