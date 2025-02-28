import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CuestionarioApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Pregunta> preguntas = new ArrayList<>();
        boolean salir = false;

        while (!salir) {
            // Menú de opciones
            System.out.println("\n Menú :");
            System.out.println("a) Engadir pregunta");
            System.out.println("b) Responder cuestionario");
            System.out.println("c) Mostrar resultados");
            System.out.println("d) Salir");
            System.out.print("Selecciona unha opción : ");
            String opcion = scanner.nextLine().trim().toLowerCase();

            switch (opcion) {
                case "a":
                    // Añadir preguntaa
                    boolean agregarMas;
                    do {
                        Pregunta pregunta = Pregunta.crearPregunta();
                        preguntas.add(pregunta);
                        System.out.print("Queres engadir outra pregunta? (s/n): ");
                        agregarMas = scanner.nextLine().trim().equalsIgnoreCase("s");
                    } while (agregarMas);
                    break;

                case "b":
                    // Responder cuestionario
                    System.out.println("\n Responder Cuestionario :");
                    for (Pregunta pregunta : preguntas) {
                        Resposta.responderCuestionario(pregunta);
                    }
                    break;

                case "c":
                    // Mostrar resultados
                    System.out.println("\n Resultados :");
                    for (Pregunta pregunta : preguntas) {
                        System.out.println("\n" + pregunta.getTexto());
                        int totalRespostas = pregunta.getRespostas().stream().mapToInt(Resposta::getContador).sum();
                        for (Resposta resposta : pregunta.getRespostas()) {
                            double porcentaxe = (totalRespostas > 0) ? (resposta.getContador() * 100.0 / totalRespostas) : 0;
                            System.out.printf("%s: %.2f%%\n", resposta.getTexto(), porcentaxe);
                        }
                    }
                    break;

                case "d":
                    // Salir del programa
                    salir = true;
                    break;

                default:
                    System.out.println("Opción non válida. Por favor, intenta de novo.");
                    break;
            }
        }

        scanner.close();
    }
}

