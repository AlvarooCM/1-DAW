#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que calcule o mínimo común múltiplo de dous números introducidos polo usuario.
"""

__author__ = "Manuel Ramón Varela López"

# Pedimos 2 numeros maiores que 0
num1 = int(input("Introduce un número positivo maior que 0: "))
num2 = int(input("Introduce outro número positivo maior que 0: "))

if num1 > 0 and num2 > 0:
    # Collemos o número máis grande
    if num1 > num2:
        maior = num1
    else:
        maior = num2

    # Buscamos aquel numero que e divisible polos dous numeros
    # while not (maior % num1 == 0 and maior % num2 == 0):
    while (maior % num1 != 0) or (maior % num2 != 0):
        maior = maior + 1
    
    # Imprimimos o mcm
    print("O mcm e", maior)

else:
    print("Introduce números maiores que 0.")