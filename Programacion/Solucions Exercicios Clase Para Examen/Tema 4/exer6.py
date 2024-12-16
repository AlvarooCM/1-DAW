#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida o nome de usuario e contrasinal ao usuario. Indica se o inicio de sesión é correcto. 
O nome de usuario correcto sería “python” e o contrasinal “pip”. 
Crea a función login(usuario: str, contrasinal: str) -> boolean para realizar esta operación.
"""


__author__ = "Manuel Ramón Varela López"


def login(usuario, contrasinal):
    """
    Función que indica se un login se realizou corectamente

    Args:
        usuario (float): O nome de usuario que se desexa loguear
        contrasinal (float): O seu respectivo contrasinal

    Returns:
        (boolean): Verdadeiro se o usuairo ten acceso, falso en caso contrario
    """
    if usuario == "python" and contrasinal == "pip":
        return True
    else:
        return False

# Pedimos os datos
usuario = input("Introduce o nome de usuario: ")
contrasinal = input("Introduce o teu contrasinal: ")

# Comprobamos o acceso
if login(usuario, contrasinal):
    print("Inicio de sesión correcto.")
else:
    print("Acceso non autorizado.")