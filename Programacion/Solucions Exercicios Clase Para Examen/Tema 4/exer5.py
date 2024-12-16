#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un *script* que faga o cambio de divisas tanto de euros a libras e viceversa. Crea un menú para que o usuario escolla o cambio que desexa realizar. Realiza unha función para cada un dos cambios:

- `libras_to_euros(euros: float) -> float`
- `euros_to_libras(libras: float) -> float`

> Un € é igual a 1,10 libras
"""


__author__ = "Manuel Ramón Varela López"

## Variables globais

equivalencia_euro_libras = 1.10

## Funcións

def libras_to_euros(libras):
    """
    Función que devolve a equivalencia de euros dunha cantidade de libras
    
    Args:
        libras (float) : a cantidade de libras

    Return:
        (float) : o cambio en euros
    """
    return libras / equivalencia_euro_libras

def euros_to_libras(euros):
    """
    Función que devolve a equivalencia de libras dunha cantidade de euros
    
    Args:
        euros (float) : a cantidade de euros

    Return:
        (float) : o cambio en libras
    """
    return euros * equivalencia_euro_libras

## Programa principal

print("Elixe a opción que desexas: ")
print("\a) Pasar de libras a euros")
print("\b) Pasar de euros a libras")
opcion = input("> ")

if opcion == "a":
    libras = float(input("Introduza a cantidade de libras: "))
    print(libras_to_euros(libras), "€")
elif opcion == "b":
    euros = float(input("Introduza a cantidade de euros: "))
    print(euros_to_libras(euros), "libras")
else:
    print("Opcion incorrecta")

