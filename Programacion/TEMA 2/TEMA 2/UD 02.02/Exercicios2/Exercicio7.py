__author__ = "Alvaro Camino Martinez"

ano = int(input("Introduzca un año:"))

if ano < 0:
    print ("Erro")

else:

    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        print ("Bisiesto")

    else:
        print("No bisiesto")




