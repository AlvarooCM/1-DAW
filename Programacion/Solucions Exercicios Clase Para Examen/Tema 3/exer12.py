#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que elixirá no seu comezo un número ao azar entre 1 e 25. 
A continuación o usuario introducirá números por teclado ata que acerte o número seleccionado ao azar. 
Cada vez que se introduza un número incorrecto, o script proporcionaralle pistas ao usuario: “o número e maior” ou “o número é menor”. 
Unha vez que o usuario acerte o número, indicaráselle por pantalla se gañou o xogo ou non. Para gañar, o usuario deberá acertar o número en menos de 5 intentos.
"""

import random

__author__ = "Manuel Ramón Varela López"

# Configuracion do xogo
numero_mais_baixo = 1
numero_mais_alto = 25
numero_intentos = 5

# Collemos un numero que hai que adivinar
numero_adivinar = random.randint(numero_mais_baixo, numero_mais_alto)

# Construimos as mensaxes que se mostrara ao usuario
mensaxe = "Dame un numero entre " + str(numero_mais_baixo) + " e " + str(numero_mais_alto) + " incluidos: "

# Numero de intentos que levamos
intentos = 0

# Facemos un bucle
while True:

    # Pedimos un numero e sumamos un intento
    numero = int(input(mensaxe))
    intentos = intentos + 1

    # Miramos se acertamos ou se o numero e maior ou menor
    if numero == numero_adivinar:
        break
    elif numero > numero_adivinar:
        print("O numero a adivinar e mais pequeno")
    else:
        print("O numero a adivinar e mais grande.")

# Indicamoslle ao usuairo se ganou
if intentos > numero_intentos:
    print("GAME OVER")
else:
    print("WIN")