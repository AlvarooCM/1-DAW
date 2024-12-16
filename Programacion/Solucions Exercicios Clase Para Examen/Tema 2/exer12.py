#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida o nome de usuario e contrasinal ao usuario. 
Indica se o inicio de sesión é correcto. 
O nome de usuario sería “python” e o contrasinal “pip”.
"""

__author__ = "Manuel Ramón Varela López"

username = input("Introduce o nome de usuario: ")
password = input("Introduce o contrasinal: ")

if username == "python" and password == "pip":
    print("Benvido!")
else:
    print("As credenciais utilizadas son incorrectas")