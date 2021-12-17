# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing Color
color = (100, 100, 100)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(100, 50, 60, 100))
pygame.display.flip()
stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True