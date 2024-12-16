#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe unha función raiz_cadrada(numero: float) -> float nun script que calcule a raíz cadrada dun número. 
Se o parámetro non é un número ou é negativo, lanza unha excepción chamada ValueError. 
O propio script debe recibir un número por parte do usuario e calcula a raíz cadrada dese número utilizando a función creada anteriormente. 
Captura a excepción que lanza a función.
"""


__author__ = "Manuel Ramón Varela López"

def comprobar_int_ou_float(valor):
    """
    Comproba se un valor e un numero

    Args:
        valor (*): un valor

    Returns:
        float: vardairo se un número, falso en caso contrario

    """
    if type(valor) is int or type(valor) is float:
        return True
    return False


def raiz_cadrada(numero):
    """
    Calcula a raiz cadrada dun numero

    Args:
        numero (float): o número do que se vai calcular a raiz

    Returns:
        float: o raiz cadrada do número

    Raises:
        ValueError: Se os valores introducidos non son válidos
    """
    # Comprobamos que os valores sexan válidos
    if not comprobar_int_ou_float(numero):
        raise ValueError
    if numero < 0:
        raise ValueError
    
    return numero**(1/2)



# pedimos un número
while True:
    try:
        numero = float(input("Introduza un numero: "))
        break
    except:
        print("Introduce un número")

try:
    print(raiz_cadrada(numero))
except:
    print("Os valores introducidos non son correctos")
