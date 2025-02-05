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



    }



}
