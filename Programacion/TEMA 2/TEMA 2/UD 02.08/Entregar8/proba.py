# Lista para almacenar los datos de los alumnos
alumnos = []

def ingresar_datos():
    """Función para ingresar un nuevo alumno."""
    nombre = input("Introduce el nombre del alumno: ").strip()
    apellidos = input("Introduce los apellidos del alumno: ").strip()
    while True:
        try:
            nota = float(input("Introduce la nota del alumno (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Introduce un número válido.")
    alumnos.append({"nombre": nombre, "apellidos": apellidos, "nota": nota})
    print("Alumno añadido con éxito.\n")

def eliminar_datos():
    """Función para eliminar un alumno."""
    listar_alumnos()
    try:
        indice = int(input("Introduce el índice del alumno a eliminar: "))
        if 0 <= indice < len(alumnos):
            eliminado = alumnos.pop(indice)
            print(f"Alumno eliminado: {eliminado['apellidos']}, {eliminado['nombre']}.\n")
        else:
            print("Índice fuera de rango.\n")
    except ValueError:
        print("Introduce un índice válido.\n")

def modificar_nota():
    """Función para modificar la nota de un alumno."""
    listar_alumnos()
    try:
        indice = int(input("Introduce el índice del alumno a modificar: "))
        if 0 <= indice < len(alumnos):
            while True:
                try:
                    nueva_nota = float(input(f"Introduce la nueva nota para {alumnos[indice]['apellidos']}, {alumnos[indice]['nombre']} (0-10): "))
                    if 0 <= nueva_nota <= 10:
                        alumnos[indice]['nota'] = nueva_nota
                        print("Nota actualizada con éxito.\n")
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Introduce un número válido.")
        else:
            print("Índice fuera de rango.\n")
    except ValueError:
        print("Introduce un índice válido.\n")

def listar_alumnos():
    """Función para mostrar la lista de alumnos."""
    if not alumnos:
        print("No hay alumnos registrados.\n")
    else:
        for i, alumno in enumerate(alumnos):
            print(f"{i}. {alumno['apellidos']}, {alumno['nombre']}: {alumno['nota']}")

def ver_aprobados():
    """Función para mostrar los alumnos aprobados."""
    aprobados = [alumno for alumno in alumnos if alumno['nota'] >= 5]
    if not aprobados:
        print("No hay alumnos aprobados.\n")
    else:
        for i, alumno in enumerate(aprobados):
            print(f"{i}. {alumno['apellidos']}, {alumno['nombre']}: {alumno['nota']}")
    print()

def ordenar_alfabeticamente():
    """Función para mostrar alumnos ordenados alfabéticamente por apellidos."""
    if not alumnos:
        print("No hay alumnos registrados.\n")
    else:
        alumnos_ordenados = sorted(alumnos, key=lambda x: (x['apellidos'], x['nombre']))
        for i, alumno in enumerate(alumnos_ordenados):
            print(f"{i}. {alumno['apellidos']}, {alumno['nombre']}: {alumno['nota']}")
    print()

def calcular_nota_media():
    """Función para calcular y mostrar la nota media."""
    if not alumnos:
        print("No hay alumnos registrados.\n")
    else:
        media = sum(alumno['nota'] for alumno in alumnos) / len(alumnos)
        print(f"La nota media de los alumnos es: {media:.2f}\n")

def menu():
    """Función principal para mostrar el menú y manejar las opciones."""
    while True:
        print("Menú:")
        print("a) Ingresar datos alumno")
        print("b) Eliminar datos alumno")
        print("c) Modificar nota alumno")
        print("d) Ver nombres y apellidos de alumnos aprobados")
        print("e) Mostrar alumnos alfabéticamente")
        print("f) Ver la nota media")
        print("g) Salir")
        opcion = input("Elige una opción: ").strip().lower()

        if opcion == 'a':
            ingresar_datos()
        elif opcion == 'b':
            eliminar_datos()
        elif opcion == 'c':
            modificar_nota()
        elif opcion == 'd':
            ver_aprobados()
        elif opcion == 'e':
            ordenar_alfabeticamente()
        elif opcion == 'f':
            calcular_nota_media()
        elif opcion == 'g':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

# Ejecutar el programa
menu()
