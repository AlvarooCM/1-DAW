public class App {
    public static void main(String[] args) throws Exception {
        
        Coche ibiza = new Coche("Seat", "Ibiza", "Rojo", 3);

        Coche leon = new Coche("Seat", "Leon", "Negro", 5);

        leon.setCor("Amarillo");

        System.out.println(ibiza.getMarca() + " " + ibiza.getModelo() + ": " + ibiza.getCor());
        System.out.println(leon.getMarca() + " " + leon.getModelo() + ": " + leon.getCor());
    }
}
