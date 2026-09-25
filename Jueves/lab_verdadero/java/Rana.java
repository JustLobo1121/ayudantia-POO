package lab_verdadero.java;

public class Rana {
    private String color;
    private int direccion;
    
    public Rana(String color, int direccion) {
        this.color = color;
        this.direccion = direccion;
    }

    public String getColor() {
        return color;
    }

    public int getDireccion() {
        return direccion;
    }

    @Override
    public String toString() {
        return color.substring(0,1);
    }
}
