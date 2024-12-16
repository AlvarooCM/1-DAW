#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Os números 17, 341 y 62 teñen en común que a suma dos seus díxitos dan o mesmo valor, 8. 
Hai moitos outros números así; de todos eles, o 17 é o máis pequeno.

Implanta un programa que recibirá por teclado un número entre 1 e 1000 e 
a continuación se mostre o número decimal máis pequeno que as súas cifras sumen ese cantidade.
""" 

import time
from exer4a import atopar_menor_suma_cifras as atopar_menor_suma_cifras_a
from exer4b import atopar_menor_suma_cifras as atopar_menor_suma_cifras_b

# O numero maximo a introducir
numero_maximo = 10000

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

######## Esta e a solución A
time_start = time.time()
for numero in range(1, numero_maximo + 1):
    # Collemos a suma de cifras do numero
    sum_cifras = sumar_cifras(numero)
    solucion = atopar_menor_suma_cifras_a(sum_cifras)
time_finish = time.time()
print("Temo do algoritmo A: ", time_finish - time_start)

######## Esta e a solución B
time_start = time.time()
for numero in range(1, numero_maximo + 1):
    # Collemos a suma de cifras do numero
    sum_cifras = sumar_cifras(numero)
    solucuion = atopar_menor_suma_cifras_b(sum_cifras)
time_finish = time.time()
print("Temo do algoritmo B: ", time_finish - time_start)