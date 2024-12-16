#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que reciba un enteiro (n) maior ou igual a 1 e ofreza o resultado da seguinte suma: 1 + 1/2 + 1/3 + … 1/n
"""


__author__ = "Manuel Ramón Varela López"

# Pedimos o numero enteiro
n = int(input("Introduce un número positivo maior que 0: "))

# Comprobamos que sexa maior que 0
if n > 0:
    # Variable para facer a iteracion
    i = 1
    # Acumulamos a solucion neste resultado
    resultado = 0.0
    # Realizamos a suma ata chegar ao número N
    while i <= n:
        resultado = resultado + (1.0/i)
        i = i + 1
    print(resultado)
else:
    print("O número é menor que 0")

