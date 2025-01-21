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

        //* Pido numero de estudiantes. */

        System.out.println("Introduzca el numero de estudiantes del curso: ");
        int estudiantes = scanner.nextInt();

        //* Pido numero de modulos */

        System.out.println("Introduzca el numero de modulos del curso: ");
        int modulos = scanner.nextInt();

        //* Creo una matriz para guardar las notas y la voy a llamar curso. */

        double[][] curso  = new double[estudiantes][modulos];

        for(int i = 0; i < estudiantes; i++){
            for (int j = 0; j < modulos; j++){
                System.out.println("Dato ["+ i +"] ["+ j +"]");
            }
        }
        
        while (true) {

            System.out.println("Menu:");

            System.out.println("a) Media dun alumno/a");

            System.out.println("b) Porcentaxe de alumnos aprobados");

            System.out.println("Ingrese la opcion a escoger:");

            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    
                    break;
            
                default:
                    break;
            }

        }


            


    }
}
