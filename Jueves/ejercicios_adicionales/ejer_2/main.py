class Estudiante:
    def __init__(self, nombre, fecha_nacimiento, carrera, anio_ingreso):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera
        self.anio_ingreso = anio_ingreso

    def __str__(self):
        return f"Nombre: {self.nombre} | Fecha Nacimiento: {self.fecha_nacimiento} | Carrera: {self.carrera} | Año Ingreso: {self.anio_ingreso}"
    

class Asignatura:
    def __init__(self, nombre, fecha_inicio, estudiante):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.estudiante = estudiante

    def __str__(self):
        ## con el f"..{..}" sirve para retornar un string con dentro de los { } poner una variable
        ## para que sea dinamico
        return f"Asignatura: {self.nombre} | Inicio: {self.fecha_inicio}\nEstudiante -> {self.estudiante}"

def main():
    print("--- DATOS DEL ESTUDIANTE ---")
    nombre_est = input("Nombre: ")
    fecha_nac = input("Fecha de nacimiento (DD/MM/AAAA): ")
    carrera = input("Carrera: ")
    anio = int(input("Año de ingreso: "))

    estudiante = Estudiante(nombre_est, fecha_nac, carrera, anio)

    print("\n--- DATOS DE LA ASIGNATURA ---")
    nombre_asig = input("Nombre de la Asignatura: ")
    fecha_inicio = input("Fecha inicio clases (DD/MM/AAAA): ")

    asignatura = Asignatura(nombre_asig, fecha_inicio, estudiante)

    print("\n--- REGISTRO COMPLETADO ---")
    print(asignatura)

if __name__ == "__main__":
    main()