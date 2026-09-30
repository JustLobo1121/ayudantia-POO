colores_base     = ['🟩', '🟩', '🟩', 'X', '🟫', '🟫', '🟫']
direcciones_base = ['Derecha', 'Derecha', 'Derecha', 'X', 'Izquierda', 'Izquierda', 'Izquierda']

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Rana:
    def __init__(self, color, direccion):
        self.color = color
        self.direccion = direccion

class Laguna:
    def __init__(self):
        self.ranas = [Rana(colores_base[i], direcciones_base[i]) for i in range(len(colores_base))]

    def mostrar_ranas(self):
        for rana in self.ranas:
            print(f'{rana.color} ', end='')
        print()

    # Una manera más optimizada de hacerlo
    def saltar(self, i, es_simple):
        # Dirección controla si sumamos o restamos el paso
        if self.ranas[i].direccion == 'Derecha':
            multi = 1
        else:
            multi = -1
        # Se selecciona el paso
        if es_simple:
            multi *= 1
        else:
            multi *= 2

        # Lógica
        if self.ranas[i + multi].color != 'X':
            print("Movimiento inválido")
            return
        # Swap
        self.ranas[i], self.ranas[i + multi] = self.ranas[i + multi], self.ranas[i] # a,b = b,a

    # Una manera simple de hacerlo
    def saltar_normal(self, i, es_simple):
        if self.ranas[i].direccion == 'Derecha':
            if es_simple:
                if self.ranas[i + 1].color != 'X':
                    print("Movimiento inválido")
                    return
                # a,b = b,a
                self.ranas[i], self.ranas[i + 1] = self.ranas[i + 1], self.ranas[i]
            else:
                if self.ranas[i + 2].color != 'X':
                    print("Movimiento inválido")
                    return
                # a,b = b,a
                self.ranas[i], self.ranas[i + 2] = self.ranas[i + 2], self.ranas[i]

        else:
                    if es_simple:
                        if self.ranas[i - 1].color != 'X':
                            print("Movimiento inválido")
                            return
                        # a,b = b,a
                        self.ranas[i], self.ranas[i - 1] = self.ranas[i - 1], self.ranas[i]
                    else:
                        if self.ranas[i - 2].color != 'X':
                            print("Movimiento inválido")
                            return
                        # a,b = b,a
                        self.ranas[i], self.ranas[i - 2] = self.ranas[i - 2], self.ranas[i]

    def partida_ganada(self):
        # Si no es una copia se invertiría el arreglo original, y no queremos eso
        temp = colores_base.copy()
        temp.reverse()
        return temp == [rana.color for rana in self.ranas]

def main():
    respuesta = input("Desea jugar? (S/N) ").upper()
    if respuesta == 'S':
        respuesta = input("Ingrese su nombre: ")
        jugador = Jugador(respuesta)
        laguna = Laguna()
        # De aquí en adelante es lógica
        while not laguna.partida_ganada():
            laguna.mostrar_ranas()
            respuesta_1 = int(input(f"Seleccione una rana (1-{len(colores_base)}): "))
            # Tipo de salto
            print("Seleccione un tipo de salto.\n" \
                  "1. Salto simple\n"              \
                  "2. Salto doble"
                 )
            respuesta_2 = int(input("Tipo de salto: "))
            # Salto
            laguna.saltar(respuesta_1 - 1, True if respuesta_2 == 1 else False)
            # También se puede usar la otra alternativa
            # laguna.saltar_normal(respuesta_1 - 1, True if respuesta_2 == 1 else False)
        # Gana el jugador
        laguna.mostrar_ranas()
        print("Ganaste, tienes un token más en tu chatbot favorito!!!!")
        print("/s")
    elif respuesta == 'N':
        print("Adiós")
    else:
        print("Respuesta inválida")

if __name__ == '__main__':
    main()
