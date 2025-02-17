//  Crea un programa que xestione as citas dunha consulta médica. Deberas almacenar para cada paciente o día e hora da súa cita. Utiliza un ArrayList para os nomes dos pacientes (ArrayList de String) e outro para as citas (ArrayList de LocalDataTime). O programa contará co seguinte menú:

// a. Engadir cita: engadirá o nome do paciente e a súa cita. A cita introducirase co seguinte formato HH:mm dd/MM/yyyy Comprobarase que non existen citas 30 minutos antes ou 30 minutos despois. Ademais non se pode engadir unha cita un sábado ou domingo. Se acontecera algún destes casos informarase ao usuario que non se puido realizar a cita.

// b. Eliminar cita: mostraranse as citas, indicando o paciente e día e hora no seguinte formato dd/MM/yyyy HH:mm, nun menú para seleccionar a cita a eliminar.

// c. Seleccionar data: introducirase unha data co formato dd-MM-yyyy e mostraranse as citas dese día. Non teñen que mostrarse en orde.

import java.time.DayOfWeek;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Scanner;

public class consultaMedica {

    // Listas para almacenar os nomes dos pacientes e as súas citas

    private static ArrayList<String> pacientes = new ArrayList<>();
    private static ArrayList<LocalDateTime> citas = new ArrayList<>();

    // Formato para as datas

    private static DateTimeFormatter formatter = DateTimeFormatter. ofPattern("HH:mm dd/MM/yyyy");
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Menú:");
            System.out.println("a. Engadir cita");
            System.out.println("b. Eliminar cita");
            System.out.println("c. Seleccionar data");
            System.out.println("d. Sair");
            System.out.print("Escolle unha opción:");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "a":
                    engadirCita(scanner);
                    break;
                case "b":
                    eliminarCita(scanner);
                    break;
                case "c":
                    seleccionarData(scanner);
                    break;
                case "d":
                    System.out.println("Saindo do programa...");
                    return;
                default:
                    System.out.println("Opción n inválida");
                    break;
            }
        }
    }

    // Método para engadir unha cita

    public static void engadirCita(Scanner scanner) {
        System.out.print("Introduce o nome do paciente: ");
        String paciente = scanner.nextLine();

        System.out.print("Introduce a data e hora da cita (HH:mm dd/MM/yyyy): ");
        String data = scanner.nextLine();

        LocalDateTime cita = LocalDateTime.parse(data, formatter);

        // Comprobamos que a cita non sexa un sábado ou domingo

        if (cita.getDayOfWeek() == DayOfWeek.SATURDAY || cita.getDayOfWeek() == DayOfWeek.SUNDAY) {
            System.out.println("Non se poden engadir citas un sábado ou domingo.");
            return;
        }

        for (LocalDateTime citaExistente : citas) {
            if (cita.isBefore(citaExistente.plusMinutes(30)) && cita.isAfter(citaExistente.minusMinutes(30))) {
                System.out.println("Xa hai unha cita dentro de 30 minutos antes ou despois.");
                return;
            }
        }

        // Engadimos a cita

        pacientes.add(paciente);
        citas.add(cita);
        System.out.println("Cita del paciente " + paciente + " el " + cita.format(formatter) + " añadida correctamente. ");
    }

    // Metodo eliminarCitas

    public static void eliminarCita(Scanner scanner) {
        if (pacientes.isEmpty()) {
            System.out.println("No hay citas");
            return;
        }

        // Mostrar citas y pedir al usuario que seleccione para eliminar

        System.out.println("Citas Existentes;");
        for (int i = 0; i < pacientes.size(); i++) {
            System.out.println((i + 1) + ") " + pacientes.get(i) + " - " + citas.get(i).format(formatter));
        }
        
        System.out.print("Elixe a cita a eliminar (1-" + pacientes.size() + "): ");
        int index = Integer.parseInt(scanner.nextLine()) - 1;

        if (index >= 0 && index < pacientes.size()) {
            String pacienteEliminado = pacientes.remove(index);
            citas.remove(index);
            System.out.println("Cita de " + pacienteEliminado + " eliminada.");
        } else {
            System.out.println("O número de cita non é válido.");
        }
    }

    // Método para seleccionar as citas dun día
    public static void seleccionarData(Scanner scanner) {
        System.out.print("Introduce a data (dd-MM-yyyy): ");
        String dataStr = scanner.nextLine();

        // Transfromar a data
        LocalDateTime data;
        try {
            data = LocalDateTime.parse(dataStr + "00:00:00");
        } catch (Exception e) {
            System.out.println("Formato de data incorrecto.");
            return;
        }

        // Mostrar as citas para esa data
        System.out.println("Citas para o día " + dataStr + ":");
        for (int i = 0; i < pacientes.size(); i++) {
            LocalDateTime cita = citas.get(i);
            if (cita.toLocalDate().isEqual(data.toLocalDate())) {
                System.out.println(pacientes.get(i) + " - " + cita.format(formatter));
            }
        }
    }
}
