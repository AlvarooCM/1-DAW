public class App {
    public static void main(String[] args){

        Empregado manuel = new Empregado("55026812R", "Manuel", "Varela", "López", 1500);

        System.out.println(manuel.getDNI());

        manuel.setDNI("55026811R");

        String mensaxe = manuel.getApelidos() + ", " + manuel.getNome() + " con " + manuel.getDNI() +
            " ten un salario neto de " + manuel.getSalarioNeto() + " €";
        System.out.println(mensaxe);
    }
}