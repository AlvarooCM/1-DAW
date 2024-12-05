"""
Escribe un script que calcule o mínimo común múltiplo de dous números introducidos polo usuario.
"""

__author__ = "Alvaro Camino Martinez"

# Pedimos la introducion de 2 numeros

n1 = int(input("Introduzca un numero:"))

n2 = int(input("Introduzca un segundo numero:"))

if n1 > n2:
    mcm = n1
else:
    mcm = n2

# Iniciamos el bucle

while True:
    if mcm % n1 == 0 and mcm % n2 == 0:
        break
    mcm += 1

# Imprimimos solucion

print (f"El mcm de los 2 numeros es de {mcm}")




