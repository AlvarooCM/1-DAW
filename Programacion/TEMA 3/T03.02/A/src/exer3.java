/**
 * Exercicio 3. Crea o seguinte programa:

Crea unha matriz bidimensional. O usuario introducirá o número de columnas e filas nesa orde.

A continuación introducirá os valores columna a columna.

Calcula o valor da suma de cada columna. Imprime eses valores en orde con System.out.println en orde.

Calcula o valor da suma de cada fila. Imprime eses valores en orde con System.out.println en orde.
 */

 import java.util.Scanner;

 public class exer3 {
     public static void main(String[] args) {
 
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca o numero de columnas da matriz: ");
        int columnas = scanner.nextInt(); 

        System.out.println("Introduzca o numero de columnas da matriz: ");
        int filas = scanner.nextInt();

        int [][] matriz = new int[columnas][filas];

        for(int c = 0; c < matriz.length; c++){
             
            for(int f = 0; f < matriz [c].length; f++){

                System.out.println("Introduzca el valor da columna " + c + " e fila " + f + " :");
                
                int valor = scanner.nextInt();
                matriz[c][f] = valor;
            }
        }
        for (int c = 0; c < matriz.length; c++){

            int suma = 0;

            for (int f = 0; f < matriz [c].length; f++){
                suma = suma + matriz[c][f];
            }
            System.out.println(suma);
        }

        int [] sumaFilas = new int [filas];

        for(int c=0; c < matriz.length; c++){

            for(int f = 0; f < matriz [c].length; f++){
                sumaFilas [f] = sumaFilas [f] + matriz [c] [f];
            }
        }

        for(int suma: sumaFilas){
            System.out.println(suma);
        }

        scanner.close();
    }
}