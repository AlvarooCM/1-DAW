/**
 * Exercicio 2. Inicializa nunha aplicación un vector cos seguintes elementos nesta orde: 3, 5 ,7, 2 e 9. Iráselle pedindo ao usuario o índice do elemento a borrar, ata que non queden máis. No momento do borrado, mostrarase o elemento borrado por pantalla. Despois de eliminar o último, imprimirase ademais Fin. Se o índice introducido non existe imprimirase Erro. Cada vez que se elimina un elemento o vector deberá reducir o seu tamaño para axustarse.
 */

import java.util.Scanner;

public class exer2 {
    public static void main(String[] args) {

        // Inicializamos la entrada de datos
        Scanner scanner = new Scanner(System.in);

        // Inicializamos el vector
        int[] datos = {3,5,7,2,9};

        // El while se ejecutará mientras que el tamaño del vector sea mayor que 0
        while (datos.length > 0){
        }
            System.out.println("Introduzca o indice a eliminar: ");
            int indice = scanner.nextInt();

        if (indice < datos.length && indice >= 0){

                System.out.println(datos[indice]);
            }
        
        int [] datosnuevos = new int [datos.length - 1];

        int x = 0;

        for (int i=0; i < datos.length; i++){

            if (i !=indice){
                datosnuevos[x] = datos[i];
                x++;
            }
        }
            datos = datosnuevos;
            }
            else{
                System.out.println("Error");

            }
    scanner.close();
}
