import pygame
import math
from pygame import mixer
clock = pygame.time.Clock()
REFRESH_RATE = 60
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
LEFT = 1
SCROLL = 2
RIGHT = 3
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Oasis Casino")
quit = False
WHITE = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
    IMAGE = ('bodyguardd.png')
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    screen.blit(img, (1620, 0))
    pygame.display.flip()




    clock.tick(REFRESH_RATE)
