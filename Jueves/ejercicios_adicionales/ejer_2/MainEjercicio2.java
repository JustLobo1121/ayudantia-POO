package ejercicios_adicionales.ejer_2;

import java.util.Scanner;

class Estudiante {
    private String nombre;
    private String fechaNacimiento;
    private String carrera;
    private int anioIngreso;

    public Estudiante(String nombre, String fechaNacimiento, String carrera, int anioIngreso) {
        this.nombre = nombre;
        this.fechaNacimiento = fechaNacimiento;
        this.carrera = carrera;
        this.anioIngreso = anioIngreso;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " | Fecha Nacimiento: " + fechaNacimiento + 
               " | Carrera: " + carrera + " | Año Ingreso: " + anioIngreso;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(String fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    public int getAnioIngreso() {
        return anioIngreso;
    }

    public void setAnioIngreso(int anioIngreso) {
        this.anioIngreso = anioIngreso;
    }
    
}

class Asignatura {
    private String nombre;
    private String fechaInicio;
    private Estudiante estudiante;

    public Asignatura(String nombre, String fechaInicio, Estudiante estudiante) {
        this.nombre = nombre;
        this.fechaInicio = fechaInicio;
        this.estudiante = estudiante;
    }

    @Override
    public String toString() {
        return "Asignatura: " + nombre + " | Inicio: " + fechaInicio + 
               "\nEstudiante -> " + estudiante.toString();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFechaInicio() {
        return fechaInicio;
    }

    public void setFechaInicio(String fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public Estudiante getEstudiante() {
        return estudiante;
    }

    public void setEstudiante(Estudiante estudiante) {
        this.estudiante = estudiante;
    }
    
}

public class MainEjercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        /*
         * consejo con los getters y setters en vscode usar el ctrl + .
        */
        // Ingresar datos de Estudiante
        System.out.println("--- DATOS DEL ESTUDIANTE ---");
        System.out.print("Nombre: ");
        String nombreEst = scanner.nextLine();
        System.out.print("Fecha de nacimiento (DD/MM/AAAA): ");
        String fechaNac = scanner.nextLine();
        System.out.print("Carrera: ");
        String carrera = scanner.nextLine();
        System.out.print("Año de ingreso: ");
        int anio = Integer.parseInt(scanner.nextLine());

        Estudiante estudiante = new Estudiante(nombreEst, fechaNac, carrera, anio);

        // Ingresar datos de Asignatura
        System.out.println("\n--- DATOS DE LA ASIGNATURA ---");
        System.out.print("Nombre de la Asignatura: ");
        String nombreAsig = scanner.nextLine();
        System.out.print("Fecha inicio clases (DD/MM/AAAA): ");
        String fechaInicio = scanner.nextLine();

        Asignatura asignatura = new Asignatura(nombreAsig, fechaInicio, estudiante);

        // Mostrar datos
        System.out.println("\n--- REGISTRO COMPLETADO ---");
        System.out.println(asignatura.toString());
        
        scanner.close();
    }
}