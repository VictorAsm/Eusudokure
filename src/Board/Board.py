import pygame

class Board:
    def __init__(self, width, height,  screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.grid = [[1,2,3],[4,5,6],[7,8,9]]

    def draw(self):
        self.screen.fill((255, 255, 255))

        # De 3x3 es la primera matriz. De 9x9 seran 3 matrices entre matrices
        for row in range(3):
            for col in range(3):
                cell_value = self.grid[row][col]
                font = pygame.font.SysFont('calibri', 40)

                text = font.render(str(cell_value), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (75 + (col - 1) * 50, 75 + (row - 1) * 50)
                self.screen.blit(text, text_rect)
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 pygame.Rect(50 + (col - 1) * 50, 50 + (row - 1) * 50, 50, 50), 1)

                if (col + 1) % 3 == 0 and col != 8:
                    pygame.draw.line(self.screen, (0, 0, 0), ((col + 1) * 50, 0), ((col + 1) * 50, 450),
                                     width=4)

                if (row + 1) % 3 == 0 and row != 8:
                    pygame.draw.line(self.screen, (0, 0, 0), (0, (row + 1) * 50), (450, (row + 1) * 50),
                                     width=4)