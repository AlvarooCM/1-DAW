public class Alumno {
    private static int numeroExpedienteSeguinte = 101;

    private String nome;
    private String apelidos;
    private double[] notas;
    private boolean[] notasEngadidas;
    private String numeroExpediente;

    public Alumno(String nome, String apelidos){
        this.setNome(nome);
        this.setApelidos(apelidos);

        this.numeroExpediente = String.valueOf(Alumno.numeroExpedienteSeguinte);
        numeroExpedienteSeguinte++;

        notas = new double[3];
        notasEngadidas = new boolean[3];
        for(int i=0; i< notasEngadidas.length; i++){
            notasEngadidas[i] = false;
        }
    }

    public void setNota1Trimestre(double nota){
        this.setNotatrimestre(nota, 0);
    }

    public void setNota2Trimestre(double nota){
        this.setNotatrimestre(nota, 1);
    }

    public void setNota3Trimestre(double nota){
        this.setNotatrimestre(nota, 2);
    }

    private void setNotatrimestre(double nota, int trimestre) {
        if (nota >= 0 && nota <= 10){
            this.notas[trimestre] = nota;
            this.notasEngadidas[trimestre] = true;
        }
    }

    public String getNome() {
        return nome;
    }

    public String getApelidos() {
        return apelidos;
    }

    public String getNumeroExpediente() {
        return numeroExpediente;
    }

    public double getMedia(){
        int nNotas = 0;
        double sumaNotas = 0;

        for(int i=0; i < notasEngadidas.length; i++){
            if(notasEngadidas[i]){
                nNotas++;
                sumaNotas = sumaNotas + notas[i];
            }
        }

        if (nNotas > 0){
            return sumaNotas / nNotas;
        }

        return 0.0;
    }

    public boolean isAprobado() {
        for(int i=0; i < notasEngadidas.length; i++){
            if(! notasEngadidas[i]){
                return false;
            }
        }

        if (this.getMedia() >= 5){
            return true;
        }
        return false;
    }
}
