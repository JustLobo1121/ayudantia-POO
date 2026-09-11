package lab1;

// MODIFICACION PARA LA CLASE
// abstract class habitacion
public class habitacion {
    String nombre;
    int precio;
    String capacidad;
    public habitacion(String nombre, int precio, String capacidad) {
        this.nombre = nombre;
        this.precio = precio;
        this.capacidad = capacidad;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getPrecio() {
        return precio;
    }
    public void setPrecio(int precio) {
        this.precio = precio;
    }
    public String getCapacidad() {
        return capacidad;
    }
    public void setCapacidad(String capacidad) {
        this.capacidad = capacidad;
    }
    
}
/* EJEMPLO DE USO DE ABSTRACCION DE CLASE

class EjecutivaIndividual extends Habitacion {
    public EjecutivaIndividual(int numero) {
        super(numero, 30000, 2);
    }
}

class EjecutivaDoble extends Habitacion {
    public EjecutivaDoble(int numero) {
        super(numero, 60000, 4);
    }
}

class Familiar extends Habitacion {
    public Familiar(int numero) {
        super(numero, 120000, 8);
    }
}

class PentHouse extends Habitacion {
    private String orientacion; // Volcanes (NE) o Pacífico (SO)
    
    public PentHouse(int numero, String orientacion) {
        super(numero, 500000, 2);
        this.orientacion = orientacion;
    }
}
*/