import random

class Buscaminas:
    def __init__(self, n, bombas):
        self.n = n
        self.arr = []

        # Popular la matriz
        for i in range(n):
            self.arr.append([])
            for j in range(n):
                self.arr[i].append([])

        # También colocar bombas al azar
        while bombas != 0:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            self.arr[i][j] = 'X'
            bombas = bombas - 1

        # Rellenar el tablero con la cantidad de bombas
        for i in range(n):
            for j in range(n):
                # Hay una bomba, ignorar
                if self.arr[i][j] == 'X':
                    continue
                contador = 0
                # Caso 1: elemento en una esquina
                if i == 0 and j == 0:
                    if self.arr[0][1] == 'X':
                        contador = contador + 1
                    if self.arr[1][0] == 'X':
                        contador = contador + 1
                    if self.arr[1][1] == 'X':
                        contador = contador + 1

                elif i == 0 and j == n - 1:
                    if self.arr[0][n - 2] == 'X':
                        contador = contador + 1
                    if self.arr[1][n - 1] == 'X':
                        contador = contador + 1
                    if self.arr[1][n - 2] == 'X':
                        contador = contador + 1

                elif i == n - 1 and j == 0:
                    if self.arr[n - 1][1] == 'X':
                        contador = contador + 1
                    if self.arr[n - 2][0] == 'X':
                        contador = contador + 1
                    if self.arr[n - 2][1] == 'X':
                        contador = contador + 1

                elif i == n - 1 and j == n - 1:
                    if self.arr[n - 1][n - 2] == 'X':
                        contador = contador + 1
                    if self.arr[n - 2][n - 2] == 'X':
                        contador = contador + 1
                    if self.arr[n - 2][n - 1] == 'X':
                        contador = contador + 1

                # Asignamos la cantidad de bombas
                self.arr[i][j] = contador

    def mostrar(self):
        for i in range(self.n):
            print(self.arr[i])
