package lab1;

import java.util.Scanner;

import lab1.*;

public class main {
    public static void main(String[] args) {
        // muestra de instancias de clases
        habitacion h1 = new habitacion("Ejecutiva Individual", 30000, "2 (1 recomendado)");
        // habitacion h2 = new habitacion("Ejecutiva Doble", 60000, "4 (2 recomendados)");
        // habitacion h3 = new habitacion("Familiar", 120000,  "8 (6 recomendados)");
        // habitacion h4 = new habitacion("PentHouse", 500000,  "2 (con invitados temporales indefinidos)");
        pasajero p1 = new pasajero("11111", "john", "doe", "doe 1", null, "test");
        boolean menu = true;
        while (menu) {
            Scanner sc1 = new Scanner(System.in);
            // ejemplo de como hacer el menu
            System.out.println("1) caso 1");
            System.out.println("2) caso 2");
            System.out.println("3) caso 3");
            System.out.println("4) caso 4");
            System.out.println("Escribe tu opcion:");
            int opcion = sc1.nextInt();
            switch (opcion) {
                case 1:
                    System.out.println("test 1");
                    break;
                case 2:
                    System.out.println("test 2");
                    break;
                default:
                    break;
            } 
        }
    }
}
/* EJEMPLO DE USO CODIGO GENERADO POR IA
class Reserva {
    private Pasajero cliente;
    private List<Habitacion> habitaciones;
    private int diasEstadia;
    private boolean checkInRealizado;

    public Reserva(Pasajero cliente, int diasEstadia) {
        this.cliente = cliente;
        this.diasEstadia = diasEstadia;
        this.habitaciones = new ArrayList<>();
        this.checkInRealizado = false;
    }

    public void agregarHabitacion(Habitacion h) {
        this.habitaciones.add(h);
    }
    
    public void realizarCheckIn() {
        this.checkInRealizado = true;
        System.out.println("Pulseras digitales entregadas. Check-in exitoso.");
    }

    public int calcularCostoTotal() {
        int total = 0;
        for(Habitacion h : habitaciones) {
            total = h.getPrecioPorNoche() * diasEstadia
        }
        return total;
    }
}
*/