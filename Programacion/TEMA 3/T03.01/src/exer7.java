/**
 * Pide un número por consola e imprime por pantalla Primo se este é un número primo, e Non primo en caso contrario.
 */

import java.util.Scanner;

public class exer7 {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca un numero:");
        int numero = scanner.nextInt();

        boolean primos = true; 
        for(int i = 2; i < numero; i++) {
        if (numero % i == 0) {
            primos = false;
            break;
            }
        }
        if (primos)
        System.out.println(numero + " es primo");
        else
        System.out.println(numero + " no es primo");
    }
    
}
