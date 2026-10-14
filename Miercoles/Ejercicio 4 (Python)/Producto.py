from abc import ABC

class Producto(ABC):
    """
    Objeto con SKU, nombre, descripción y precio.
    Es una clase abstracta.
    """
    def __init__(self, sku, nombre, descripcion, precio):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio