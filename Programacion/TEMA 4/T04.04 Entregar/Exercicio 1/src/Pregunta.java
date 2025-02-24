import java.util.ArrayList;
import java.util.List;

public class Pregunta {
    private String texto;
    private List<Resposta> respostas;

    // Constructor
    public Pregunta(String texto) {
        this.texto = texto;
        this.respostas = new ArrayList<>();
    }

    // Engadir unha resposta á pregunta
    public void engadirResposta(Resposta resposta) {
        respostas.add(resposta);
    }

    // Mostrar as respostas posibles
    public void mostrarRespostas() {
        for (int i = 0; i < respostas.size(); i++) {
            System.out.println((i + 1) + ". " + respostas.get(i).getTexto());
        }
    }

    // Mostrar resultados (porcentaxes)
    public void mostrarResultados() {
        int totalRespostas = respostas.stream().mapToInt(Resposta::getContador).sum();
        for (Resposta resposta : respostas) {
            double porcentaxe = (totalRespostas > 0) ? (resposta.getContador() * 100.0 / totalRespostas) : 0;
            System.out.printf("%s: %.2f%%\n", resposta.getTexto(), porcentaxe);
        }
    }

    // Getter para o texto da pregunta
    public String getTexto() {
        return texto;
    }

    // Getter para as respostas
    public List<Resposta> getRespostas() {
        return respostas;
    }

    public void add(Pregunta pregunta) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'add'");
    }
}
