import random

class Jugador:
    def __init__(self, palabra):
        self.intentos_restantes = 6
        self.palabra_arreglo = []
        self.adivinanza_arreglo = []

        # Avanzar por la palabra
        for letra in palabra:
            self.palabra_arreglo.append(letra)

        # Inicializar el arreglo de la palabra adivinada
        for _ in self.palabra_arreglo:
            self.adivinanza_arreglo.append('_')

        # Copiar una letra al azar
        i = random.randint(0, len(self.palabra_arreglo) - 1)
        self.adivinanza_arreglo[i] = self.palabra_arreglo[i]

    def es_ganador(self):
        for i in range(len(self.palabra_arreglo)):
            if self.palabra_arreglo[i] != self.adivinanza_arreglo[i]:
                return False
        return True

    def mostrar(self):
        print(f"Intentos restantes: {self.intentos_restantes}")
        for letra in self.adivinanza_arreglo:
            print(f"{letra} ", end="")
        print()

    def adivinar(self, letra):
        if letra not in self.palabra_arreglo:
            self.intentos_restantes = self.intentos_restantes - 1
        else:
            # Pasar todas las veces que aparezca la letra
            for i in range(len(self.palabra_arreglo)):
                if self.palabra_arreglo[i] == letra:
                    self.adivinanza_arreglo[i] = letra
