import java.time.LocalDate;

public class Disco {
    
    private String titulo;
    private String grupo;
    private int anoLanzamento;
    private int numCancions;

    public Disco(String titulo, String grupo, int anoLanzamento, int numCancions) {
        this.titulo = titulo;
        this.grupo = grupo;
        this.anoLanzamento = anoLanzamento;
        this.numCancions = numCancions;
    }

    public int getAnosExistencia(){
        LocalDate agora = LocalDate.now();
        return agora.getYear() - this.anoLanzamento;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getGrupo() {
        return grupo;
    }

    public void setGrupo(String grupo) {
        this.grupo = grupo;
    }

    public int getAnoLanzamento() {
        return anoLanzamento;
    }

    public void setAnoLanzamento(int anoLanzamento) {
        this.anoLanzamento = anoLanzamento;
    }

    public int getNumCancions() {
        return numCancions;
    }

    public void setNumCancions(int numCancions) {
        this.numCancions = numCancions;
    }
}
