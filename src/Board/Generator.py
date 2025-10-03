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
            self.grid = [ grilla de listas de valores de 0 a 9, 9 listas]. Si te fijas en el generator.py que pusiste, ese grid cae perfecto aca
    
    """
    def __init__(self, k, grid):
        self.k = k
        self.grid = grid # esto podria ser self.grid = La mouse herramienta misteriosa

    # Good
    def setK(self, k):
        self.k = k

    # Hacete una funcion getGrid que devuelva solo el grid. def getGrid(self): dame grid
    
    # def fillBox(self):
    # Un chingo de logica

    """
    Te faltan funciones para agregar. Aca tene presente que la grid no necesariamente va a pasar como parametro. Esto anda probando, que funciona mejor.
    Habran casos donde tengas a la funcion que pasarle el grid, o simplemente dentro de la funcion llamas al grid y completas y solo le pasas los indices.
    Te dejo dos ejemplos en el fillDiagonal.
    Para llamar al grid desde otra funcion, usa simplemente self.grid y listo.
    Es por eso que el primer parametro de cada funcion siempre debe ser el self, es como el this. Con tener el self ya podes referenciar.
    Incluso, puedes llamar a otras funciones dentro de tu clase, usando self. Haces self.function y listo
    """
    def fillDiagonal(self):
        pass # Este pass es como un return true, sirve para que no te marque como funcion incompleta. Quitalo cuando armes la funcion.
        """
        Dos ejemplos:
        # ... completar ...
        # self.fillBox(self.grid, i, i) # Aca tu funcion recibe el grid por parametro. Como python es python, deberia modificar esa matriz, o por ahi no, probalo ;)
        
        # ... completar ...
        # self.fillBox(i, i) # En este caso, tu fillBox dentro debe llamar a self.grid para completarle lo que corresponda
        """

    def fillRemaining(self):
        pass # Este pass es como un return true, sirve para que no te marque como funcion incompleta. Quitalo cuando armes la funcion.

    # Como es un metodo de la clase, tambien necesita el self. def removeKDigits(self, grid, k):
    # Aca tambien puedes usar self.k para no pasar parametro, aunque como lo estas modificando, tendras que reemplazar todos los k por self.k
    # La otra es una variable temporal, k_aux = self.k, modificas el k_aux pero acordate al final de la funcion hacer self.k = k_aux porque lo modificaste
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