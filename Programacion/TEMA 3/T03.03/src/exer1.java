//Alvaro Camino Martinez

/**
 * Exercicio 1. O matemático indio Ramchandra Kaprekar descubriu en 1949 unha curiosa característica do número 6174. Este número coñécese como constante de Kaprekar na súa honra.

Este número ten a seguinte propiedade:

Elixe un número de catro díxitos que teña polo menos dous diferentes (é valido colocar o díxito 0 ao principio, polo que o número 0009 é válido).

Coloca os seus díxitos en orde ascendente e en orde descendente para formar dous novos números. Podes engadir os díxitos 0 que necesites ao principio.

Resta o menor ao maior.

Volve ao paso 2.

Este proceso coñécese como a rutina Kaprekar, e sempre chegará ao número 6174 en coma moito 7 iteracións. Unha vez que o resultado da operación do paso 3 de ese número, o proceso parará.

Por exemplo, o número 3542 alcanzará a constante de Kaprekar en 3 iteracións:

5432 − 2345 = 3087
8730 − 0378 = 8352
8532 − 2358 = 6174
Os únicos díxitos de catro cifras para os que a rutina non alcanza este número son os repdigits, é dicir, aqueles nas que as súas catro cifras son iguais (como 1111), pois na primeira iteración alcanzarase o valor 0 e xa non se pode saír del. Por iso se pide no paso 1 explicitamente que o número inicial tivera polo menos dous díxitos diferentes.

Aquí tes dous exemplos máis:

2111 − 1112 = 0999
9990 − 0999 = 8991
9981 − 1899 = 8082
8820 − 0288 = 8532
8532 − 2358 = 6174


9831 − 1389 = 8442
8442 − 2448 = 5994
9954 − 4599 = 5355
5553 − 3555 = 1998
9981 − 1899 = 8082
8820 − 0288 = 8532
8532 − 2358 = 6174

Pídese un programa que reciba un número e indique o número de iteracións necesarias para calcular a constante de Kaprekar. Para os números repdigits deberase indicar -1, e se se introduce a constante de Kaprekar deberase indicar o número 0.
 */

import java.util.Scanner;

public class exer1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Pedimos un numero de 4 cifras

        System.out.println("Introduzca un numero de 4 cifras: ");
        int numero = scanner.nextInt();

        //Comprobamos que el numero tenga 4 cifras

        if (numero < 1000 || numero > 9999){
            System.out.println("El número debe tener exactamente 4 cifras.");
            return;
        }

        if (numero == 6174){
            System.out.println("El número 6174 ya es la constante de Kaprekar.");
            return;
        }

        int digito1 = numero / 1000;
        int digito2 = (numero % 1000) / 100;
        int digito3 = (numero % 100) / 10;
        int digito4 = numero % 10;
        
        if (digito1 == digito2 && digito2 == digito3 && digito3 == digito4){
            System.out.println("El número no puede tener todos los dígitos iguales.");
            return;
        }

        //Creacion del contador de iteraciones y del array digitos

        int iteraciones = 0;

        while (numero != 6174 ) {
            int[] digitos = {digito1, digito2, digito3, digito4};

            //Metedo burbulla de ordenacion dos digitss

            for (int i = 0; i < digitos.length - 1; i++) {
                for (int j = i + 1; j < digitos.length; j++) {

                    if (digitos[i] > digitos[j]) {
                        int aux = digitos[i];
                        digitos[i] = digitos[j];
                        digitos[j] = aux;
                    }
                }
            }

            // Calculamos el número ascendente y descendente

            int ascendente = digitos[0] * 1000 + digitos[1] * 100 + digitos[2] * 10 + digitos[3];

            int descendente = digitos[3] * 1000 + digitos[2] * 100 + digitos[1] * 10 + digitos[0];

            numero = descendente - ascendente;

            digito1 = numero / 1000;
            digito2 = (numero % 1000) / 100;
            digito3 = (numero % 100) / 10;
            digito4 = numero % 10;

            iteraciones++;
        }

        System.out.println("El número de iteraciones necesarias para llegar a la constante de Kaprekar es: " + iteraciones);
    }             
}
        


            

        

        
