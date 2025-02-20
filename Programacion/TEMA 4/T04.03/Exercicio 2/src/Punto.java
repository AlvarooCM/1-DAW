public class Punto {
    
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public void desprazamentoHorizontal(double desprazamento){
        this.x = x + desprazamento;
    }

    public void desprazamentoVertical(double desprazamento){
        this.y = y + desprazamento;
    }

    public double getDistancia(Punto p) {
        double desprazamentoVertical = this.y - p.getY();
        double desprazamentoHorizontal = this.x - p.getX();
        
        double aux = Math.pow(desprazamentoVertical, 2) +
    Math.pow(desprazamentoHorizontal, 2);
        return Math.sqrt(aux);
    }

    public String getPosicion() {
        return "(" + this.getX() + ", " + this.getY() + ")";
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    } 



}
