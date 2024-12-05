__author__ = "Alvaro Camino Martinez"

km = int(input("Introduzca el numero de km recorridos:"))
peso = int(input("Introduzca el peso de su vehiculo:"))
peso_toneladas = peso /1000

print ("Elija su vehiculo:")
print ("\ta) Moto")
print ("\tb) Turismo")
print ("\tc) Camión")

opcion = input (">")

if opcion == 'a':
    print (f"El importe es de 1€")
elif opcion == 'b':
    print (f"El importe es de {0.25 * km}€")
elif opcion == 'c':
    print (f"El importe es de {0.25 * km + peso_toneladas * 0.15}€")
else:
    print ("Error")