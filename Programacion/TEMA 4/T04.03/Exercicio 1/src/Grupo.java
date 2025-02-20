// Exercicio 1. Segue os seguintes pasos:

// Crea a clase Grupo coas seguintes características:

// Desexase almacenar para cada grupo o seu nome, país e ano de creación.

// Crea getters e setters necesarios

// Crea unha construtor para inicializar tódolos atributos. Os valores destes pásanse por parámetros.

// Documenta os construtores.

// Crea o método int getIdade() que devolva os anos do grupo. Obtén o ano actual.

// Documenta os métodos.

import java.time.LocalDate;

public class Grupo {

    private String nome;
    private String pais;
    private int anoCreacion;

    public Grupo(String nome, String pais, int anoCreacion) {
        
        this.nome = nome;
        this.pais = pais;
        this.anoCreacion = anoCreacion;

    }

    public int getIdade() {
        LocalDate agora = LocalDate.now();
        return agora.getYear() - this.anoCreacion;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public int getAnoCreacion() {
        return anoCreacion;
    }

    public void setAnoCreacion(int anoCreacion) {
        this.anoCreacion = anoCreacion;
    }     
}

