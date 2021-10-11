import pygame
from pygame.locals import *

# Colors
green_1 = (6, 150, 43)
green_2 = (25, 90, 44)
black = (0, 0, 0)
white = (255, 255, 255)
blue_1 = (10, 20, 180)

# INITIALISATION
pygame.init()  # Initialise Pygame lib
fps = 60  # Frames per second in Pygame

width = 600  # Width of the window
height = 600  # Height of the window

square = 30  # Size of each squares in pixels

screen = pygame.display.set_mode((width, height), )


def update():
    pygame.display.update()


class Snake:
    def __init__(self):
        self.speed = -1
        self.color = blue_1

    def start(self):
        x = 300
        y = 300

        dy = self.speed - 1

        dx = 0
        pygame.draw.rect(screen, self.color, (x, dy, square, square)) #draw snake

    def die(self):
        pass

    def eat(self):
        pass


class AppleSpawn:
    def __init__(self):
        pass


# Function to draw green squares all over the background
def background_green(pos, y):
    for i in range(1, 20, 1):
        if pos == 0:
            if i == 1:
                pygame.draw.rect(screen, green_2, (0, y * square, square, square))
                pygame.draw.rect(screen, green_1, (0 + square, y * square, square, square))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_2, (x, y * square, square, square))
                pygame.draw.rect(screen, green_1, (x + square, y * square, square, square))
            else:
                pass
        elif pos % 2:
            if i == 1:
                pygame.draw.rect(screen, green_1, (0, y * square, square, square))
                pygame.draw.rect(screen, green_2, (0 + square, y * square, square, square))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_1, (x, y * square, square, square))
                pygame.draw.rect(screen, green_2, (x + square, y * square, square, square))
            else:
                pass
        else:
            if i == 1:
                pygame.draw.rect(screen, green_2, (0, y * square, square, square))
                pygame.draw.rect(screen, green_1, (0 + square, y * square, square, square))
            elif i % 2 == 0:
                x = i * 30
                pygame.draw.rect(screen, green_2, (x, y * square, square, square))
                pygame.draw.rect(screen, green_1, (x + square, y * square, square, square))
            else:
                pass


def background():
    for i in range(20):
        background_green(i, i)


def enter_text():
    font = pygame.font.Font("cartoonist_kooky.ttf", 35)
    img = font.render('PRESS ANY KEY TO START THE GAME', True, white)
    screen.blit(img, (300 - img.get_width() // 2, 285))  # Center the text


def game():
    background()
    update()

    snake = Snake()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background()
        snake.start()
        update()
        pygame.time.Clock().tick(fps)


def game_intro():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                running = False
                game()

        background()
        enter_text()
        update()


def main():
    game_intro()


if __name__ == "__main__":
    main()
