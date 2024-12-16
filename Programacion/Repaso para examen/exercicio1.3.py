"""Escribe unha función nun script que informe se un número é par ou impar. Esta algoritmo debe ir dentro dunha función definida como:

comprobar_par(numero: int) -> boolean
En dito script, utiliza dita función para comprobar se un número que introduce un usuario é par ou impar. Se é par, imprime Par e senón Impar.

"""

__author__ = "Alvaro Camino Martinez"

def comprobar_par(numero: int) -> bool:

    if numero % 2 == 0:
        return True
    else:
        return False

numero = int (input("Introduce un numero:"))

e_par = comprobar_par(numero)

if e_par:
    print("Par")
else:
    print("Impar")

