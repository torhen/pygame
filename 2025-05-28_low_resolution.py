import pygame
pygame.init()

# Internal resolution
WIDTH, HEIGHT = 128, 128
# Upscale factor
SCALE = 5

# Internal surface (low resolution)
internal_surface = pygame.Surface((WIDTH, HEIGHT))

# Display surface (scaled up)
screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))

dx1 = 0
dx2 = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx1 = dx1 + 0.02
    dx2 = dx2 + 0.03
    r1 = 20
    r2 = 15
    if dx1 > WIDTH + r1:
        dx1 = -r1
    if dx2 > WIDTH + r2:
        dx2 = -r2
    # Draw to internal surface
    internal_surface.fill((0, 0, 0))
    pygame.draw.circle(internal_surface, (255, 0, 0), (dx1,40), 20)
    pygame.draw.circle(internal_surface, (0, 0, 255), (dx2,20), 15)

    # Scale the internal surface to screen
    scaled_surface = pygame.transform.scale(internal_surface, (WIDTH * SCALE, HEIGHT * SCALE))
    screen.blit(scaled_surface, (0, 0))

    pygame.display.update()

pygame.quit()
