import pygame
import random
import math
import sys
import time


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
numbers_list = []
randomized_list = []
list_size = 200
color = (255, 255, 255)
w_constant = WINDOW_WIDTH / list_size

pygame.init()
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("visualize sort")


def make_rgb_list():
    rgb_list = []
    for i in range(256):
        rgb_list.append((255, 255, 255 - i))  # white to yellow
    for i in range(256):
        rgb_list.append((255, 255 - i, 0))  # yellow to red
    for i in range(256):
        rgb_list.append((255 - i, i, 0))  # red to green
    for i in range(256):
        rgb_list.append((0, 255, i))  # green to light blue
    for i in range(256):
        rgb_list.append((0, 255 - i, 255))  # light blue to blue
    for i in range(256):
        rgb_list.append((i, 0, 255))  # from blue to pink
    for i in range(256):
        rgb_list.append((255, i, 255))  # from pink to white
    return rgb_list


for i in range(list_size):
    numbers_list.append(i)

for i in range(list_size):
    my_index = random.randint(0, len(numbers_list) - 1)
    randomized_list.append(numbers_list[my_index])
    numbers_list.pop(my_index)


stop = False
new_rgb_list = make_rgb_list()
print(len(new_rgb_list))
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                stop = True
            if event.key == pygame.K_SPACE:
                screen.fill((0, 0, 0))
                for z in range(len(randomized_list)):
                    w = w_constant
                    h = randomized_list[z] * (WINDOW_HEIGHT / list_size)
                    x = z * (WINDOW_WIDTH / list_size)
                    y = WINDOW_HEIGHT - h
                    color = new_rgb_list[randomized_list[z]]
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
                    pygame.display.flip()
                for i in range(list_size - 1):
                    # range(n) also work but outer loop will repeat one time more than needed.

                    # Last i elements are already in place
                    for j in range(0, list_size - i - 1):

                        # traverse the array from 0 to n-i-1
                        # Swap if the element found is greater
                        # than the next element
                        if randomized_list[j] > randomized_list[j + 1]:
                            randomized_list[j], randomized_list[j + 1] = randomized_list[j + 1], randomized_list[j]
                        w = w_constant
                        # min_idx = j
                        # i = (j+1)
                        """h = randomized_list[j] * (WINDOW_HEIGHT / list_size)
                        x = (j+1) * (WINDOW_WIDTH / list_size)
                        y = WINDOW_HEIGHT - h

                        h1 = randomized_list[(j+1)] * (WINDOW_HEIGHT / list_size)
                        x1 = j * (WINDOW_WIDTH / list_size)
                        y1 = WINDOW_HEIGHT - h
                        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, w, h))
                        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, w, h))
                        pygame.display.flip()"""

                        h = randomized_list[(j+1)] * (WINDOW_HEIGHT / list_size)
                        x = (j+1) * (WINDOW_WIDTH / list_size)
                        y = WINDOW_HEIGHT - h
                        color = new_rgb_list[randomized_list[i]]
                        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

                        h1 = randomized_list[j] * (WINDOW_HEIGHT / list_size)
                        x1 = j * (WINDOW_WIDTH / list_size)
                        y1 = WINDOW_HEIGHT - h
                        color = new_rgb_list[j]
                        pygame.draw.rect(screen, color, pygame.Rect(x1, y1, w, h1))
                        pygame.display.flip()
                    screen.fill((0, 0, 0))

pygame.quit()
