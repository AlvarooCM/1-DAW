import java.util.*;

class Pregunta {
    String enunciado;
    List<String> respuestas;
    Map<String, Integer> conteoRespuestas;

    public Pregunta(String enunciado) {
        this.enunciado = enunciado;
        this.respuestas = new ArrayList<>();
        this.conteoRespuestas = new HashMap<>();
    }

    public void agregarRespuesta(String respuesta) {
        respuestas.add(respuesta);
        conteoRespuestas.put(respuesta, 0);
    }

    public void responder(String respuesta) {
        if (conteoRespuestas.containsKey(respuesta)) {
            conteoRespuestas.put(respuesta, conteoRespuestas.get(respuesta) + 1);
        }
    }

    public void mostrarResultados() {
        System.out.println(enunciado);
        int totalRespuestas = conteoRespuestas.values().stream().mapToInt(Integer::intValue).sum();
        for (String respuesta : respuestas) {
            int conteo = conteoRespuestas.get(respuesta);
            double porcentaje = totalRespuestas == 0 ? 0 : (conteo * 100.0 / totalRespuestas);
            System.out.printf(respuesta, porcentaje, conteo);
        }
    }
}

public class Encuesta {
    static List<Pregunta> preguntas = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // Datos de prueba
        Pregunta p1 = new Pregunta("¿Cuál es tu lenguaje de programación favorito?");
        p1.agregarRespuesta("Java");
        p1.agregarRespuesta("Python");
        p1.agregarRespuesta("C++");
        preguntas.add(p1);

        Pregunta p2 = new Pregunta("¿Prefieres frontend o backend?");
        p2.agregarRespuesta("Frontend");
        p2.agregarRespuesta("Backend");
        p2.agregarRespuesta("Fullstack");
        preguntas.add(p2);

        menu();
    }

    public static void menu() {
        while (true) {
            System.out.println("\nMenú de Encuestas");
            System.out.println("a) Engadir pregunta");
            System.out.println("b) Responder cuestionario");
            System.out.println("c) Mostrar resultados");
            System.out.println("d) Salir");
            System.out.print("Opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "a":
                    agregarPregunta();
                    break;
                case "b":
                    responderCuestionario();
                    break;
                case "c":
                    mostrarResultados();
                    break;
                case "d":
                    System.out.println("Saliendo...");
                    return;
                default:
                    System.out.println("Opción inválida, intenta de nuevo.");
            }
        }
    }

    public static void agregarPregunta() {
        System.out.print("Introduce la pregunta: ");
        String enunciado = scanner.nextLine();
        Pregunta pregunta = new Pregunta(enunciado);

        while (pregunta.respuestas.size() < 2 || confirmar("¿Quieres agregar otra respuesta? (s/n) ")) {
            System.out.print("Introduce una respuesta: ");
            String respuesta = scanner.nextLine();
            pregunta.agregarRespuesta(respuesta);
        }
        preguntas.add(pregunta);
        System.out.println("Pregunta añadida con éxito!");
    }

    public static void responderCuestionario() {
        for (Pregunta pregunta : preguntas) {
            System.out.println(pregunta.enunciado);
            for (int i = 0; i < pregunta.respuestas.size(); i++) {
                System.out.println((i + 1) + ") " + pregunta.respuestas.get(i));
            }
            System.out.print("Selecciona una opción: ");
            int seleccion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea
            if (seleccion > 0 && seleccion <= pregunta.respuestas.size()) {
                pregunta.responder(pregunta.respuestas.get(seleccion - 1));
            } else {
                System.out.println("Selección inválida");
            }
        }
    }

    public static void mostrarResultados() {
        for (Pregunta pregunta : preguntas) {
            pregunta.mostrarResultados();
        }
    }

    public static boolean confirmar(String mensaje) {
        System.out.print(mensaje);
        String respuesta = scanner.nextLine().toLowerCase();
        return respuesta.equals("s");
    }
}