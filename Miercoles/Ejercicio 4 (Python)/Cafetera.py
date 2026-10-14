from Insumo import Insumo

class Cafetera(Insumo):
    """
    Representa una cafetera que tiene un tipo,
    la cafeteria siendo un insumo a su vez
    """
    def __init__(self, sku, nombre, descripcion, precio,
                tipo):
        # Tipos:
        # Flitro por goteo
        # Francesa
        # De sifón
        # Moka
        # Italiana
        # Aeropress
        # Máquina espresso
        super(sku, nombre, descripcion, precio, tipo)