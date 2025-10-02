import sudoku
import random

class Generator:
    def __init__(self, k, grid):
        self.k = k
        self.grid = grid

    def setK(self, k):
        self.k = k

    def fillDiagonal(self):

    def fillRemaining(self):

    def removeKDigits(grid,k):
        while k > 0:

            # Pick a random cell
            cellId = random.randint(0, 80)

            # Get the row index
            i = cellId // 9

            # Get the column index
            j = cellId % 9

            # Remove the digit if the cell is not already empty
            if grid[i][j] != 0:
                # Empty the cell
                grid[i][j] = 0
                # Decrease the count of digits to remove
                k -= 1