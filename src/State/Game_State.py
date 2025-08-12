import pygame

from src.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, BLACK, BACKGROUND, BACKGROUND_WIN, BACKGROUND_LOST

def getGeneralBackground():
    background = pygame.image.load(BACKGROUND)
    background_rect = background.get_rect()
    background_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def getWinBackground():
    background = pygame.image.load(BACKGROUND_WIN)
    original_width, original_height = background.get_size()
    new_width = int(original_width * 0.5)
    new_height = int(original_height * 0.5)
    background = pygame.transform.scale(background, (new_width, new_height))
    background_rect_win = background.get_rect()
    background_rect_win.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def getLostBackground():
    background = pygame.image.load(BACKGROUND_LOST)
    background_rect_lost = background.get_rect()
    background_rect_lost.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def gameStart(game_window, font):

    background = getGeneralBackground()
    game_window.blit(background, (0, 0))

    # Rendering menu
    text = font.render("Bienvenido a Eusudokure", True, WHITE)
    game_window.blit(text, (100, 120))

    text = font.render("Selecciona la dificultad:", True, WHITE)
    game_window.blit(text, (100, 250))

    pygame.draw.rect(game_window, WHITE, (40, 350, 90, 30), 1)
    text = font.render("Facil", True, WHITE)
    game_window.blit(text, (50, 350))

    pygame.draw.rect(game_window, WHITE, (180, 350, 90, 30), 1)
    text = font.render("Normal", True, WHITE)
    game_window.blit(text, (190, 350))

    pygame.draw.rect(game_window, WHITE, (330, 350, 90, 30), 1)
    text = font.render("Dificil", True, WHITE)
    game_window.blit(text, (350, 350))

def gameInProgress(game_window, font, board):

    background = getGeneralBackground()
    game_window.blit(background, (0, 0))

    # Rendering in progress game
    board.draw()

    # Rendering buttons
    pygame.draw.rect(game_window, BLACK, (40, 460, 90, 30), 1)
    text = font.render("reset", True, BLACK)
    game_window.blit(text, (50, 460))

    pygame.draw.rect(game_window, BLACK, (180, 460, 90, 30), 1)
    text = font.render("restart", True, BLACK)
    game_window.blit(text, (200, 460))

    pygame.draw.rect(game_window, BLACK, (330, 460, 90, 30), 1)
    text = font.render("exit", True, BLACK)
    game_window.blit(text, (350, 460))

def gameOver(game_window, font, board):
    # Check board. game_over_state TRUE => WIN. FALSE => LOST
    if board.game_over_state:
        background = getWinBackground()
        game_window.blit(background, (0, 0))

        text = font.render("Game Won!", True, WHITE)
        game_window.blit(text, (200, 250))

        text = font.render("Exit", True, WHITE)
        game_window.blit(text, (220, 410))
    else:

        background = getLostBackground()
        game_window.blit(background, (0, 0))

        text = font.render("Game Over", True, WHITE)
        game_window.blit(text, (200, 250))

        text = font.render("Restart", True, WHITE)
        game_window.blit(text, (220, 410))

    pygame.draw.rect(game_window, WHITE, (200, 400, 140, 40), 1)