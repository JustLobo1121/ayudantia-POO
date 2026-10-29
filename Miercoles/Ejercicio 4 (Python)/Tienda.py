class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay ningún producto registrado")
            return
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: {producto.precio}")
            print(f"SKU: {producto.sku}")
            print("==========")
