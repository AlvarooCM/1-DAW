import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Tarea {
    // Atributos de la clase Tarea
    String titulo;          // Título de la tarea
    String descripcion;     // Descripción de la tarea
    LocalDateTime fechaLimite;  // Fecha límite para completar la tarea
    LocalDateTime fechaCreacion; // Fecha en que la tarea fue creada
    boolean realizada;      // Indica si la tarea ha sido marcada como realizada o no

    // Constructor de la clase Tarea
    public Tarea(String titulo, String descripcion, LocalDateTime fechaLimite) {
        this.titulo = titulo;               // Inicializa el título de la tarea
        this.descripcion = descripcion;     // Inicializa la descripción de la tarea
        this.fechaLimite = fechaLimite;     // Inicializa la fecha límite
        this.fechaCreacion = LocalDateTime.now();  // Establece la fecha de creación como el momento actual
        this.realizada = false;             // Por defecto, la tarea no está realizada
    }

    // Método para marcar la tarea como realizada
    public void marcarComoRealizada() {
        this.realizada = true;  // Cambia el estado de la tarea a realizada
    }

    // Método que verifica si la tarea está vencida
    public boolean vencida() {
        // La tarea está vencida si la fecha límite ya pasó y no ha sido realizada
        return LocalDateTime.now().isAfter(fechaLimite) && !realizada;
    }

    // Método que verifica si la tarea está dentro de las próximas 48 horas
    public boolean enProximas48Horas() {
        LocalDateTime ahora = LocalDateTime.now();  // Obtiene la fecha y hora actuales
        // La tarea está en las próximas 48 horas si su fecha límite está después de ahora
        // y antes de 48 horas a partir de ahora, además de no haber sido realizada
        return !realizada && fechaLimite.isAfter(ahora) && fechaLimite.isBefore(ahora.plusHours(48));
    }

    // Método para obtener los detalles de la tarea como una cadena de texto
    public String detalles() {
        // Define un formato para la fecha de creación y la fecha límite (día/mes/año hora:minuto)
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        
        // Retorna una cadena con los detalles de la tarea (título, descripción, fechas)
        return "Título: " + titulo + "\nDescripción: " + descripcion + "\nCreado: " + fechaCreacion.format(formatter) + "\nLímite: " + fechaLimite.format(formatter);
    }
}
