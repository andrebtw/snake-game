import pygame
from pygame.locals import *

green_1 = (6, 150, 43)
green_2 = (25, 90, 44)

# INITIALISATION
pygame.init()  # Initialise Pygame lib
fps = 60  # Frames per second in Pygame

width = 600  # Width of the window
height = 600  # Height of the window

screen = pygame.display.set_mode((width, height), )


def update():
    pygame.display.update()


class Snake:
    pass


class AppleSpawn:
    pass

# Function to draw green squares all over the background
def background_green(pos, y):
    for i in range(1, 20, 1):
        if pos == 0:
            if i == 1:
                pygame.draw.rect(screen, green_2, (0, y * 30, 30, 30))
                pygame.draw.rect(screen, green_1, (0 + 30, y * 30, 30, 30))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_2, (x, y * 30, 30, 30))
                pygame.draw.rect(screen, green_1, (x + 30, y * 30, 30, 30))
            else:
                pass
        elif pos % 2:
            if i == 1:
                pygame.draw.rect(screen, green_1, (0, y * 30, 30, 30))
                pygame.draw.rect(screen, green_2, (0 + 30, y * 30, 30, 30))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_1, (x, y * 30, 30, 30))
                pygame.draw.rect(screen, green_2, (x + 30, y * 30, 30, 30))
            else:
                pass
        else:
            if i == 1:
                pygame.draw.rect(screen, green_2, (0, y * 30, 30, 30))
                pygame.draw.rect(screen, green_1, (0 + 30, y * 30, 30, 30))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_2, (x, y * 30, 30, 30))
                pygame.draw.rect(screen, green_1, (x + 30, y * 30, 30, 30))
            else:
                pass


def background():
    for i in range(20):
        background_green(i, i)


def game():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background()
        update()


def main():
    game()


if __name__ == "__main__":
    main()
