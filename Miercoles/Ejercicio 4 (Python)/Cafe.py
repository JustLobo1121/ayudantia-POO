from Producto import Producto

class Cafe(Producto):
    """
    Esta clase representa un café con su respectivo tipo,
    origen, aroma, acidez y molienda
    """
    def _init__(self, sku, nombre, descripcion, precio,
                tipo, origen, aroma, acidez, molienda):
        super(sku, nombre, descripcion, precio)
        # Arábica o robúsca
        self.tipo = tipo
        self.origen = origen
        self.aroma = aroma
        self.acidez = acidez
        # Gramo entero - sin molienda
        # Gramo fino
        # Gramo extrafino
        self.molienda = molienda