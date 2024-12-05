"""Queremos realizar un programa que calcule o índice dunha chave para un dicionario utilizando o algoritmo de hashing por folding. O programa recibirá en orde os seguintes parámetros: tamaño da táboa, número de división por folding e a chave."""

__author__ = "Alvaro Camino Martinez"

# Creamos una funcion que almacena tamaño_taboa, numero_division, chave

def hashing_por_folding (tamaño_taboa, tamaño_division, chave):
    """_summary_

    Args:
        tama (_type_): Tamaño que va a tener la tabla.
        numero_division (_type_): Numero de divisiones que va a tener.
        chave (_type_): Llave que se va a convertir.

    Returns:
        _type_: Devuelve la posicion en la tabla hash en la que se almacenara la clave.
    """

# Conversion da chave a cadena de texto

    chave_cadena = str(chave)

# Calculamos el tamaño de cada parte de la clave y se divide entre el numero de divisiones

    parte_folding = len(chave_cadena) // tamaño_division

# Inicializamus un acumuladr

    total = 0

# Iniciamos un for 

    for i in range (numero_division):

        parte_clave = chave_cadena [i * tamaño_division:(i + 1) * tamaño_division]

        total = total + int (parte_clave)

    index = total % tamaño_taboa
    return index

# Pedir datos a los usuarios mas impresion final

tamaño_taboa = int(input("Introduzca el tamaño que va a tener la tabla:"))

numero_division = int(input("Introduce el numero de divisiones:"))

chave = int(input("Introduzca la llave que quiere convertir:"))

index = hashing_por_folding (tamaño_taboa, numero_division, chave)

print ("Indice calculado:", index)



