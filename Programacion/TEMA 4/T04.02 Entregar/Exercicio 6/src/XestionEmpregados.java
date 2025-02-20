// Exercicio 6. Crea un programa en Java para xestionar as horas traballadas polos empregados. Deberás crear un HashMap onde a clave é o DNI dos empregados e o valor é unha ArrayList para almacenar as fichaxes (tanto de entrada como de saía) de dito empregado. O programa contará co seguinte menú:

// a) Fichar entrada/saída: o usuario introducirá o seu DNI e almacenarase a hora actual. Tanto as horas de entrada como de saída almacénanse nunha mesma lista, polo tanto o primeiro elemento da lista sería a fichaxe de entrada e o segundo a de saída. Do mesmo modo, o terceiro elemento sería unha fichaxe de entrada e o cuarto unha fichaxe de saída. O resto de fichaxes seguen o mesmo mecanismo.

// b) Comprobar salario: o usuario introducirá o seu DNI e indicarase o seu salario a percibir. Cada hora traballada págase a 12€, aínda que este salario se calcula en función dos minutos traballados. Para realizar o cálculo debes ter en conta tan só as xornadas terminadas, se por exemplo hai unha fichaxe de entrada sen a súa saída non se contabilizará.

import java.time.LocalDateTime;
import java.time.Duration;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class XestionEmpregados {
    // Mapa para almacenar os rexistros de fichaxe dos empregados
    private static final HashMap<String, ArrayList<LocalDateTime>> fichaxes = new HashMap<>();
    private static final double SALARIO_POR_HORA = 12.0; // Salario por hora en euros
    private static final DateTimeFormatter FORMATO = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss"); // Formato de data e hora

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;
        
        // Introducir datos de proba
        fichaxes.put("12345678A", new ArrayList<>(Arrays.asList(
            LocalDateTime.now().minusHours(5), LocalDateTime.now().minusHours(4),
            LocalDateTime.now().minusDays(1).minusHours(6), LocalDateTime.now().minusDays(1).minusHours(4)
        )));
        fichaxes.put("87654321B", new ArrayList<>(Arrays.asList(
            LocalDateTime.now().minusHours(3), LocalDateTime.now().minusHours(2)
        )));
        
        do {
            // Menú de opcións
            System.out.println("Menú:");
            System.out.println("1. Fichar entrada/saída");
            System.out.println("2. Comprobar salario");
            System.out.println("3. Saír");
            System.out.print("Escolle unha opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();
            
            switch (opcion) {
                case 1:
                    fichar(scanner);
                    break;
                case 2:
                    comprobarSalario(scanner);
                    break;
                case 3:
                    System.out.println("Saíndo...");
                    break;
                default:
                    System.out.println("Opción incorrecta. Inténtao de novo.");
            }
        } while (opcion != 3);
        
        scanner.close();
    }

    private static void fichar(Scanner scanner) {
        System.out.print("Introduce o teu DNI: ");
        String dni = scanner.nextLine();
        LocalDateTime agora = LocalDateTime.now(); // Captura a hora actual
        
        // Engade o rexistro á lista do empregado
        fichaxes.putIfAbsent(dni, new ArrayList<>());
        fichaxes.get(dni).add(agora);
        
        System.out.println("Fichaxe rexistrada: " + agora.format(FORMATO));
    }

    private static void comprobarSalario(Scanner scanner) {
        System.out.print("Introduce o teu DNI: ");
        String dni = scanner.nextLine();
        
        // Verifica se hai rexistros suficientes para calcular o salario
        if (!fichaxes.containsKey(dni) || fichaxes.get(dni).size() < 2) {
            System.out.println("Non hai datos suficientes para calcular o salario.");
            return;
        }
        
        ArrayList<LocalDateTime> rexistros = fichaxes.get(dni);
        long minutosTraballados = 0;
        
        // Calcula o tempo traballado só en sesións completas (entrada-saída)
        for (int i = 0; i < rexistros.size() - 1; i += 2) {
            LocalDateTime entrada = rexistros.get(i);
            LocalDateTime saida = rexistros.get(i + 1);
            minutosTraballados += Duration.between(entrada, saida).toMinutes();
        }
        
        // Calcula o salario baseado nos minutos traballados
        double salario = (minutosTraballados / 60.0) * SALARIO_POR_HORA;
        System.out.printf("Salario a percibir: %.2f€%n", salario);
    }
}