from Cliente import Cliente
from Producto import Producto
from Tienda import Tienda

tienda = Tienda()
p1 = Producto(1234, "Cachupin", "Comida", 10000)
tienda.agregar_producto(p1)
p2 = Producto(4444, "El pepe", "Algo", 5000)
tienda.agregar_producto(p2)
p3 = Producto(1000, "67", "67", 6767)
tienda.agregar_producto(p3)

cliente = Cliente(12345678, "Ermenegildo", "hola@gmail.com")
cliente.carrito.agregar(p3)
cliente.carrito.agregar(p2)

cliente.comprar_carrito()