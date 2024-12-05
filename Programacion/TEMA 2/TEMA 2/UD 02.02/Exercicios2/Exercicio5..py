__author__ = "Alvaro Camino Martinez"

x = int(input("Introduzca un numero:"))

y = int(input("Introduzca otro numero:"))

z = int(input("Introduzca otro numero:"))

if x == y or x == z or y == z:
    print ("Erro")

else:
    menor = min (x,y,z)
    print (f"O menor e {menor}")