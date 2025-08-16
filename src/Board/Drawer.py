import pygame
from src.Constants import COLORS

class Drawer:
    def __init__(self, screen, default_font):
        self.screen = screen
        self.default_font = default_font

        pygame.display.set_caption("Eusudokure")
        pygame.display.set_icon(pygame.image.load('src/Images/logo.jpg'))

    def draw_fill(self, color):
        self.screen.fill(color)

    def draw_rect(self, params, width, color=COLORS['BLACK']):
        pygame.draw.rect(self.screen, color, params, width)

    def draw_rect_with_text(self, text, text_position, rect_dimension, width, color=COLORS['BLACK'], font=None):
        font_to_use = font if font else self.default_font
        text = font_to_use.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = text_position
        self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, color, pygame.Rect(rect_dimension), width)



    def draw_rect_with_params(self, rect_params, width, color=COLORS['BLACK']):
        pygame.draw.rect(self.screen, color, pygame.Rect(rect_params), width)

    def draw_line(self, start_pos, end_pos, width, color=COLORS['BLACK']):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def render_box_text(self, text, center, color=COLORS['BLACK'], font=None):
        font_to_use = font if font else self.default_font
        text = font_to_use.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = center
        self.screen.blit(text, text_rect)

    def render_text(self, text, position, color=COLORS['BLACK'], font=None):
        font_to_use = font if font else self.default_font
        text = font_to_use.render(text, True, color)
        self.screen.blit(text, position)

    def render_background(self, background, position):
        self.screen.blit(background, position)

    def render_button(self, text, dimension, position, width=1, color=COLORS['BLACK'], font = None):
        font_to_use = font if font else self.default_font
        pygame.draw.rect(self.screen, color, dimension, width)
        text = font_to_use.render(text, True, color)
        self.screen.blit(text, position)