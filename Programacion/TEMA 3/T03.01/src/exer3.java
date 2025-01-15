/**
 * Queremos calcular o prezo dunha compra dunha froitería. Primeiro pediremos por pantalla os quilogramos comprados de mazás e despois os quilogramos de laranxas. Imprimirase por pantalla o importe a pagar. Os prezos das froitas son as seguintes:

Mazás: 3,5 €/kg
Laranxas: 1,6€/kg
 */

import java.util.Scanner;

public class exer3 {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca los quilogramos comprados de manzanas: ");
        double kgManzanas = scanner.nextDouble();

        System.out.println("Introduzca los quilogramos comprados de naranjas: ");
        double kgNaranjas = scanner.nextDouble();

        double pagarManzanas = kgManzanas * 3.5;

        double pagarNaranjas = kgNaranjas * 3.5;

        System.out.println("El precio a pagar por las manzanas es de: " + pagarManzanas);

        System.out.println("El precio a pagar por las naranja es de: " + pagarNaranjas);
    }
    
}
