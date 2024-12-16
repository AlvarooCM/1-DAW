#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pide ao usuario por teclado os coeficientes dunha ecuación de segundo grao e calcula a solución. 
Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda.
"""

__author__ = "Manuel Ramón Varela López"

# Pedimos os coeficientes da ecuación
a = float(input("Introduce o coeficiente a: "))
b = float(input("Introduce o coeficiente b: "))
c = float(input("Introduce o coeficiente c: "))


# Calculamos o discriminante
discriminante = b ** 2 - 4 * a * c

# Cando o discriminante é maior que 0, a ecuación ten dúas solucións
if discriminante > 0:
    # Calculamos as dúas solucións
    solucion_1 = (-b + discriminante ** 0.5) / (2 * a)
    solucion_2 = (-b - discriminante ** 0.5) / (2 * a)
    print("As solucións son: ", solucion_1, "e", solucion_2)

# Se o discriminante é igual a 0, temos unha solución
elif discriminante == 0:
    solucion = -b / (2 * a)
    print("A solución é", solucion)

# Se o discriminante é menor que 0, a ecuación non ten solución
else:
    print("A ecuación non ten solución")
