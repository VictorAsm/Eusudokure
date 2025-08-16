import pygame

from src.Constants import WINDOW_WIDTH, WINDOW_HEIGHT,  BACKGROUND, BACKGROUND_WIN, BACKGROUND_LOST, COLORS

def get_general_background():
    background = pygame.image.load(BACKGROUND)
    background_rect = background.get_rect()
    background_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def get_win_background():
    background = pygame.image.load(BACKGROUND_WIN)
    original_width, original_height = background.get_size()
    new_width = int(original_width * 0.5)
    new_height = int(original_height * 0.5)
    background = pygame.transform.scale(background, (new_width, new_height))
    background_rect_win = background.get_rect()
    background_rect_win.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def get_lost_background():
    background = pygame.image.load(BACKGROUND_LOST)
    background_rect_lost = background.get_rect()
    background_rect_lost.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    return background

def game_start(drawer):

    font = pygame.font.Font(None, 30)
    background = get_general_background()
    drawer.render_background(background, (0, 0))

    # Rendering menu
    drawer.render_text(text="Bienvenido a Eusudokure", position=(100, 120), color=COLORS['WHITE'], font = font)

    drawer.render_text(text="Selecciona la dificultad:", position=(100, 250), color=COLORS['WHITE'], font = font)

    drawer.render_button(text="Facil", dimension=(40, 350, 90, 30), position=(50, 350), color=COLORS['WHITE'], font = font)

    drawer.render_button(text="Normal", dimension=(180, 350, 90, 30), position=(190, 350), color=COLORS['WHITE'], font = font)

    drawer.render_button(text="Dificil", dimension=(330, 350, 90, 30), position=(350, 350), color=COLORS['WHITE'], font = font)

def game_in_progress(drawer, board):

    font = pygame.font.Font(None, 30)
    background = get_general_background()
    drawer.render_background(background, (0, 0))

    # Rendering in progress game
    board.draw(drawer)

    # Rendering buttons
    drawer.render_button(text="Reset", dimension=(40, 460, 90, 30), position=(50, 460), font = font)

    drawer.render_button(text="Restart", dimension=(180, 460, 90, 30), position=(200, 460), font=font)

    drawer.render_button(text="Exit", dimension=(330, 460, 90, 30), position=(350, 460), font=font)

def game_over(drawer, board):

    font = pygame.font.Font(None, 30)

    # Check board. game_over_state TRUE => WIN. FALSE => LOST
    if board.game_over_state:
        background = get_win_background()
        drawer.render_background(background, (0, 0))

        drawer.render_text(text="Ganaste!", position=(200, 250), color=COLORS['WHITE'], font=font)

        drawer.render_text(text="Salir", position=(220, 410), color=COLORS['WHITE'], font=font)
    else:

        background = get_lost_background()
        drawer.render_background(background, (0, 0))

        drawer.render_text(text="Perdiste!", position=(200, 250), color=COLORS['WHITE'], font=font)

        drawer.render_text(text="Reiniciar", position=(220, 410), color=COLORS['WHITE'], font=font)

    drawer.draw_rect(params=(200, 400, 140, 40), width=1, color=COLORS['WHITE'])