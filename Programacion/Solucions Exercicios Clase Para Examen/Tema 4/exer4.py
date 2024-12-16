#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un *script* que pide ao usuario os coeficientes dunha ecuación de segundo grao e calcula a solución. Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda. Crea as seguintes funcións:

- Unha función que calcule o discriminante: `descriminante(a: float, b: float, c: float) -> float`

- Unha función que calcule o número de solucións: `numero_solucions(a: float, b: float, c: float) -> int`

- Unha para calcular a solución cando esta é única: `solucion_unica(a: float, b: float) -> float`

- Cando haxa dúas solucións crearemos dúas funcións distintas; unha para a solución do "+", `solucion_positiva(a: float, b: float, c: float) -> float` e outra para a do "-", `solucion_negativa(a: float, b: float, c: float): float`. 

Estas dúas funcións e a de `numero_solucions` deben de utilizar internamente a función `descriminante`.
"""


__author__ = "Manuel Ramón Varela López"

def descriminante(a, b, c):
    """
    Función que calcula o descirminante dunha ecuación de segundo grao

    Args:
        a (float): coeficiente a
        b (float): coeficiente b
        c (float): coeficiente c

    Returns:
        (float): O valor do descriminante 
    """
    return b ** 2 - 4 * a * c

def numero_solucions(a, b, c):
    """
    Función que calcula o número de solucións dunha ecuación de segundo grao

    Args:
        a (float): coeficiente a
        b (float): coeficiente b
        c (float): coeficiente c

    Returns:
        (int): A cantidade de solucions, 0, 1 ou 2
    """
    dis = descriminante(a, b, c)
    if dis > 0:
        return 2
    elif dis == 0:
        return 1
    else:
        return 0

def solucion_unica(a, b, c):
    """
    Función que calcula a solución única cando unha ecuación de segundo grao ten unha única solución

    Args:
        a (float): coeficiente a
        b (float): coeficiente b
        c (float): coeficiente c

    Returns:
        (float): A solución
    """
    return -b / (2 * a)

def culcula_duas_solucions(a, b, c):
    """
    Función que calcula las dos soluciones de una ecuación de segundo grado

    Args:
        a (float): coeficiente a
        b (float): coeficiente b
        c (float): coeficiente c

    Returns:
        (float, float): Devuelve las dos soluciones
    """
    sol1 = (-b + descriminante(a, b, c)**0.5) / (2 * a)
    sol2 = (-b - descriminante(a, b, c)**0.5) / (2 * a)
    return sol1, sol2


    
########## Programa principal

# Pedimos os datos
a = float(input("Introduce o coeficiente a: "))
b = float(input("Introduce o coeficiente b: "))
c = float(input("Introduce o coeficiente c: "))

# Calculamos o numero de solucións
num_solucions = numero_solucions(a, b, c)

# Segundo o numero de solucions imprimimos estas
if num_solucions == 2:
    s1, s2 = culcula_duas_solucions(a, b, c)
    print("As solucions son", s1, "e", s2)
elif num_solucions == 1:
    print("A solucion é:", solucion_unica(a, b, c))
else:
    print("Non hai solucións reais")

