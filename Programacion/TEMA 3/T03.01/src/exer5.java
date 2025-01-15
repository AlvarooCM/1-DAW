/**
 * Pedir 3 números por pantalla e imprimir en orde de maior a menor.
 */

import java.util.Scanner;

public class exer5 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca un numero:");
        int numero1 = scanner.nextInt();

        System.out.println("Introduzca otro numero:");
        int numero2 = scanner.nextInt();

        System.out.println("Introduzca otro numero:");
        int numero3 = scanner.nextInt();

        if (numero1 > numero2 && numero1 > numero3){

            System.out.println(numero1);
        }
        else if (numero2 > numero1 && numero2 > numero3){

            System.out.println(numero2);
        }
        else {
            System.out.println(numero3);
        }

    }
    
}
