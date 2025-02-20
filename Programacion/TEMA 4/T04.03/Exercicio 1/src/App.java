public class App {
    public static void main(String[] args) {

        Grupo laRaiz = new Grupo ("La raiz", "España", 2006);

        Disco entrePoetasYPresos = new Disco ("Entre Poetas y Presos", "laRaiz", 2016, 15);

        System.out.println(laRaiz.getIdade());

        System.out.println(entrePoetasYPresos.getAnosExistencia());
        
    }
}
