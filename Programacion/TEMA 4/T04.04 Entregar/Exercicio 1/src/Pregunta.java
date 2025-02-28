import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Pregunta {
    private String texto; // Texto de la pregunta
    private List<Resposta> respostas; // Lista de respuestas

    // Constructor de la clase Pregunta
    public Pregunta(String texto) {
        this.texto = texto;
        this.respostas = new ArrayList<>();
    }

    // Método para añadir una respuesta
    public void engadirResposta(Resposta resposta) {
        respostas.add(resposta);
    }

    // Método para mostrar las respuestas disponibles
    public void mostrarRespostas() {
        for (int i = 0; i < respostas.size(); i++) {
            System.out.println((i + 1) + ". " + respostas.get(i).getTexto());
        }
    }

    // Método estático para crear una nueva pregunta
    public static Pregunta crearPregunta() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduce a pregunta: "); // Solicita la pregunta
        String textoPregunta = scanner.nextLine(); 
        Pregunta pregunta = new Pregunta(textoPregunta); // Crea el objeto Pregunta

        // Permite añadir respuestas mientras se quiera y haya al menos dos respuestas
        while (pregunta.respostas.size() < 2 || continuarEngadindo(scanner)) {
            System.out.print("Introduce unha resposta: "); // Solicita la respuesta
            String textoResposta = scanner.nextLine();
            pregunta.engadirResposta(new Resposta(textoResposta)); // Añade la respuesta
        }
        
        return pregunta; // Devuelve la pregunta con las respuestas añadidas
    }

    // Método que pregunta al usuario si quiere seguir añadiendo respuestas
    private static boolean continuarEngadindo(Scanner scanner) {
        System.out.print("Queres engadir outra resposta? (s/n): ");
        String resposta = scanner.nextLine().trim().toLowerCase();
        return resposta.equals("s"); // Si la respuesta es 's', continúa
    }

    // Getter para el texto de la pregunta
    public String getTexto() {
        return texto;
    }

    // Getter para la lista de respuestas
    public List<Resposta> getRespostas() {
        return respostas;
    }
}


