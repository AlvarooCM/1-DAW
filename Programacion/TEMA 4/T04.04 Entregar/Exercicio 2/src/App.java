import java.util.*;

public class App {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer entradas desde la consola
        Scanner scanner = new Scanner(System.in);

        // Crear instancias de los gestores de usuarios y tareas
        GestorUsuarios gestorUsuarios = new GestorUsuarios();
        GestorTareas gestorTareas = new GestorTareas();
        
        // Variable para almacenar al usuario actualmente logueado
        HashPassword usuarioActual = null;

        // Bucle principal que muestra el menú hasta que el usuario elija salir
        while (true) {
            // Mostrar las opciones del menú
            System.out.println("Menú de inicio:");
            System.out.println("1) Iniciar sesión");
            System.out.println("2) Registrarse");
            System.out.println("3) Salir");

            // Leer la opción elegida por el usuario
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar el buffer del scanner

            // Si elige la opción 1 (Iniciar sesión)
            if (opcion == 1) {
                System.out.print("Usuario: ");
                String username = scanner.nextLine(); // Leer el nombre de usuario
                System.out.print("Contraseña: ");
                String password = scanner.nextLine(); // Leer la contraseña

                // Intentar iniciar sesión con el nombre de usuario y la contraseña
                usuarioActual = gestorUsuarios.iniciarSesion(username, password);
                if (usuarioActual != null) {
                    // Si el inicio de sesión es exitoso, saludar al usuario
                    System.out.println("Bienvenido " + usuarioActual.nombre);
                } else {
                    // Si el inicio de sesión falla, mostrar un mensaje de error
                    System.out.println("Credenciales incorrectas");
                }
            }
            // Si elige la opción 2 (Registrarse)
            else if (opcion == 2) {
                System.out.print("Nombre: ");
                String nombre = scanner.nextLine(); // Leer el nombre del usuario
                System.out.print("Usuario: ");
                String username = scanner.nextLine(); // Leer el nombre de usuario
                System.out.print("Contraseña: ");
                String password = scanner.nextLine(); // Leer la contraseña
                System.out.print("Repetir Contraseña: ");
                String confirmacion = scanner.nextLine(); // Leer la confirmación de la contraseña

                // Intentar registrar al usuario con la información proporcionada
                if (gestorUsuarios.registrarUsuario(nombre, username, password, confirmacion)) {
                    // Si el registro es exitoso, mostrar un mensaje de éxito
                    System.out.println("Usuario registrado correctamente");
                } else {
                    // Si el registro falla (por ejemplo, si las contraseñas no coinciden)
                    System.out.println("Error al registrar usuario");
                }
            }
            // Si elige la opción 3 (Salir)
            else if (opcion == 3) {
                System.out.println("Saliendo");
                break; // Salir del bucle y terminar el programa
            }
        }
        
        // Cerrar el scanner para liberar recursos
        scanner.close();
    }
}

