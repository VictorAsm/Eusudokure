from src.Constants import COLORS

class Cell:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.sketch = 0
        self.selected = False

    def set_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def set_selected(self, value):
        self.selected = value

    def draw(self, drawer):
        if self.value != 0:
            drawer.render_box_text(text=str(self.value), center=(75 + (self.col - 1) * 50, 75 + (self.row - 1) * 50))

        if self.selected:
            drawer.draw_rect_with_params(rect_params=(50 + (self.col - 1) * 50, 50 + (self.row - 1) * 50, 50, 50), width=4, color=COLORS['RED'])

        if self.sketch != 0:
            drawer.render_box_text(text=str(self.sketch), center=(75 + (self.col - 1) * 50, 75 + (self.row - 1) * 50), color=COLORS['GRAY'])

        drawer.draw_rect_with_params(rect_params=(50 + (self.col - 1) * 50, 50 + (self.row - 1) * 50, 50, 50), width=1)

        if (self.col + 1) % 3 == 0 and self.col != 8:
            drawer.draw_line(start_pos=((self.col + 1) * 50, 0), end_pos=((self.col + 1) * 50, 450), width=4)

        if (self.row + 1) % 3 == 0 and self.row != 8:
            drawer.draw_line(start_pos=(0, (self.row + 1) * 50), end_pos=(450, (self.row + 1) * 50), width=4)
