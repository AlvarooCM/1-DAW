/**
 * Exercicio 5. Implanta un xogo de Tres en Raia en Java utilizando arrays bidimensionais para representar o taboleiro de xogo. O programa debe permitir que dous xogadores humanos xoguen entre eles alternando quendas ata que un deles consiga gañar ou que o taboleiro quede completo, resultando nun empate.

Utiliza un vector bidimensional 3x3 de enteiros para representar o taboleiro.

Inicialmente, cada posición do taboleiro debe estar baleira, representada cun 0 no vector.

Alterna entre os dous xogadores, representados polos números 1 e 2.

Amosa o taboleiro despois de cada movemento. Os espazos baleiros represéntaos con - e os xogadores con X para o xogador 1 e O para o xogador 2.

Verifica e amosa unha mensaxe cando un xogador gaña ou se hai un empate se se encheron todos os ocos.

Exemplo de taboleiro baleiro (Separa con tabuladores os diferentes partes do taboleiro):

   C1 C2 C3
F0 -  -  -
F1 -  -  -
F2 -  -  -

Exemplo despois dalgúns movementos:

   C1 C2 C3
F0 X  -  X
F1 -  O  O
F2 -  -  -
 */

import java.util.Scanner;

public class exer5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        /* Defino el tablero de juego */

        int [][] tablero = new int [3][3];

        /* Variables de control del juego */

        boolean juegoActivado = true;
        int jugadorActivo = 1;

        while (juegoActivado){

            System.out.println(" C1 C2 C3");
            for (int i = 0; i < 3; i++) {
                System.out.println("F" + i + " ");
                for (int j = 0; j < 3; j++) {
                    if (tablero[i][j] == 0) {
                        System.out.println("- ");
                    } else if (tablero[i][j] == 1){
                        System.out.println("X ");
                    } else {
                        System.out.println("O ");
                    }
                }
                System.out.println();
            }
        }

        System.out.println("Turno del jugador " + jugadorActivo + " (" + (jugadorActivo == 1 ? "X" : "O") + ")");

        System.out.print("Introduce fila (0-2)");

        int fila = scanner.nextInt();

        System.out.print("Introduce columna (0-2)");

        int columna = scanner.nextInt();

        if (fila < 0 || fila > 2 || columna < 0 || columna > 2 || tablero [fila][columna] != 0) {
            System.out.println("Movimiento invalido. Intentelo de nuevo");
            continue;
        }

        tablero [fila] [columna] = jugadorActivo;
        




    }
}