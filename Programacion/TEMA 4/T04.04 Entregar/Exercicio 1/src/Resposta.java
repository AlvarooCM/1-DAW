public class Resposta {
    
    private String texto;
    private int contador;

    // Constructor
    public Resposta(String texto) {
        this.texto = texto;
        this.contador = 0;
    }

    // Getter para o texto
    public String getTexto() {
        return texto;
    }

    // Incrementar o contador cando se selecciona a resposta
    public void incrementarContador() {
        contador++;
    }

    // Getter para o contador
    public int getContador() {
        return contador;
    }
}

