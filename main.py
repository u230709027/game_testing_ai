import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Red Square")
clock = pygame.time.Clock()

running = True
x = 300
y = 220
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 40
            if event.key == pygame.K_RIGHT:
                x = x + 40
            if event.key == pygame.K_UP:
                y = y - 40
            if event.key == pygame.K_DOWN:
                y = y + 40

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 40))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

