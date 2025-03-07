import java.util.*;

public class GestorUsuarios {
    // Mapa que almacena los usuarios. La clave es el nombre de usuario y el valor es el objeto de tipo HashPassword.
    Map<String, HashPassword> usuarios = new HashMap<>();

    // Método para registrar un nuevo usuario
    public boolean registrarUsuario(String nombre, String username, String password, String confirmacion) {
        // Verifica si el nombre de usuario ya existe o si las contraseñas no coinciden
        if (usuarios.containsKey(username) || !password.equals(confirmacion)) {
            return false; // Si existe el usuario o las contraseñas no coinciden, no se registra el usuario
        }
        
        // Si todo es correcto, se crea un nuevo objeto HashPassword y se agrega al mapa de usuarios
        usuarios.put(username, new HashPassword(nombre, username, password));
        return true; // Registro exitoso
    }

    // Método para iniciar sesión de un usuario
    public HashPassword iniciarSesion(String username, String password) {
        // Busca al usuario en el mapa de usuarios por su nombre de usuario
        HashPassword usuario = usuarios.get(username);
        
        // Verifica si el usuario existe y si la contraseña proporcionada es correcta
        return (usuario != null && usuario.verificarPassword(password)) ? usuario : null;
        // Si las credenciales son correctas, retorna el objeto HashPassword del usuario, de lo contrario, retorna null
    }
}

