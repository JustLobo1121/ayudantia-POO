package lab_verdadero.java;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese el nombre del jugador para comenzar: ");
        String nombre = scanner.nextLine();
        Jugador jugador = new Jugador(nombre);
        Laguna laguna = new Laguna(jugador);

        System.out.println("\n¡Comienza, " + jugador.getNombre() + "!");
        
        while (true) {
            laguna.mostrarEstado();

            if (laguna.verificarVictoria()) {
                System.out.println("\n¡Felicidades! Has resuelto el acertijo.");
                break;
            }

            if (!laguna.hayMovimientosPosibles()) {
                System.out.println("\nJuego terminado: Te has bloqueado y no hay más movimientos posibles.");
                break;
            }

            System.out.print("\nIngresa el número de la piedra (0-6) de la rana que deseas mover: ");
            int posicion = scanner.nextInt();
            laguna.moverRana(posicion);
        }
        
        scanner.close();
    }
}