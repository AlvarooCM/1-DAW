// Exercicio 6. Crea un programa en Java para xestionar as horas traballadas polos empregados. Deberás crear un HashMap onde a clave é o DNI dos empregados e o valor é unha ArrayList para almacenar as fichaxes (tanto de entrada como de saía) de dito empregado. O programa contará co seguinte menú:

// a) Fichar entrada/saída: o usuario introducirá o seu DNI e almacenarase a hora actual. Tanto as horas de entrada como de saída almacénanse nunha mesma lista, polo tanto o primeiro elemento da lista sería a fichaxe de entrada e o segundo a de saída. Do mesmo modo, o terceiro elemento sería unha fichaxe de entrada e o cuarto unha fichaxe de saída. O resto de fichaxes seguen o mesmo mecanismo.

// b) Comprobar salario: o usuario introducirá o seu DNI e indicarase o seu salario a percibir. Cada hora traballada págase a 12€, aínda que este salario se calcula en función dos minutos traballados. Para realizar o cálculo debes ter en conta tan só as xornadas terminadas, se por exemplo hai unha fichaxe de entrada sen a súa saída non se contabilizará.

import java.util.*;

public class XestionHoras {
    public static void main(String[] args) throws Exception {
        
        // Crear o HashMap para almacenar os datos
        HashMap<String, ArrayList<Long>> fichaxes = new HashMap<>();

        // Datos de proba (fichaxes de entrada/saída)
        // Empregado 1: DNI 12345
        ArrayList<Long> fichaxesEmpregado1 = new ArrayList<>();
        fichaxesEmpregado1.add(System.currentTimeMillis() - 3600000); // Fichaxe de entrada
        fichaxesEmpregado1.add(System.currentTimeMillis() - 1800000); // Fichaxe de saída
        fichaxes.put("12345", fichaxesEmpregado1);
    }
}
