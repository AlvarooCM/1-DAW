/**
 * Exercicio 4. Deséxase xestionar as notas de estudantes dun curso mediante matrices en Java. O exercicio consiste en almacenar as notas de varios estudantes en diferentes módulos.

Primeiro indicaranse o número de estudantes.

A continuación indicarase o número de módulos.

A continuación engadiranse as notas de cada estudante módulo a módulo.

Unha vez introducidos as notas do alumnado mostrarase o seguinte menú utilizando a estrutura switch:

a) Media dun alumno/a: pedirase o índice do alumno e calcularase a media das súas notas.

b) Porcentaxe de aprobados: calcularase a porcentaxe de aprobados do módulo do que se introduza o índice.
 */

import java.util.Scanner;

public class exer4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca el numero de estudiantes del curso: ");
        int estudiantes = scanner.nextInt();

        System.out.println("Introduzca el numero de modulos del curso: ");
        int modulos = scanner.nextInt();

        System.out.println("Introduzca las notas de cada alumno en cada 1 de los modulos: ");
        int notas = scanner.nextInt();

        int [][][] curso  = new int[estudiantes][modulos][notas];

        for(int c = 0; c < curso.length; c++){
            for(int f = 0; f < curso [c].length; f++){
                for(int p = 0; p < curso [f].length; p++){

                    System.out.println("Introduzca los valores de las columnas " + c + "fila" + f + "profundidad" + p + " :");

                    int valor = scanner.nextInt();
                    curso[c][f][p] = valor;
                }
            }
        }

        while (true) {

            
            
        }






    }
}
