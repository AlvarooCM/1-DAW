'''
Escribe un script que reciba por teclado un número enteiro positivo N. O programa mostrará por pantalla nesta orde:

O número de pares entre 1 e N incluídos.
O número de impares entre 1 e N incluídos.
A suma total de todos os números entre 1 e N incluídos.
A media só dos números pares entre 1 e N incluídos.

'''

__author__ = "Alvaro Camino Martínez"

n = int(input("Introduzca un número:"))

# Iterador

a = 1

# Acumuladores

numeros_pares = 0
numeros_impares = 0
suma_total = 0
suma_pares = 0

while a <= n:
    suma_total = suma_total + a
    if a % 2 == 0:
        numeros_pares = numeros_pares + a
        suma_pares = suma_pares + a
    else:
        numeros_impares = numeros_impares + a
    
    a = a + 1

if numeros_pares > 0:
    media_pares = suma_pares / numeros_pares
else:
    media_pares = 0

print(numeros_pares)
print(numeros_impares)
print(suma_total)
print(media_pares)







