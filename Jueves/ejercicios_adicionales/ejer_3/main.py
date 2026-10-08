class Contacto:
    def __init__(self, direccion_fisica, correo_electronico, telefono_fijo, telefono_movil):
        self.direccion_fisica = direccion_fisica
        self.correo_electronico = correo_electronico
        self.telefono_fijo = telefono_fijo
        self.telefono_movil = telefono_movil

class Cliente:
    def __init__(self, rut, nombre, contacto):
        self.rut = rut
        self.nombre = nombre
        self.contacto = contacto

class Colaborador:
    def __init__(self, rut, nombre, cargo, contacto):
        self.rut = rut
        self.nombre = nombre
        self.cargo = cargo
        self.contacto = contacto
        self.clientes = []  # Listado de clientes
    ## en caso de no hacer este metodo al hacer una nueva instancia
    ## modificar el constructor para agregar la lista de clientes
    ## pero a la altura de lista de clientes usar el [...]
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

class Empresa:
    def __init__(self, nombre, fecha_fundacion):
        self.nombre = nombre
        self.fecha_fundacion = fecha_fundacion
        self.colaboradores = []  # Listado de colaboradores

    def agregar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)

def main():
    ## en caso de querer usar un menu
    ## usar el bucle while(true) y usar el input(...)

    # Ejemplo de uso e instanciación del modelo
    mi_empresa = Empresa("Tech Solutions", "15/08/2010")
    
    contacto_colab = Contacto("Av. Principal 123", "juan@tech.com", "22334455", "+56987654321")
    colaborador = Colaborador("11.111.111-1", "Juan Pérez", "Ejecutivo de Ventas", contacto_colab)
    
    contacto_cliente = Contacto("Calle Sur 456", "cliente@mail.com", "22998877", "+56912345678")
    cliente = Cliente("22.222.222-2", "Comercializadora SPA", contacto_cliente)
    
    colaborador.agregar_cliente(cliente)
    mi_empresa.agregar_colaborador(colaborador)
    
    print("Estructura de la empresa inicializada correctamente.")

if __name__ == "__main__":
    main()