public class App {
    public static void main(String[] args) throws Exception {

        Rectangulo rect1 = new Rectangulo(7.50,3.00);
        Rectangulo rect2 = new Rectangulo(10.00, 5.00);

        System.out.println("Perimetro rectángulo 1" + rect1.getPerimetro() + " cm");

        System.out.println("Perimetro rectángulo 2" + rect2.getPerimetro() + " cm");

        System.out.println("Área rectangulo 1 " + rect1.getArea() +" cm^2");

        System.out.println("Área rectangulo 2 " + rect2.getArea() +" cm^2");
    }
}
