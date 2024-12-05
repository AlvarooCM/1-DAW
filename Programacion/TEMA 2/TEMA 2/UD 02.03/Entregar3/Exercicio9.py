"""
Escribe un script que permita obter o factorial dun número enteiro positivo introducido por teclado.

"""

__author__ = "Alvaro Camino Martinez"

# Pedimos la introducion de 1 numero al usuario.

n = int(input("Introduzca un numero entero positivo:"))

factorial = 1

i = 1

# Inicializamos bucle.

while i <= n:
    factorial = factorial * i
    i = i + 1

# Imprimimos solucion.

print (f"O factorial de {n} e {factorial}.")