'''
Escribe un script que pide ao usuario por teclado os coeficientes dunha ecuación de segundo grao e calcula a solución. Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda.

'''
__author__ = "Alvaro Camino Martinez"

#Ingresa los datos

a = float(input("Ingrese valor de a:"))
b = float(input("Ingrese valor de b:"))
c = float(input("Ingrese valor de c:"))

discriminante = b**2 -4 * a * c

if discriminante > 0:

    solucion1 = -b + discriminante**0.5
    solucion2 = -b - discriminante**0.5

    x = 2*a
    y = solucion1 / x
    z = solucion2 / x

    print (f"Las dos soluciones son {y} y {z}")

#Imprime las posibles soluciones

elif discriminante == 0:
    v = -b / 2*a
    print (f"La solucion es {v}")

else:
    print ("No tiene solucion")