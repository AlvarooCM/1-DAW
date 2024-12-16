#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida ao usuario o seu nome e apelidos por separado e mostra a seguinte mensaxe por pantalla: 
O usuario <apelido1> <apelido 2>, <nome> rexistrouse correctamente.
"""

__author__ = "Manuel Ramón Varela López"

# Pedimos ao usuario os datos
nome = input("Introduza o seu nome: ")
apelido1 = input("Introduza o seu primeiro apelido: ")
apelido2 = input("Introduza o seu segundo apelido: ")

# Construimos a mensaxe concatenando texto
mensaxe = "O usuario " + apelido1 + " " + apelido2 + ", " + nome + " rexistrouse correctamente."

# imprimimos o resultado
print(mensaxe)
