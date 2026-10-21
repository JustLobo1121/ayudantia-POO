from Jugador import Jugador

palabra = input("Ingrese la palabra original: ")

jugador = Jugador(palabra)

# Cómo queda el arreglo?
# print(jugador.palabra_arreglo)

while not jugador.es_ganador():
    jugador.mostrar()
    letra_adivinada = input("Ingrese una posible letra: ")
    jugador.adivinar(letra_adivinada)
    if jugador.intentos_restantes == 0:
        print("Has perdido, pues te has quedado sin intentos")
        break

# El jugador ganó el juego
if jugador.intentos_restantes > 0:
    jugador.mostrar()
    print("Has ganado!")
