"""Vaise realizar un sorteo no que pode haber un número diferente de gañadores a partir dunhas rifas numeradas entre 0001e 9999. Escribe un script que reciba por teclado o número de premios dispoñibles e imprima os números premiados co formato de 4 díxitos."""

__author__ = "Alvaro Camino Martinez"

import random

# Solicitar el número de premios
numero_premios = int(input("Introduce el número de premios que quiere tener:"))

# Lista para almacenar los números premiados
numero_premiados = []

# Generar los números premiados
for _ in range(numero_premios):
    numero_aleatorio = random.randint(1, 9999)
    numero_premiados.append(f"{numero_aleatorio:04d}")

# Imprimir los números premiados
print("Números premiados:")
for numero in numero_premiados:
    print(numero)
