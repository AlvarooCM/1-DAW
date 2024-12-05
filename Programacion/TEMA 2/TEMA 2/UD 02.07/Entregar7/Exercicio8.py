"""Crea un script que pida as notas dun exame dos alumnos dunha clase para procesalos. Tódalas notas téñense que ir almacenando nunha lista. Mostra un menú que se mostre continuamente ata que o usuario seleccione a opción saír. As entradas do menú son:"""

__author__ = "Alvaro Camino Martinez"

def engadir_nota(lista: list[float], nota: float):
    """
    Añade una nota a la lista de notas.

    Args:
        lista (list[float]): Lista de notas donde se agregará la nueva nota.
        nota (float): Nota a añadir.

    Raises:
        ValueError: Si 'lista' no es una lista o 'nota' no es un número flotante.
    """
    # Verifica que el parámetro 'lista' sea del tipo correcto (lista)
    if type(lista) is not list:
        raise ValueError("Non é unha lista")  # Lanza un error si no es una lista
    
    # Verifica que el parámetro 'nota' sea del tipo correcto (float)
    if type(nota) is not float:
        raise ValueError("Valor inválido")  # Lanza un error si no es un número flotante
    
    # Si las validaciones son correctas, agrega la nota a la lista
    lista.append(nota)


def mostrar_notas(lista: list[float]) -> list[str]:
    """
    Muestra las notas junto con sus índices y devuelve una lista formateada.

    Args:
        lista (list[float]): Lista de notas a mostrar.

    Returns:
        list[str]: Lista con las notas formateadas.

    Raises:
        ValueError: Si 'lista' no es una lista.
    """
    # Verifica que la entrada sea una lista
    if type(lista) is not list:
        raise ValueError("Error, non é unha lista")  # Lanza un error si no es una lista
    
    lista_nova = []  # Lista auxiliar para guardar las notas con formato

    # Recorre cada nota en la lista junto con su índice
    for indice, nota in enumerate(lista):
        print(f"{indice}: {nota}")  # Imprime el índice y la nota
        # Formatea el índice y la nota como un string y lo añade a 'lista_nova'
        lista_nova.append(f"Índice: {indice} - Nota: {nota}")
    
    # Devuelve la lista formateada
    return lista_nova


def media_notas(lista: list[float]) -> float:
    """
    Calcula la media de las notas en la lista.

    Args:
        lista (list[float]): Lista de notas.

    Returns:
        float: La media de las notas.

    Raises:
        ValueError: Si 'lista' no es una lista.
    """
    # Verifica que el parámetro sea una lista
    if type(lista) is not list:
        raise ValueError("Error, non é unha lista")  # Lanza un error si no es una lista
    
    # Calcula la suma de las notas usando la función 'sum'
    suma = sum(lista)
    # Divide la suma total entre la cantidad de elementos en la lista
    return suma / len(lista)  # Devuelve el promedio


def numero_aprobados(lista: list[float]) -> int:
    """
    Cuenta el número de aprobados (notas >= 5).

    Args:
        lista (list[float]): Lista de notas.

    Returns:
        int: Número de aprobados.

    Raises:
        ValueError: Si 'lista' no es una lista.
    """
    # Verifica que la entrada sea una lista
    if type(lista) is not list:
        raise ValueError("Error, non é unha lista")  # Lanza un error si no es una lista
    
    aprobado = 0  # Inicializa el contador de aprobados

    # Recorre cada nota en la lista
    for nota in lista:
        # Verifica si la nota es mayor o igual a 5 (aprobado)
        if nota >= 5:
            aprobado += 1  # Incrementa el contador si es aprobado
    
    # Devuelve la cantidad de aprobados
    return aprobado


def maxima_nota(lista: list[float]) -> float:
    """
    Encuentra la nota máxima en la lista.

    Args:
        lista (list[float]): Lista de notas.

    Returns:
        float: La nota máxima.

    Raises:
        ValueError: Si 'lista' no es una lista o está vacía.
    """
    # Verifica que la entrada sea una lista
    if type(lista) is not list:
        raise ValueError("Error, non é unha lista")  # Lanza un error si no es una lista
    
    # Verifica que la lista no esté vacía
    if not lista:
        raise ValueError("A lista está vacía")  # Lanza un error si no hay notas
    
    # Devuelve la nota máxima usando la función 'max'
    return max(lista)


def eliminar_nota(lista: list[float], indice: int):
    """
    Elimina una nota por su índice.

    Args:
        lista (list[float]): Lista de notas.
        indice (int): Índice de la nota a eliminar.

    Raises:
        ValueError: Si 'lista' no es una lista o 'indice' no es un entero.
    """
    # Verifica que la entrada sea una lista
    if type(lista) is not list:
        raise ValueError("Error, non é unha lista")  # Lanza un error si no es una lista
    
    # Verifica que el índice sea un entero
    if type(indice) is not int:
        raise ValueError("Error, o índice non é válido")  # Lanza un error si el índice no es entero
    
    # Elimina la nota en la posición especificada
    del lista[indice]


# Programa principal
lista = []  # Inicializa la lista vacía para almacenar las notas

# Menú de opciones
print("NOTAS:")
print("\ta) Engadir Nota:")
print("\tb) Ver Media:")
print("\tc) Ver número de aprobados:")
print("\td) Ver máxima nota:")
print("\te) Eliminar Nota:")
print("\tf) Saír:")

# Solicita al usuario que elija una opción del menú
option = input(">")

if option == 'a':
    # Opción para añadir una nota
    nota = float(input("Ingrese una nota: "))  # Pide la nota como un número flotante
    engadir_nota(lista, nota)  # Llama a la función para añadir la nota

elif option == 'b':
    # Opción para calcular y mostrar la media de las notas
    media = media_notas(lista)  # Llama a la función para calcular la media
    print(f"La media de las notas es: {media}")

elif option == 'c':
    # Opción para contar el número de aprobados
    aprobados = numero_aprobados(lista)  # Llama a la función para contar aprobados
    print(f"El número de aprobados es: {aprobados}")

elif option == 'd':
    # Opción para encontrar y mostrar la nota máxima
    nota_maxima = maxima_nota(lista)  # Llama a la función para obtener la nota máxima
    print(f"La nota máxima es: {nota_maxima}")

elif option == 'e':
    # Opción para eliminar una nota según su índice
    indice = int(input("Ingrese el índice de la nota que quiere eliminar: "))  # Pide el índice como entero
    eliminar_nota(lista, indice)  # Llama a la función para eliminar la nota
    print("La nota ha sido eliminada")

elif option == 'f':
    # Opción para salir del programa
    print("Saliendo del programa de notas.")

else:
    # Mensaje de error si la opción ingresada no es válida
    print("Opción no válida")
