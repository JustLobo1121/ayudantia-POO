from Cliente import Cliente
from Producto import Producto
from Tienda import Tienda

tienda = Tienda()

"""
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
"""

print("Bienvenido a la cafetería Monje Capuccino!")
print("Ingrese sus datos de cliente:")
rut = input("RUT: ")
nombre = input("Nombre: ")
correo = input("Correo: ")

# Crear cliente
cliente = Cliente(rut, nombre, correo)

# Bucle de ejecución
while True:
    print("Opciones:")
    print("1. Agregar un producto a la tienda")
    print("2. Mostrar productos de la tienda")
    print("3. Mostrar carrito de compras")
    opcion = int(input("Escoja una opción: "))
    if opcion == 1:
        # Preguntas
        sku = input("Ingrese el SKU del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = input("Ingrese el precio del producto: ")
        # Crear producto
        producto = Producto(sku, nombre, descripcion, precio)
        tienda.agregar_producto(producto)
        print("Producto agregado")
        print()
    elif opcion == 2:
        tienda.mostrar_productos()
    elif opcion == 3:
        cliente.carrito.mostrar()
    else:
        print("Opción inválida!")
