import random


class Snake:
    pass


class ApplesSpawn:
    pass


def game():
    game_end = False
    x = 32
    y = 32

    apple = "▅"
    snake_head = "#"

    border = "@"
    space = " "

    border_done = (y + 2) * border

    while game_end == False:
        for i in range(y):
            print(border_done)
        quit()


def intro():
    print("WELCOME TO THE SNAKE GAME !!!")
    print("")
    print("PRESS ENTER TO START THE GAME")
    print("")
    input()
    game()


def main():
    intro()


if __name__ == "__main__":
    main()
