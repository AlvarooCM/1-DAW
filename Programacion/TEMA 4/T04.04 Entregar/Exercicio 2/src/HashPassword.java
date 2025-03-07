import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashPassword {
    String nombre;
    String username;
    String passwordHash;

    public HashPassword(String nombre, String username, String password) {
        this.nombre = nombre;
        this.username = username;
        this.passwordHash = hashPassword(password);
    }

    public boolean verificarPassword(String password) {
        return this.passwordHash.equals(hashPassword(password));
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    private static String hashPassword(String password) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}
