package lab_verdadero.java;

public class Laguna {
    private Rana[] piedras;
    private Jugador jugador;

    public Laguna(Jugador jugador) {
        this.jugador = jugador;
        this.piedras = new Rana[7];
        inicializarLaguna();
    }

    private void inicializarLaguna() {
        for (int i = 0; i < 3; i++) piedras[i] = new Rana("verde", 1);
        piedras[3] = null; 
        for (int i = 4; i < 7; i++) piedras[i] = new Rana("roja", -1);
    }

    // Muestra estado y posición de las ranas
    public void mostrarEstado() {
        System.out.println("\n--- estado ---");
        for (Rana piedra : piedras) {
            if (piedra == null) {
                System.out.print("[ _ ] ");
            } else {
                System.out.print("[ " + piedra.toString() + " ] ");
            }
        }
        System.out.println("\n  0     1     2     3     4     5     6");
    }

    // Implementación de restricciones de movimiento
    public boolean moverRana(int posicion) {
        if (posicion < 0 || posicion >= 7 || piedras[posicion] == null) {
            System.out.println("Error: Selección inválida.");
            return false;
        }

        Rana ranaActual = piedras[posicion];
        int dir = ranaActual.getDireccion();
        int saltoSimple = posicion + dir;
        int saltoDoble = posicion + (dir * 2);

        // Validar salto simple a piedra vacía
        if (saltoSimple >= 0 && saltoSimple < 7 && piedras[saltoSimple] == null) {
            piedras[saltoSimple] = ranaActual;
            piedras[posicion] = null;
            return true;
        }
        // Validar salto doble sobre otra rana a piedra vacía
        else if (saltoDoble >= 0 && saltoDoble < 7 && piedras[saltoDoble] == null && piedras[saltoSimple] != null) {
            piedras[saltoDoble] = ranaActual;
            piedras[posicion] = null;
            return true;
        }

        System.out.println("Movimiento inválido: Esa rana está bloqueada y no puede saltar.");
        return false;
    }

    // Verifica si se alcanzó el estado final
    public boolean verificarVictoria() {
        for (int i = 0; i < 3; i++) {
            if (piedras[i] == null || !piedras[i].getColor().equals("roja")) return false;
        }
        if (piedras[3] != null) return false;
        
        for (int i = 4; i < 7; i++) {
            if (piedras[i] == null || !piedras[i].getColor().equals("verde")) return false;
        }
        return true; // Estado final alcanzado
    }

    // Verifica si ya no hay espacio para un nuevo movimiento válido
    public boolean hayMovimientosPosibles() {
        for (int i = 0; i < piedras.length; i++) {
            if (piedras[i] != null) {
                int dir = piedras[i].getDireccion();
                int saltoSimple = i + dir;
                int saltoDoble = i + (dir * 2);

                if (saltoSimple >= 0 && saltoSimple < 7 && piedras[saltoSimple] == null) return true;
                if (saltoDoble >= 0 && saltoDoble < 7 && piedras[saltoDoble] == null && piedras[saltoSimple] != null) return true;
            }
        }
        return false;
    }
}