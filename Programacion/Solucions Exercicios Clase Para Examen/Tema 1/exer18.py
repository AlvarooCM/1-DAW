#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida ao usuario 3 números e móstralle por pantalla a media dos 3 números.
"""

__author__ = "Manuel Ramón Varela López"

# Pedimos os datos aos números
num1 = float(input("Por favor, introduza o primeiro número: "))
num2 = float(input("Por favor, introduza o segundo número: "))
num3 = float(input("Por favor, introduza o terceiro número: "))

# CAlculamos a media
media = (num1 + num2 + num3) / 3

# Mostramos o resultado
print("A media é", media)
