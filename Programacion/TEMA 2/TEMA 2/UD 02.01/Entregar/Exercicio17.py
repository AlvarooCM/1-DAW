"""
 Escribe un script que pida ao usuario o número de quilómetros recorridos na súa última viaxe en coche, o consumo do coche en litros cada 100 quilómetros e o prezo en euros dun litro de combustible. Calcula o custo da viaxe e móstrallo ao usuario por pantalla.
"""

__author__ ="Alvaro Camino Martinez"

#Pedimos que ingrese los datos

kilometros = float(input("Introduce el numero de kilometros recorridos en su ultimo viaje en coche:"))

consumo = float(input("Introduce el consumo del coche en litros cada 100 kilometros:"))

precio = float(input("Introduce el precio en euros de un litro de combustible:"))

preciojasoil = (precio * 1 * consumo / 100)

costototal = (kilometros * preciojasoil)

#Imprimimos la solucion

print (f"El costo total del viaje fue de {costototal} euros")
