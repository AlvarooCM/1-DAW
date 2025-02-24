// Clase Main.java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    private List<Pregunta> pregunta;

    // Constructor
    public App() {
        pregunta = new ArrayList<>();
    }

    // Engadir pregunta
    public void engadirPregunta() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce a pregunta: ");
        String textoPregunta = scanner.nextLine();

        Pregunta pregunta = new Pregunta(textoPregunta);

        while (true) {
            System.out.print("Introduce unha resposta posible: ");
            String textoResposta = scanner.nextLine();

            Resposta resposta = new Resposta(textoResposta);
            pregunta.engadirResposta(resposta);

            System.out.print("Queres engadir outra resposta? (s/n): ");
            String engadirMais = scanner.nextLine();

            if (!engadirMais.equalsIgnoreCase("s")) {
                break;
            }
        }

        pregunta.add(pregunta);
    }

    // Responder cuestionario
    public void responderCuestionario() {
        Scanner scanner = new Scanner(System.in);

        for (Pregunta pregunta : pregunta) {
            System.out.println("\nPregunta: " + pregunta.getTexto());
            pregunta.mostrarRespostas();

            while (true) {
                try {
                    System.out.print("Elixe unha resposta (1-" + pregunta.getRespostas().size() + "): ");
                    int seleccion = Integer.parseInt(scanner.nextLine());

                    if (seleccion >= 1 && seleccion <= pregunta.getRespostas().size()) {
                        pregunta.getRespostas().get(seleccion - 1).incrementarContador();
                        break;
                    } else {
                        System.out.println("Elixe un número válido.");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Por favor, introduce un número válido.");
                }
            }
        }
    }

    // Mostrar resultados
    public void mostrarResultados() {
        for (Pregunta pregunta : pregunta) {
            System.out.println("\nPregunta: " + pregunta.getTexto());
            pregunta.mostrarResultados();
        }
    }

    // Menú principal
    public void menu() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nMenú:");
            System.out.println("a) Engadir pregunta");
            System.out.println("b) Responder cuestionario");
            System.out.println("c) Mostrar resultados");
            System.out.println("d) Saír");

            System.out.print("Elixe unha opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "a":
                    engadirPregunta();
                    break;
                case "b":
                    responderCuestionario();
                    break;
                case "c":
                    mostrarResultados();
                    break;
                case "d":
                    System.out.println("Saíndo do programa...");
                    return;
                default:
                    System.out.println("Opción non válida, por favor elixe de novo.");
                    break;
            }
        }
    }

    public static void main(String[] args) {
        App app = new App();
        app.menu();
    }
}
