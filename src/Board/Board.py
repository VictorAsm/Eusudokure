from src.Board.Cell import Cell
from src.Constants import COLORS
import random # TODO: Remove

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[Cell(random.randint(0, 9), row, col) for col in range(9)] for row in range(9)]
        self.selected_row = None
        self.selected_col = None
        self.game_started = False

    def draw(self, drawer):
        drawer.draw_fill(color=COLORS['WHITE'])

        for row in range(9):
            for col in range(9):
                cell = self.grid[row][col]
                cell.draw(drawer)

    def select(self, row, col):
        if (self.selected_row is not None) and (self.selected_col is not None):
            self.grid[self.selected_row][self.selected_col].set_selected(False)

        self.selected_row = row
        self.selected_col = col
        self.grid[self.selected_row][self.selected_col].set_selected(True)

    def click(self, x, y):
        if x < 0 or y < 0 or x > self.width * 50 or y > self.height * 50:
            return None
        row = y // 50
        col = x // 50
        return row, col

    def sketch(self, value):
        cell_value = self.grid[self.selected_row][self.selected_col].value
        if cell_value == 0:
            self.grid[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        cell_value = self.grid[self.selected_row][self.selected_col].value
        if cell_value == 0:
            self.grid[self.selected_row][self.selected_col].set_value(value)
            self.grid[self.selected_row][self.selected_col].set_sketched_value(0)

    def is_full(self):
        return False