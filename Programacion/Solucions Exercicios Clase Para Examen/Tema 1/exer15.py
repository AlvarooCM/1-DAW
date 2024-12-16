#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida ao usuario os coeficientes dunha ecuación de segundo grao e calcula as dúas solucións. 
Mostra as dúas solucións por pantalla.
"""

__author__ = "Manuel Ramón Varela López"

# Pedimos os datos ao usuario
a = float(input("Por favor, introduza o valor de a: "))
b = float(input("Por favor, introduza o valor de b: "))
c = float(input("Por favor, introduza o valor de c: "))

# Realizamos os calculos
descriminante = b ** 2 - 4 * a * c
raiz = descriminante ** (1/2)
solucion1 = (-b + raiz) / (2 * a)
solucion2 = (-b - raiz) / (2 * a)

# Imprimimos a solucion
print("As solucións son as seguintes:", solucion1, "e", solucion2)
