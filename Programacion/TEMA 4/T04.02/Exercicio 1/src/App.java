import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // Abrimos scanner

        Scanner sc = new Scanner(System.in);

        // Hora de inicio pedida

        System.out.print("Introduzca la hora de inicio en formato HH:mm: ");
        String horaString = sc.nextLine();
        System.out.print("Introduzca los minutos que dura el programa: ");
        int duracion = sc.nextInt();

        DateTimeFormatter formato = DateTimeFormatter.ofPattern("HH:mm");

        LocalTime hora = LocalTime.parse(horaString, formato);

        LocalTime horaFinalizacion = hora.plus(duracion, ChronoUnit.MINUTES);

        String horaFinalizacionText = horaFinalizacion.format(formato);

        System.out.println(horaFinalizacionText);

        sc.close();
    }
}
