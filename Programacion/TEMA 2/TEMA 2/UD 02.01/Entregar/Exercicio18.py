"""
Escribe un script que pida ao usuario 3 números e móstralle por pantalla a media dos 3 números.
"""

__author__="Alvaro Camino Martinez"

#Pedimos que ingrese los datos correspondientes

numero1 = int(input("Ingrese un numero:"))

numero2 = int(input("Ingrese un numero:"))

numero3 = int(input("Ingrese un numero:"))

media = (numero1 + numero2 + numero3)/3

#Imprimimos la solucion

print (f"A media dos seguintes numeros e {media}")