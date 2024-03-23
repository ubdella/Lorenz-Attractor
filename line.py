import pygame
from pygame.locals import *
import sys
import numpy as np

# attractor parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
dt = 0.01

# Init
x, y, z = 0.1, 2.0, 0.4


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lorenz Attractor")
clock = pygame.time.Clock()


background_color = (0, 0, 0)
line_color = (200, 0, 200)

# centering
x_offset, y_offset = width // 2, height // 2  # Center of the screen
scale = 10  

points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # attractor equations
    dx = sigma * (y - x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt

    x += dx
    y += dy
    z += dz


    screen_x = int(x * scale) + x_offset
    screen_y = int(y * scale) + y_offset
    points.append((screen_x, screen_y))

    # to keep it from getting too large
    if len(points) > 10000:
        points.pop(0)


    screen.fill(background_color)

    # Draw
    for i in range(len(points) - 1):
        pygame.draw.line(screen, line_color, points[i], points[i + 1], 2)

    pygame.display.flip()
    clock.tick(500)
