#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe unha función `calcular_desconto_irpf(soldo_bruto: float, irpf: int) -> float` nun *script* o soldo bruto e o irpf en tanto por cen. 
Comproba que estes dous valores son números, que o soldo é maior que 0 e que o IRPF é un valor válido. 
Se algunha destas condicións non se cumpre, lanza a excepción `ValueError`. 
O propio *script* deberá recibir estes datos por teclado, e utilizar a función creada para calcular o desconto do IRPF. 
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

def calcular_desconto_irpf(soldo_bruto, irpf):
    """
    Calcula o desconto do IRFP

    Args:
        soldo_bruto (float): o soldo bruto
        irpf (int): o irpf en tanto por cen

    Returns:
        float: o desconto do irfp

    Raises:
        ValueError: Se os valores introducidos non son válidos
    """
    # Comprobamos que os valores sexan válidos
    if not comprobar_int_ou_float(soldo_bruto):
        raise ValueError
    if not comprobar_int_ou_float(irpf):
        raise ValueError
    if soldo_bruto < 0:
        raise ValueError
    if irpf > 100 or irpf < 0:
        raise ValueError
    
    # Realizamos a operación
    return soldo_bruto * (1 - irpf / 100)

## Programa principal

# Pedimos o soldo
while True:
    try:
        soldo = float(input("Introduza o soldo bruto: "))
        break
    except:
        print("Introduce un número")

# pedimos o IRPF
while True:
    try:
        irpf = float(input("Introduza o irpf en tanto por cen: "))
        break
    except:
        print("Introduce un número")

# CAlculamos o salario
try:
    print(calcular_desconto_irpf(soldo, irpf))
except:
    print("Os valores introducidos non son correctos")

    