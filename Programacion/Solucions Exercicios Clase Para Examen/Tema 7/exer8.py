#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crea un *script* que pida as notas dun exame dos alumnos dunha clase para procesalos. Tódalas notas téñense que ir almacenando nunha lista. Mostra un menú que se mostre continuamente ata que o usuario seleccione a opción saír. As entradas do menú son:

- `a) Engadir nota`
- `b) Ver media`
- `c) Ver número de aprobados`
- `d) Ver máxima nota`
- `e) Eliminar nota` Primeiro debes de mostrar un menú onde mostres para cada índice da lista, a súa nota. O usuario indicará o índice da nota a eliminar. 
- `f) Saír`


Para poder realizar cada acción do menú, implanta as seguintes funcións:

- `engadir_nota(lista: list[float], nota: float)`. 
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.
    - Se a nota é un valor inválido, lanza a excepción `ValueError`.

- `mostrar_notas(lista: list[float])`
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.
    - Débese mostrar neste formato: `índice: nota`. Exemplo:
        ```plaintext
        0 : nota1
        1 : nota2
        ...
        ```

- `media_notas(lista: list[float]) -> float`
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.

- `numero_aprobados(lista list[float]) -> int`
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.

- `maxima_nota(lista: list[float]) -> float`
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.

- `eliminar_nota(lista: list[float], indice: int)`
    - Comproba que a lista sexa unha lista, senón lanza excepción `ValueError`.
    - Se o índice non é válido lanza excepción `ValueError`.


> **IMPORTANTE**: Non utilices para realizar estas funcións as funcións do sistema `max`, `min`, etc. realiza este cálculo iterando sobre a lista.
"""


__author__ = "Manuel Ramón Varela López"


def engadir_notas(lista, nota):
    """
    Engade unha nota

    Args:
        lista (list): A lista onde se gardan as notas
        nota (float): A nota a engadir

    Raises:
        ValueError: Algún dos parámetros é inválido
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    if not(type(nota) is int or type(nota) is float):
        raise ValueError
    if nota < 0 or nota > 10:
        raise ValueError
    
    # Engadimos o valor
    lista.append(nota)

def mostrar_notas(lista):
    """
    Mostra as notas por pantalla

    Args:
        lista (list): A lista a mostrar

    Raises:
        ValueError: Algún dos parámetros é inválido
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    
    for indice, nota in enumerate(lista):
        print(indice, ":", nota)

def media_notas(lista):
    """
    Devolve a media das notas da lista

    Args:
        lista (list): A lista de notas

    Raises:
        ValueError: Se algún parámetro é inválido

    Returns:
        float A media das notas
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    
    # A lista non ten elementos polo que a media e 0
    if len(lista) == 0:
        return 0
    
    # Calculamos a media
    suma = 0
    for nota in lista:
        suma += nota
    return lista /len(lista)

def numero_aprobados(lista):
    """
    Devolve o número de aprobados

    Args:
        lista (list): A lista de notas

    Raises:
        ValueError: Se algún parámetro é inválido

    Returns:
        int: O número de aprobados
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    
    # Calculamos os aprobados
    aprobados = 0
    for nota in lista:
        if nota >= 5:
            aprobados += 1
    return aprobados

def maxima_nota(lista):
    """
    Devolve a máxima das notas da lista

    Args:
        lista (list): A lista de notas

    Raises:
        ValueError: Se algún parámetro é inválido

    Returns:
        float: A nota máxima
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    
    # Collemos a nota mais alta
    maxima = 0
    for nota in lista:
        if nota > maxima:
            maxima = nota
    
    return nota


def eliminar_nota(lista, indice):
    """
    Función que elimina unha nota

    Args:
        lista (float): A lista de notas
        indice (int): O índice da nota a borrar

    Raises:
        ValueError: Se algún dos valores non é válido
    """
    # Comprobamos os tipos e os valores válidos
    if type(lista) is not list:
        raise ValueError
    if type(indice) is not int:
        raise ValueError
    if indice < 0 or indice >= len(lista):
        raise ValueError
    
    # Elimino o valor indicado
    lista.pop(indice)

## Programa principal
# Esta e a lista onde gardamos as notas
lista_notas = []

while True:
    # Mostramos o menú
    print("Elixe unha opción:")
    print("\ta) Engadir nota")
    print("\tb) Ver media")
    print("\tc) Ver número de aprobados")
    print("\td) Ver máxima nota")
    print("\te) Eliminar nota")
    print("\tf) Saír")
    opcion = input("> ")

    if opcion == "a":
        try:
            nota = float(input("Introduce unha nota: "))
            engadir_notas(lista_notas, nota)
        except:
            print("Introduce valores válidos")

    elif opcion == "b":
        try:
            print("A media das notas é", media_notas(lista_notas))
        except:
            print("Introduce valores válidos")

    elif opcion == "c":
        try:
            print("O número de aprobados é", numero_aprobados(lista_notas))
        except:
            print("Introduce valores válidos")

    elif opcion == "d":
        try:
            print("A máxima nota é", maxima_nota(lista_notas))
        except:
            print("Introduce valores válidos")

    elif opcion == "e":
        try:
            mostrar_notas(lista_notas)
            indice_borrar = int(input("Introduce o índice a borrar: "))
            eliminar_nota(lista_notas, indice_borrar)
        except:
            print("Introduce valores válidos")

    elif opcion == "f":
        break

    else:
        print("Introduce un valor válido")