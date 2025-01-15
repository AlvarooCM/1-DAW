import java.util.Scanner;

/**
 * Pide por pantalla a idade dunha persoa e mostra por pantalla o ano no que naceu. Considera o ano actual 2025.
 */

public class exer2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca su edad:");

        int añoActual = 2025;

        int numero = scanner.nextInt();

        int añoNacimiento = añoActual - numero;

        System.out.println(añoNacimiento);    
    }
}
