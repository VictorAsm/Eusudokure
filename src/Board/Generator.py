import sudoku
import random

class Generator:
    """
    La clase no deberia recibir un grid, porque es tu clase la que lo genera. Sin embargo, a lo largo de tu clase, existe tu grid, por lo que, no la pasas por parametro
    pero la instancias. Si ves el generator.py entonces sabes como generar ese grid. Es como darle un valor predefinido.
    Con el K podría pasar algo similar, puede asignarse al principio, o usar el setter cuando le des en jugar.
    Ambas opciones andan bien, pero te lo dejo a vos, lo que mas sencillo se te ocurra.
    Entonces deberia quedarte algo como
        def __init__(self, k):
            self.k = k

    """
    def __init__(self, k):
        self.k = k
        self.grid = grid = [[0] * 9 for _ in range(9)] # La mouse herramienta misteriosa
        """self.grid = [ grilla de listas de valores de 0 a 9, 9 listas]. 
        Si te fijas en el generator.py que pusiste, ese grid cae perfecto aca
        """

    def setK(self, k):
        self.k = k

    def getGrid(self):
        return self.grid

    def fillBox(self):
        for i in range(3):
            for j in range(3):
                while True:
                    # Generate a random number between 1 and 9
                    num = random.randint(1, 9)
                    if unUsedInBox(self.grid, row, col, num):
                        break
                self.grid[row + i][col + j] = num

    def unUsedInBox(grid, rowStart, colStart, num):
        for i in range(3):
            for j in range(3):
                if grid[rowStart + i][colStart + j] == num:
                    return False
        return True

    """
    Te faltan funciones para agregar. Aca tene presente que la grid no necesariamente va a pasar como parametro. Esto anda probando, que funciona mejor.
    Habran casos donde tengas a la funcion que pasarle el grid, o simplemente dentro de la funcion llamas al grid y completas y solo le pasas los indices.
    Te dejo dos ejemplos en el fillDiagonal.
    Para llamar al grid desde otra funcion, usa simplemente self.grid y listo.
    Es por eso que el primer parametro de cada funcion siempre debe ser el self, es como el this. Con tener el self ya podes referenciar.
    Incluso, puedes llamar a otras funciones dentro de tu clase, usando self. Haces self.function y listo
    """
    def fillDiagonal(self):
        self.fillBox(self.grid, i, i) # Aca tu funcion recibe el grid por parametro. Como python es python, deberia modificar esa matriz, o por ahi no, probalo ;)

    def fillRemaining(self):
        pass # Este pass es como un return true, sirve para que no te marque como funcion incompleta. Quitalo cuando armes la funcion.

    def removeKDigits(self):

        while self.k > 0:
            # Pick a random cell
            cellId = random.randint(0, 80)

            # Get the row index
            i = cellId // 9

            # Get the column index
            j = cellId % 9

            # Remove the digit if the cell is not already empty
            if self.grid[i][j] != 0:
                # Empty the cell
                self.grid[i][j] = 0
                # Decrease the count of digits to remove
                self.k -= 1

    """
    Una vez tengas tus funciones, las principales unificalas en un solo metodo: generateSudoku(self). 
    Asi podemos tener el control al iniciar el game. Pensa que en el sudoky.py, cuando le demos click en iniciar debera ocurrir una secuencia asi:

        Generator.setK(K)
        GRID = Generator.generateSudoku()
        board = Board(ROWS, COLS, GRID)

    # Pensa el generateSudoku como el main de tu clase. El nucleo, el centro de todo
    def generateSudoku(self):
        Aca generas tu sudoku con tus funciones y tu referencia
        self.primer funcion
        self.segunda funcion
        ...
        self.ultima funcion
        return self.grid # Por simplicidad lo devolves. Si queres ir un pasito más, te haces un getter del grid, y el return se lo das alli.

        Si haces ese getter, la secuencia queda como:
        Generator.setK(K)
        Generator.generateSudoku()
        GRID = Generator.getGrid()
        board = Board(ROWS, COLS, GRID)

    Son cuestiones de diseño
    """