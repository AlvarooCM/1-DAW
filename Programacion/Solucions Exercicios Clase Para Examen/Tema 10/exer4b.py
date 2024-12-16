#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Os números 17, 341 y 62 teñen en común que a suma dos seus díxitos dan o mesmo valor, 8. 
Hai moitos outros números así; de todos eles, o 17 é o máis pequeno.

Implanta un programa que recibirá por teclado un número entre 1 e 1000 e 
a continuación se mostre o número decimal máis pequeno que as súas cifras sumen ese cantidade.
""" 

__author__ = "Manuel Ramón Varela López"

def sumar_cifras(num):
    """
    Funcion que suma as cifras dun numero

    Args:
        num (int): O numero

    Raises:
        ValueError: se suma non é un enteiro positivo

    Returns:
        int: a suma das cifras
    """
    if type(num) is not int:
        raise ValueError
    if num < 0:
        raise ValueError
    suma = 0
    numero_str = str(num)
    for dixito in numero_str:
        dixito_int = int(dixito)
        suma += dixito_int
    return suma


def atopar_menor_suma_cifras(suma):
    """Función que atopa o menor dos números que a suma das súas cifras é a buscada

    Args:
        suma (int):A suma de cifras que buscamos

    Raises:
        ValueError: se suma non é un enteiro positivo

    Returns:
        int: O menor dos números que a súa suma de cifras dá un determinado valor
    """
    cadea = ""
    while True:
        if suma >= 10:
            cadea = "9" + cadea
            suma = suma - 9
        else:
            cadea = str(suma) +  cadea
            break
    
    return int(cadea)


if __name__ == "__main__":
    # Pedimos o numero entre 1 e 1000
    while True:
        try:
            numero = int(input("Introduce un numero entre 1 e 1000: "))
            if numero > 1000 or numero < 1:
                print("O valor ten que estar entre 1 e 1000")
            else:
                break
        except:
            print("Introduce un número.")

    # Collemos a suma de cifras do numero
    sum_cifras = sumar_cifras(numero)
    solucion= atopar_menor_suma_cifras(sum_cifras)

    # Imprimimos a solución
    print("A solucion é:", solucion)