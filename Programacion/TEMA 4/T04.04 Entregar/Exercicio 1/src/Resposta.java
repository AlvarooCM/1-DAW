import java.util.Scanner;

public class Resposta {
    private String texto; // Texto de la respuesta
    private int contador; // Contador de cuántas veces se ha seleccionado la respuesta

    // Constructor de la clase Resposta
    public Resposta(String texto) {
        this.texto = texto;
        this.contador = 0; // Inicializa el contador a 0
    }

    // Método para incrementar el contador cuando la respuesta es seleccionada
    public void incrementarContador() {
        contador++;
    }

    // Getter para obtener el texto de la respuesta
    public String getTexto() {
        return texto;
    }

    // Getter para obtener el contador de la respuesta
    public int getContador() {
        return contador;
    }

    // Método estático que permite al usuario responder un cuestionario
    public static void responderCuestionario(Pregunta pregunta) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\n" + pregunta.getTexto()); // Muestra el texto de la pregunta
        pregunta.mostrarRespostas(); // Muestra las respuestas disponibles
        
        int opcion;
        do {
            System.out.print("Selecciona unha resposta (1-" + pregunta.getRespostas().size() + "): ");
            // Asegura que la entrada sea un número entero válido
            while (!scanner.hasNextInt()) {
                System.out.print("Por favor, introduce un número válido: ");
                scanner.next(); // Descarta la entrada no válida
            }
            opcion = scanner.nextInt(); // Lee la opción seleccionada por el usuario
        } while (opcion < 1 || opcion > pregunta.getRespostas().size()); // Verifica que la opción esté en el rango válido
        
        // Incrementa el contador de la respuesta seleccionada
        pregunta.getRespostas().get(opcion - 1).incrementarContador();
        System.out.println("Resposta gardada \n"); // Confirmación de que la respuesta fue registrada
    }
}



