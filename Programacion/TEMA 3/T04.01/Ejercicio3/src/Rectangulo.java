public class Rectangulo {
    
    private Double altura;
    private Double base;

    
    public Rectangulo(Double altura, Double base) {
        this.altura = altura;
        this.base = base;
    }

    public double getPerimetro() {
        return this.base * 2 + this.altura + 2;
    }

    public double getArea() {
        return this.base * this.altura;
    }

    public Double getAltura() {
        return altura;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }

    public Double getBase() {
        return base;
    }

    public void setBase(Double base) {
        this.base = base;
    }
}
