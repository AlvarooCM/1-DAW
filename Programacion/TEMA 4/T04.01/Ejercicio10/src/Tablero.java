/* Alvaro Camino Martinez */

public class Tablero {
    private int[][] tablero;

    public Tablero() {
        this.tablero = new int[3][3]; // Crear tablero de 3x3
    }

    public void mostrarTablero() {
        System.out.println(" C1 C2 C3");
        for (int i = 0; i < 3; i++) {
            System.out.print("F" + i + " ");
            for (int j = 0; j < 3; j++) {
                if (tablero[i][j] == 0) {
                    System.out.print("- "); // Espacio vacío
                } else if (tablero[i][j] == 1) {
                    System.out.print("X "); // Jugador 1
                } else {
                    System.out.print("O "); // Jugador 2
                }
            }
            System.out.println();
        }
    }

    public boolean realizarMovimiento(int fila, int columna, int jugadorActivo) {
        if (fila < 0 || fila > 2 || columna < 0 || columna > 2 || tablero[fila][columna] != 0) {
            return false; // Movimiento inválido
        }
        tablero[fila][columna] = jugadorActivo; // Realizar el movimiento
        return true;
    }

    public boolean verificarGanador(int jugadorActivo) {
        // Verificar filas y columnas
        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] == jugadorActivo && tablero[i][1] == jugadorActivo && tablero[i][2] == jugadorActivo) {
                return true;
            }
            if (tablero[0][i] == jugadorActivo && tablero[1][i] == jugadorActivo && tablero[2][i] == jugadorActivo) {
                return true;
            }
        }

        // Verificar diagonales
        if (tablero[0][0] == jugadorActivo && tablero[1][1] == jugadorActivo && tablero[2][2] == jugadorActivo) {
            return true;
        }
        if (tablero[0][2] == jugadorActivo && tablero[1][1] == jugadorActivo && tablero[2][0] == jugadorActivo) {
            return true;
        }

        return false;
    }

    public boolean verificarEmpate() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tablero[i][j] == 0) {
                    return false; // No está lleno
                }
            }
        }
        return true; // El tablero está lleno
    }
}

