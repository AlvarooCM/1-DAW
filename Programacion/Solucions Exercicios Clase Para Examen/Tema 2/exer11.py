#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que faga o cambio de divisas tanto de euros a libras e viceversa. 
Crea un menú para que o usuario escolla o cambio que desexa realizar e a continuación introducirá o valor da moeda correspondente 
para realizar o cambio de divisas. 1 € son 1,10 libras.
"""

__author__ = "Manuel Ramón Varela López"

# Valor de 1 € en libras
euro_libras = 1.10

# Mostramos o menú
print("Elixe unha das opcions:")
print("\ta) Cambio de euros a libras")
print("\tb) CAmbio de libras a euros")
print("\tCalquera outro caracter para sair")
eleccion = input("> ")

# Eliximos a opción do menu
# Opcion 1: de euros a libras
if eleccion == "a":
    
    # Pedimos os datos ao usuario
    euros = float(input("Introduce os euros: "))
    
    # Calculamos as libras
    libras = euros * euro_libras
    print(euros,"euros son",libras,"libras")

# Opcion 2: de libras a euros
elif eleccion == "b":
    
    # Pedimos os datos ao usuario
    libras = float(input("Introduce as libras: "))
    
    # Calculamos as libras
    euros = libras * (1/euro_libras)
    print(libras,"libras son",euros,"euros")

# Escollese sair
else:
    print("Adios")