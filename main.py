import pygame
from game import Game
TILE = 40

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Red Square")
clock = pygame.time.Clock()
game = Game("maps/level1.txt")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move(0, -1)
            if event.key == pygame.K_RIGHT:
                game.move(0, 1)
            if event.key == pygame.K_UP:
                game.move(-1, 0)
            if event.key == pygame.K_DOWN:
                game.move(1, 0)

    screen.fill((0, 0, 0))
    for row, line in enumerate(game.map):
        for col, char in enumerate(line):
            if char == "#":
                pygame.draw.rect(screen, (100, 100, 100), (col * TILE, row * TILE, TILE, TILE))
            if char == "E":
                pygame.draw.rect(screen, (0, 200, 0), (col * TILE, row * TILE, TILE, TILE))
    pygame.draw.rect(screen, (255, 0, 0), (game.player_col * TILE, game.player_row * TILE, TILE, TILE))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

