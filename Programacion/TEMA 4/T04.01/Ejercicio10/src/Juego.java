/* Alvaro Camino Martinez */

import java.util.Scanner;

public class Juego {
    private Tablero tablero;
    private Jugador jugador1;
    private Jugador jugador2;
    private Jugador jugadorActivo;
    private boolean juegoActivado;

    public Juego() {
        this.tablero = new Tablero();
        this.jugador1 = new Jugador(1, "X");
        this.jugador2 = new Jugador(2, "O");
        this.jugadorActivo = jugador1; // Comienza el jugador 1
        this.juegoActivado = true;
    }

    public void jugar() {
        Scanner scanner = new Scanner(System.in);

        while (juegoActivado) {
            tablero.mostrarTablero();

            // Solicitar el movimiento
            System.out.println("Turno del jugador " + jugadorActivo.getNumero() + " (" + jugadorActivo.getSimbolo() + ")");
            System.out.print("Introduce fila (0-2): ");
            int fila = scanner.nextInt();
            System.out.print("Introduce columna (0-2): ");
            int columna = scanner.nextInt();

            // Realizar movimiento
            if (!tablero.realizarMovimiento(fila, columna, jugadorActivo.getNumero())) {
                System.out.println("Movimiento invalido. Intentelo de nuevo");
                continue; // Intentar nuevamente si el movimiento es invalido
            }

            // Verificar si hay un ganador
            if (tablero.verificarGanador(jugadorActivo.getNumero())) {
                tablero.mostrarTablero();
                System.out.println("El jugador " + jugadorActivo.getNumero() + " (" + jugadorActivo.getSimbolo() + ") ha ganado!");
                juegoActivado = false;
                break;
            }

            // Verificar si hay empate
            if (tablero.verificarEmpate()) {
                tablero.mostrarTablero();
                System.out.println("Empate! El tablero está completo.");
                juegoActivado = false;
                break;
            }

            // Cambiar al siguiente jugador
            jugadorActivo = (jugadorActivo == jugador1) ? jugador2 : jugador1;
        }

        scanner.close();
    }

    public static void main(String[] args) {
        Juego juego = new Juego();
        juego.jugar();
    }
}
