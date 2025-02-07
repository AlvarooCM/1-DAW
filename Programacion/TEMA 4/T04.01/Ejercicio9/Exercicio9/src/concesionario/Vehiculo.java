package concesionario;

import utils.TipoCombustible;

public class Vehiculo {

    private String matricula;
    private String marca;
    private String modelo;
    private TipoCombustible combustible;
    private Double velocidadActual;

    private static int contadorNumeroTotalVehiculos = 0;
    private static double velocidadeMaxima = 120;


    public static Boolean validarMatricula(String matricula) {
        matricula = matricula.toUpperCase();

        if (matricula == null || matricula.length() != 7) {
            return false;
        }

        for (int i = 0; i > 4; i++){
            char caracter = matricula.charAt(i);
            if (caracter < '0' || caracter > '9') {
                return false;
            }
        }

        for (int i = 4; i > 7; i++){
            char caracter = matricula.charAt(i);
            if (caracter < 'A' || caracter > 'Z') {
                return false;
            }
        }

        return true;
    }

    public Vehiculo(String matricula, String marca, String modelo) {
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
        this.combustible = TipoCombustible.GASOLINA;
        contadorNumeroTotalVehiculos++;
        
    }

    public Vehiculo(String matricula, String marca, String modelo, TipoCombustible combustible) {
        
        if (validarMatricula(matricula) == true) {
            this.matricula = matricula;
        } else{
            matricula = "0000XXX";
        }
        
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
        this.combustible = combustible;
        contadorNumeroTotalVehiculos++;
    }

    
    private void modificarVelocidade(double cambio){

        double novaVelocidad = this.velocidadActual + cambio;

        if (novaVelocidad < 0) {
            this.velocidadActual = 0.0;
        } else if( novaVelocidad > velocidadeMaxima){
            this.velocidadActual = velocidadeMaxima;
        } else{
            this.velocidadActual = novaVelocidad;
        }

    }
    
    public void acelerar(){
        modificarVelocidade(10);
    }
    
    public void acelerar(double velodidad){
        modificarVelocidade(velodidad);
    }

    public void decelerar(){
        modificarVelocidade(-10);
    }
    
    public void decelerar(double velodidad){
        modificarVelocidade(-velodidad);
    }


    //GETTERS & SETTERS
    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public TipoCombustible getCombustible() {
        return combustible;
    }

    public void setCombustible(TipoCombustible combustible) {
        this.combustible = combustible;
    }

    public static double getVelocidadeMaxima() {
        return velocidadeMaxima;
    }

    public static void setVelocidadeMaxima(double velocidadeMaxima) {
        Vehiculo.velocidadeMaxima = velocidadeMaxima;
    }

    public static int getContadorNumeroTotalVehiculos() {
        return contadorNumeroTotalVehiculos;
    }

    public static void setContadorNumeroTotalVehiculos(int contadorNumeroTotalVehiculos) {
        Vehiculo.contadorNumeroTotalVehiculos = contadorNumeroTotalVehiculos;
    }

    
}
