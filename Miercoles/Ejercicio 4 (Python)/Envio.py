class Envio:
    """
    Describe un envío con su número de envío,
    descripción, montos y fecha estimada
    """
    def __init__(self, numero, descripcion, montoCompra,
                 montoEnvio, fechaEstimada):
        self.numero = numero
        self.descripcion = descripcion
        self.montoCompra = montoCompra
        self.montoEnvio = montoEnvio
        self.fechaEstimada = fechaEstimada