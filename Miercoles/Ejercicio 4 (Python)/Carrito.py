class Carrito:
    """
    Carrito de compras del cliente
    """
    def __init__(self):
        self.lista = []

    def agregar(self, producto):
        self.lista.append(producto)

    def eliminar(self, producto):
        self.lista.remove(producto)

    def mostrar(self):
        if len(self.lista) == 0:
            print("No hay nada en el carrito")
            return
        total = 0
        for producto in self.lista:
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: {producto.precio}")
            print(f"SKU: {producto.sku}")
            print("==========")
            # Sumar al total
            total = total + producto.precio
        print(f"Total del carrito: {total}")
        return total
