#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Vaise realizar un sorteo no que pode haber un número **diferente** de gañadores a partir dunhas rifas numeradas entre `0001`e `9999`. 
Escribe un *script* que reciba por teclado o número de premios dispoñibles e imprima os números premiados co formato de 4 díxitos."""


__author__ = "Manuel Ramón Varela López"

import random

numero_premiados = int(input("Introduce o número de premiados: "))

# Nesta lista gardamos os premiados
premiados = []

# Comprobamos se temos o número de premiados necesarios
while len(premiados) < numero_premiados:
    # Collemos un novo número
    numero_aleatorio = random.randint(1, 9999)
    # Se ainda non saiu, engadimolo a lista
    if numero_aleatorio not in premiados:
        premiados.append(numero_aleatorio)

# Recorremos tódolos gañadore para imprimir a lista
for ganador in premiados:
    # Pasamolo a numero
    numero_str = str(ganador)
    # Collemos o tamaño do numero
    tam_numero = len(numero_str)
    # Engadimos o número de 0 necesarios antes do número
    numero_str = (4 - tam_numero) * "0" + numero_str
    # Imprimimos o número
    print(numero_str)
