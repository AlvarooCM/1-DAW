# Alvaro Camino Martínez

# Crea un menú en python. Tendrás que utilizar la librería de so/os. El menú debe de mostrar las siguientes opciones y se repetirá hasta que se seleccione la opción salir:

# 1 - Muestra el ID del usuario actual

# 2 - Muestra el nombre del sistema operativo actual

# 3 - Crea un directorio "directorio_os"

# 4 -Sitúate en el directorio "directorio_os"

# 5 - Muestra el directorio de trabajo actual

# 6 - Indica la instrucción para comprobar si un directorio existe o no. ¿Cuál utilizarías para un fichero?

# 7 - Lista el contenido de "directorio_os" utilizando rutas absolutas

# 8 - Crea un fichero de texto "archivo.txt"

# 9 - Abre al fichero para escritura y añade tu nombre y apellidos

# 10 - Muestra el contenido del fichero "archivo.txt"

# 11 - Renombra el fichero "archivo.txt" a "archivo_nuevo.txt"

# 12 - Crea dentro de "directorio_os" la siguiente estructura de directorios directorio_os1/directorio_os2 con una sola instrucción

# 13 - Borra la estructura de directorios creada anteriormente utilizando una sola instrucción

# 14 - Salir

import os

while True:
    print("\nElija una de las siguientes opciones: ")
    print("\t1 - Mostrar el ID del usuario actual")
    print("\t2 - Mostrar el nombre del sistema operativo actual")
    print("\t3 - Crear un directorio directorio_os")
    print("\t4 - Situarse en el directorio directorio_os")
    print("\t5 - Mostrar el directorio de trabajo actual")
    print("\t6 - Indicar la instrucción para comprobar si un directorio existe o no")
    print("\t7 - Listar el contenido de directorio_os utilizando rutas absolutas")
    print("\t8 - Crear un fichero de texto archivo.txt")
    print("\t9 - Abrir el fichero para escritura y añadir tu nombre y apellidos")
    print("\t10 - Mostrar el contenido del fichero archivo.txt")
    print("\t11 - Renombrar el fichero archivo.txt a archivo_nuevo.txt")
    print("\t12 - Crear dentro de directorio_os la siguiente estructura de datos directorio_os1/directorio_os2 con una sola instrucción")
    print("\t13 - Borrar la estructura de directorios creada anteriormente utilizando una sola instrucción")
    print("\t14 - Salir")

    try:
        option = int(input("Ingrese su opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if option == 1:
        print(f"ID del usuario actual: {os.getuid() if hasattr(os, 'getuid') else 'No disponible en este sistema'}")
    elif option == 2:
        print(f"Nombre del sistema operativo actual: {os.name}")
    elif option == 3:
        os.makedirs("directorio_os", exist_ok=True)
        print("Directorio 'directorio_os' creado.")
    elif option == 4:
        try:
            os.chdir("directorio_os")
            print("Se ha cambiado al directorio 'directorio_os'.")
        except FileNotFoundError:
            print("El directorio 'directorio_os' no existe.")
    elif option == 5:
        print(f"Directorio de trabajo actual: {os.getcwd()}")
    elif option == 6:
        print("Instrucción para verificar si un directorio existe: os.path.isdir('ruta')")
        print("Instrucción para verificar si un archivo existe: os.path.isfile('ruta')")
    elif option == 7:
        if os.path.exists("directorio_os"):
            contenido = [os.path.abspath(os.path.join("directorio_os", item)) for item in os.listdir("directorio_os")]
            print("Contenido de 'directorio_os' utilizando rutas absolutas:")
            for item in contenido:
                print(item)
        else:
            print("El directorio 'directorio_os' no existe.")
    elif option == 8:
        with open("archivo.txt", "w") as archivo:
            archivo.write("")
        print("Fichero 'archivo.txt' creado.")
    elif option == 9:
        with open("archivo.txt", "a") as archivo:
            nombre = input("Introduce tu nombre y apellidos: ")
            archivo.write(nombre + "\n")
        print("Nombre añadido al fichero 'archivo.txt'.")
    elif option == 10:
        try:
            with open("archivo.txt", "r") as archivo:
                contenido = archivo.read()
            print("Contenido de 'archivo.txt':")
            print(contenido)
        except FileNotFoundError:
            print("El fichero 'archivo.txt' no existe.")
    elif option == 11:
        try:
            os.rename("archivo.txt", "archivo_nuevo.txt")
            print("Fichero renombrado a 'archivo_nuevo.txt'.")
        except FileNotFoundError:
            print("El fichero 'archivo.txt' no existe.")
    elif option == 12:
        os.makedirs("directorio_os/directorio_os1/directorio_os2", exist_ok=True)
        print("Estructura de directorios 'directorio_os/directorio_os1/directorio_os2' creada.")
    elif option == 13:
        try:
            os.removedirs("directorio_os/directorio_os1/directorio_os2")
            print("Estructura de directorios eliminada.")
        except OSError:
            print("No se pudo eliminar la estructura de directorios. Asegúrate de que esté vacía y que exista.")
    elif option == 14:
        print("Saliend el programa")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
