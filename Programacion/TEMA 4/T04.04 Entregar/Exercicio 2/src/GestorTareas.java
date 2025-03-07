import java.time.LocalDateTime;
import java.util.*;

public class GestorTareas {
    // Lista para almacenar todas las tareas
    List<Tarea> tareas = new ArrayList<>();

    // Método para agregar una nueva tarea a la lista
    public void agregarTarea(String titulo, String descripcion, LocalDateTime fechaLimite) {
        // Crea una nueva tarea con los datos proporcionados y la agrega a la lista de tareas
        tareas.add(new Tarea(titulo, descripcion, fechaLimite));
    }

    // Método para obtener las tareas pendientes (aún no realizadas)
    public List<Tarea> obtenerTareasPendientes() {
        List<Tarea> pendientes = new ArrayList<>(); // Lista para almacenar las tareas pendientes
        // Recorre la lista de todas las tareas
        for (Tarea tarea : tareas) {
            // Si la tarea no está marcada como realizada, la agrega a la lista de pendientes
            if (!tarea.realizada) {
                pendientes.add(tarea);
            }
        }
        // Retorna la lista de tareas pendientes
        return pendientes;
    }
}

