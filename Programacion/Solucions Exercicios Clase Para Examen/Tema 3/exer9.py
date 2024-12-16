#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que permita obter o factorial dun número enteiro positivo introducido por teclado.
"""
__author__ = "Manuel Ramón Varela López"

# Pedimos o numero enteiro
n = int(input("Introduce un número positivo maior que 0: "))

# Comprobamos que sexa maior que 0
if n > 0:
    # Variable para facer a iteracion
    i = 1
    # Acumulamos a solucion neste resultado
    resultado = 1
    # Realizamos a multiplicación ata chegar a N
    while i <= n:
        resultado = resultado * i
        i = i + 1
    print(resultado)
else:
    print("O número é menor que 0")