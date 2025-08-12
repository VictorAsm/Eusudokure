import pygame
from src.Board.Board import Board
from src.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_START, GAME_IN_PROGRESS, GAME_OVER, ROWS, COLS
from src.State.Game_State import gameStart, gameInProgress, gameOver

pygame.init()
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Eusudokure")

icon = pygame.image.load('src/Images/logo.jpg')
pygame.display.set_icon(icon)
FONT = pygame.font.Font(None, 30)

# Set Initial State
game_screen = GAME_START

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if game_screen == GAME_START:
                if 40 < x < 130 and 350 < y < 380:
                    # Start a new easy game
                    board = Board(ROWS, COLS, game_window)
                    print("EASY")
                    game_screen = GAME_IN_PROGRESS
                elif 180 < x < 270 and 350 < y < 380:
                    # Start a new medium game
                    board = Board(ROWS, COLS, game_window)
                    print("MEDIUM")
                    game_screen = GAME_IN_PROGRESS
                elif 330 < x < 420 and 350 < y < 380:
                    # Start a new hard game
                    board = Board(ROWS, COLS, game_window)
                    print("HARD")
                    game_screen = GAME_IN_PROGRESS

            elif game_screen == GAME_IN_PROGRESS:
                if 40 < x < 130 and 460 < y < 490:
                    print("Reset")
                elif 180 < x < 270 and 460 < y < 490:
                    game_screen = GAME_START
                elif 330 < x < 420 and 460 < y < 490:
                    pygame.quit()


            elif game_screen == GAME_OVER:
                if 200 < x < 340 and 400 < y < 440:
                    print("Quit")
                    game_screen = GAME_START

        if game_screen == GAME_START:
            gameStart(game_window, FONT)
        elif game_screen == GAME_IN_PROGRESS:
            gameInProgress(game_window, FONT, board)
        elif game_screen == GAME_OVER:
            gameOver(game_window, FONT, board)

        pygame.display.update()

# Quit Pygame
pygame.quit()