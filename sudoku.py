import pygame
from src.Board.Drawer import Drawer
from src.Board.Board import Board
from src.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_START, GAME_IN_PROGRESS, GAME_OVER, ROWS, COLS
from src.State.Game_State import game_start, game_in_progress, game_over

pygame.init()
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FONT = pygame.font.Font(None, 30)

# Set Drawer
drawer = Drawer(screen=game_window, default_font=pygame.font.SysFont('calibri', 40))

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
                    board = Board(ROWS, COLS)
                    print("EASY")
                    game_screen = GAME_IN_PROGRESS
                elif 180 < x < 270 and 350 < y < 380:
                    # Start a new medium game
                    board = Board(ROWS, COLS)
                    print("MEDIUM")
                    game_screen = GAME_IN_PROGRESS
                elif 330 < x < 420 and 350 < y < 380:
                    # Start a new hard game
                    board = Board(ROWS, COLS)
                    print("HARD")
                    game_screen = GAME_IN_PROGRESS

        elif game_screen == GAME_IN_PROGRESS:

            if 40 < x < 130 and 460 < y < 490:
                print("Reset")
            elif 180 < x < 270 and 460 < y < 490:
                game_screen = GAME_START
            elif 330 < x < 420 and 460 < y < 490:
                pygame.quit()

            # TODO: Check Board existance
            if board.click(x, y) is not None:
                row_selected, col_selected = board.click(x, y)
                board.select(row_selected, col_selected)

            if event.type == pygame.KEYDOWN:
                print(event)
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if num in range(0, 10):
                        board.sketch(num)
                elif event.unicode == '\r':
                    board.place_number(num)
                elif event.unicode == '\x08':
                    board.place_number(0)

        elif game_screen == GAME_OVER:
            if 200 < x < 340 and 400 < y < 440:
                print("Quit")
                game_screen = GAME_START

        if game_screen == GAME_START:
            game_start(drawer)
        elif game_screen == GAME_IN_PROGRESS:
            game_in_progress(drawer, board=board)

        # TODO: Check game finish game
        """
        elif game_screen == GAME_OVER:
            game_over(drawer, board)
      """

        pygame.display.update()

# Quit Pygame
pygame.quit()