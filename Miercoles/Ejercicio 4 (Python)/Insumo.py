from Producto import Producto

class Insumo(Producto):
    """
    Insumo que tiene un tipo y es un producto
    """
    def __init__(self, sku, nombre, descripcion, precio, tipo):
        super(sku, nombre, descripcion, precio)
        self.tipo = tipo