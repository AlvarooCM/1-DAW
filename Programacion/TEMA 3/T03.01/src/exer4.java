/**
 *  Pide pon pantalla unha cantidade de tempo en segundos. Imprime por pantalla as súas correspondentes horas, minutos e segundos do valor introducido nesta orde e cada un nunha liña.
 */

 import java.util.Scanner;

 public class exer4 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca la cantidad de tiempo en segundo que quiere transformar:");
        double tiempo = scanner.nextDouble();

        double horas = tiempo /3600;

        double minutos = tiempo /60;

        double segundos = tiempo;

        System.out.println("El tiempo en horas es de " + horas);
        System.out.println("El tiempo en minutos es de " + minutos);
        System.out.println("El tiempo en segundos es de " + segundos);
    }

 }

 