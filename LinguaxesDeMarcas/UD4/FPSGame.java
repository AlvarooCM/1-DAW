import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;

import java.nio.*;
import java.util.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

public class FPSGame {

    private static final String GLFW_PRESS = null;
    
        // Ventana y contexto OpenGL
        private long window;
    
        // Variables del jugador
        private float playerX = 0.0f;
        private float playerY = 0.0f;
        private float playerZ = -5.0f;
        private float playerAngle = 0.0f;
        private final float playerSpeed = 0.1f;
    
        // Variables de los zombies
        private List<float[]> zombies = new ArrayList<>();
        private final float zombieSpeed = 0.05f;
    
        public void run() {
            init();
            loop();
    
            // Liberar recursos
            glfwFreeCallbacks(window);
            glfwDestroyWindow(window);
            glfwTerminate();
            Objects.requireNonNull(glfwSetErrorCallback(null)).free();
        }
    
        private void init() {
            // Configurar GLFW
            GLFWErrorCallback.createPrint(System.err).set();
            if (!glfwInit()) {
                throw new IllegalStateException("No se pudo inicializar GLFW");
            }
    
            // Configurar la ventana
            glfwDefaultWindowHints();
            glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
            glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    
            window = glfwCreateWindow(800, 600, "FPS Game con Zombies", NULL, NULL);
            if (window == NULL) {
                throw new RuntimeException("No se pudo crear la ventana GLFW");
            }
    
            // Configurar teclado
            glfwSetKeyCallback(window, (window, key, scancode, action, mods) -> {
                if (key == GLFW_KEY_ESCAPE && action == GLFW_RELEASE) {
                    glfwSetWindowShouldClose(window, true);
                }
            });
    
            // Centrar la ventana
            try (MemoryStack stack = stackPush()) {
                IntBuffer pWidth = stack.mallocInt(1);
                IntBuffer pHeight = stack.mallocInt(1);
                glfwGetWindowSize(window, pWidth, pHeight);
                GLFWVidMode vidMode = glfwGetVideoMode(glfwGetPrimaryMonitor());
                glfwSetWindowPos(
                        window,
                        (vidMode.width() - pWidth.get(0)) / 2,
                        (vidMode.height() - pHeight.get(0)) / 2);
            }
    
            // Hacer la ventana visible
            glfwMakeContextCurrent(window);
            glfwShowWindow(window);
    
            // Habilitar VSync
            glfwSwapInterval(1);
    
            // Inicializar OpenGL
            GL.createCapabilities();
            glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    
            // Crear zombies
            for (int i = 0; i < 5; i++) {
                createZombie();
            }
        }
    
        private void createZombie() {
            float angle = (float) (Math.random() * 2 * Math.PI);
            float distance = 5.0f + (float) (Math.random() * 5);
            float x = (float) Math.cos(angle) * distance;
            float z = (float) Math.sin(angle) * distance;
            zombies.add(new float[] { x, 0.0f, z });
        }
    
        private void drawZombie(float x, float y, float z) {
            glPushMatrix();
            glTranslatef(x, y, z);
            glColor3f(0.0f, 1.0f, 0.0f);
            glutSolidCube(0.5f);
            glPopMatrix();
        }
    
        private void drawPlayer() {
            glPushMatrix();
            glTranslatef(playerX, playerY, playerZ);
            glColor3f(1.0f, 0.0f, 0.0f);
            glutSolidCube(0.5f);
            glPopMatrix();
        }
    
        private void updateZombies() {
            for (float[] zombie : zombies) {
                float dx = playerX - zombie[0];
                float dz = playerZ - zombie[2];
                float dist = (float) Math.sqrt(dx * dx + dz * dz);
                if (dist > 0.5f) {
                    zombie[0] += (dx / dist) * zombieSpeed;
                    zombie[2] += (dz / dist) * zombieSpeed;
                }
            }
        }
    
        private void checkCollisions() {
            for (float[] zombie : zombies) {
                float dx = playerX - zombie[0];
                float dz = playerZ - zombie[2];
                float dist = (float) Math.sqrt(dx * dx + dz * dz);
                if (dist < 0.5f) {
                    System.out.println("¡Has sido atrapado por un zombie!");
                }
            }
        }
    
        private void loop() {
            glEnable(GL_DEPTH_TEST);
    
            while (!glfwWindowShouldClose(window)) {
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
                // Movimiento del jugador
                if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS) {
                    playerAngle += 1.0f;
                }
                if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS) {
                    playerAngle -= 1.0f;
                }
                if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS) {
                    playerX += Math.cos(Math.toRadians(playerAngle)) * playerSpeed;
                    playerZ += Math.sin(Math.toRadians(playerAngle)) * playerSpeed;
                }
                if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS) {
                playerX -= Math.cos(Math.toRadians(playerAngle)) * playerSpeed;
                playerZ -= Math.sin(Math.toRadians(playerAngle)) * playerSpeed;
            }

            // Configurar la vista
            glLoadIdentity();
            gluLookAt(
                playerX, playerY + 1.0f, playerZ,
                playerX + Math.cos(Math.toRadians(playerAngle)),
                playerY + 1.0f,
                playerZ + Math.sin(Math.toRadians(playerAngle))),
                0.0f, 1.0f, 0.0f
            );

            // Dibujar jugador y zombies
            drawPlayer();
            for (float[] zombie : zombies) {
                drawZombie(zombie[0], zombie[1], zombie[2]);
            }

            // Actualizar zombies y verificar colisiones
            updateZombies();
            checkCollisions();

            // Intercambiar buffers
            glfwSwapBuffers(window);
            glfwPollEvents();
        }
    }

    public static void main(String[] args) {
        new FPSGame().run();
    }
}
