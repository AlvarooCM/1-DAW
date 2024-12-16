#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script no que o usuario poida introducir números enteiros por teclado ata que teclee a palabra “fin”.
Tras finalizar a introdución de números, indícalle cal é o número máis pequeno introducido.
"""

__author__ = "Manuel Ramón Varela López"

# Ininializamos as variables
menor = None
primeira_iteracion = True

# Comezamos a recoller datos
while True:

    # Pedimoslle ao usuario que introduza datos
    mensaxe = input("Introduce un numero ou a palabra fin para finalizar: ")

    # Cando se escriba a plabra fin saimos do bucle
    if mensaxe == "fin":
        break

    # Convertimos o texto a numero enteiro
    numero = int(mensaxe)

    # Comprobamos que se e a primeira vez, asignemos o numero
    if primeira_iteracion:
        menor = numero
        primeira_iteracion = False

    # Comprobamos se o numero introducido era menor
    elif numero < menor:
        menor = numero

# Comprobamos se se meteu algun numero
if primeira_iteracion:
    print("Non se introduciu ningun numero")
# Imprimimos o menor dos numeros
else:
    print("O numero mais pequeno que se introduciu foi:", menor)