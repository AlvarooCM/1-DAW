"""
Escribe un script que pida ao usuario os coeficientes dunha ecuación de segundo grao e calcula as dúas solucións. Mostra as dúas solucións por pantalla.

"""

__author__ ="Alvaro Camino Martinez"

#Pedimos que ingrese los datos

a = int(input ("Ingrese el coeficiente de la ecuacion:"))

b = int(input ("Ingrese otro coeficiente de la ecuacion:"))

c = int(input ("Ingrese otro coeficiente de la ecuacion:"))

#Planteamos la formula

x = - b + (b**2 - 4 * a * c)**0.5

y = - b - (b**2 - 4 * a * c)**0.5

z = 2 * a

solucion1 = x / z

solucion2 = y / z

#Se imprime la solucion

print (f"A primeira solucion e {solucion1} e a segunda {solucion2}")


