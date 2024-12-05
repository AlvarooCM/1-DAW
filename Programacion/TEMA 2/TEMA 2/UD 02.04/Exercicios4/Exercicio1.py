"""
    Escribe unha función nun script que informe se un número é par ou impar. Esta algoritmo debe ir dentro dunha función definida como:
"""

__author__ = "Alvaro Camino Martinez"

def comprobar_par(numero: int) -> bool:
    
    if numero % 2 == 0:
        return True
    else:
        return False

# Pedimos un número
numero = int(input("Ingrese un numero por consola: "))

# Comprobamos ca función se é nulo o número que se lle pasa por argumento
e_par = comprobar_par(numero)

if e_par:
    print("Par")
else:
    print("Impar")
    