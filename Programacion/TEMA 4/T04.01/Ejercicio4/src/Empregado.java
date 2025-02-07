public class Empregado {
    private static double IRPF = 0.15;
    
    private String dni;
    private String nome;
    private String apelido1;
    private String apelido2;
    private double salariobruto;
    private boolean dniEngadido;


    public Empregado(String dni, String nome, String apelido1, String apelido2, double salariobruto) {
        this.dni = dni;
        this.nome = nome;
        this.apelido1 = apelido1;
        this.apelido2 = apelido2;
        this.salariobruto = salariobruto;
    }

    public Empregado (String dni, String nome, String apelido1, double salariobruto) {
        this (dni, nome, apelido1, "", salariobruto);
    }

    public Empregado (String nome, String apelido1, double salarioBruto) {

        this ("", nome, apelido1, "", salarioBruto);
    }

    private boolean validarDNI(String dni) {
        if (dni.length() != 9) {
            return false;
        }

        String numeros = dni.substring(0,8);
        char letra = dni.charAt (8);

        for(int i=0; i< numeros.length(); i++){
            if (!((int)numeros.charAt(i) >= (int) '0' && (int)numeros.charAt(i) <= (int)'9')){

                return false;
            }
        }

        if (!((int)letra >= (int) 'A' && (int)letra <= (int)'Z')){
            return false;
        }

        int numero = Integer.valueOf(numeros);

        String letras = "TRWAGMYFPDXBNJZSQVHLCKE";
        int resto = numero % letras.length();

        char letraReal = letras.charAt(resto);

        if (letra != letraReal) {
            return false;
        }

        return true;
    }

    public String getApelidos(){
        return this.apelido1 + " " + this.apelido2;
    }

    public String getDNI(){
        if(this.dniEngadido){
            return this.dni;
        }
        return "Sen informacion";
    }

    public double getSalarioNeto(){
        return this.salariobruto * (1.0 - Empregado.IRPF);
    }

    public String getNome(){
        return nome;
    }

    public double getSalarioBruto(){
        return salariobruto;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setApelido1(String apelido1) {
        this.apelido1 = apelido1;
    }

    public void setApelido2(String apelido2) {
        this.apelido2 = apelido2;
    }

    public void setSalariobruto(double salariobruto) {
        this.salariobruto = salariobruto;
    }

    public void setDNI(String dni){
        if (this.validarDNI(dni)){
            this.dni = dni;
            this.dniEngadido = true;
        }
        else {
            this.dniEngadido = false;
        }
    }
}
