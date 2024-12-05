__author__ = "Alvaro Camino Martinez"

primernum = int(input("Ingrese un numero:"))
segundonum = int(input("Ingrese otro numero:"))


print("Elija una opcion:")
print("\ta) Opcion a")
print("\tb) Opcion b")
print("\tc) Opcion c")

opcion = input (">")

if opcion == 'a':
    print (f"El resultado es {primernum + segundonum}")
elif opcion == 'b':
    print (f"El resultado es {primernum - segundonum}")
elif opcion == 'c':
    print (f"El resultado es {primernum * segundonum}")
else:
    print ("Error")
