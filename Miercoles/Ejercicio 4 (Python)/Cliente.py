from Carrito import Carrito
from Envio import Envio

class Cliente:
    """
    Clase que guarda información básica
    del cliente
    """
    def __init__(self, rut, nombre, correo):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito()
        self.envios = []

    def comprar_carrito(self):
        # Verificar que el carrito no esté vacío
        if len(self.carrito.lista) == 0:
            print("Tu carrito está vacío, no puedes comprar!")
            return
        print("Resumen del carrito:")
        total = self.carrito.mostrar()
        print("Compra exitosa!")
        print("Generando envío")
        envio = Envio(1234, f"Envío de compra con un total de {total}",
                      total, 2000, "2026-10-20")
        self.envios.append(envio)
        print("Envío generado")
        print(f"Fecha estima de entrega {envio.fechaEstimada}")
