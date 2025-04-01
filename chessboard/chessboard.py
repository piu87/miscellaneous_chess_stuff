import pygame


# defining some constants about the window
width, height = 400, 400
rows, cols = 8, 8
square_size = width / cols
white = (240, 217, 181)
black = (181, 136, 99)

# starting pygame
pygame.init()

# creating the window
board = pygame.display.set_mode((width, height))
pygame.display.set_caption("board")


def draw_board(board):

    for row in range(rows):  # looping through each row (0 to 7)
        for col in range(cols):  # looping through each column (0 to 7)
            color = white if (row + col) % 2 == 0 else black # using the remainder to determine the color
            pygame.draw.rect(board, color, (col * square_size, row * square_size, square_size, square_size))


def main_game_loop():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board(board)
        pygame.display.update()  # refresh the display to show the window

    pygame.quit()


# starting the program
main_game_loop()

