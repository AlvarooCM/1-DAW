/**
 * Exercicio 1. Escribe unha aplicación que solicite ao usuario a cantidade de números que desexa introducir. A continuación introducirase por teclado esa cantidade de números decimais. Por último imprime os números introducidos en orde inversa. Debes imprimir un por liña.
 */

import java.util.Scanner;

public class exer1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca la cantidad de numero que desee: ");
        int cantidadNumeros = scanner.nextInt();

        int[] numeros = new int[cantidadNumeros];

        for(int i = 0; i < numeros.length; i++){
            System.out.println(numeros[i]);
        }
    }
    
}
