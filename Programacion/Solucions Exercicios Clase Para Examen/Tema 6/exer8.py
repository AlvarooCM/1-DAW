#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Queremos realizar un programa que calcule o índice dunha chave para un dicionario utilizando o algoritmo de *hashing por folding*. 
O programa recibirá en orde os seguintes parámetros: tamaño da táboa, número de división por *folding* e a chave.  
"""

__author__ = "Manuel Ramón Varela López"


# Collemos os datos

while True:
    try:
        n = int(input("Tamaño da táboa: "))
        break
    except:
        print("Introduce un número")


while True:
    try:
        h = int(input("Indica cada canto realizamos a división de números: "))
        break
    except:
        print("Introduce un número")

chave = input("Indica a chave: ")


# Primeiro debemos recorrer a chave para ir collendo o codigo ASCII de cada letra
# Almacenamos este codigo nunha cadea concatenando cada número en formato texto
concatenacion_numeros = ""
for letra in chave:
	codigo = ord(letra)
	concatenacion_numeros = concatenacion_numeros + str(codigo)

# Nesta variable collemos a suma total de tódolos números
suma = 0
while len(concatenacion_numeros) > 0:
	# Comprobamos se a division por holding e maior ou igual que o tamaño da concatenacion do numero
	if len(concatenacion_numeros) >= h:
		# COllemos a division de folding segundo o tamaño desta
		numero_str = concatenacion_numeros[:h]
		# A concatenacion de numeros quitamoslle o numero da division por holding
		concatenacion_numeros = concatenacion_numeros[h:]
	else: # Temos menos letras que a división por holding
		numero_str = concatenacion_numeros # O numero a str son todolos numeros que quedan
		concatenacion_numeros = "" # Esta variable queda baleira para sair do bucle

	# Pasamos a enteiro o numero por division de holding e acumulamolo na suma
	suma += int(numero_str)

# Calculamos o resto da suma entre o tamaño da lista para obter o índice
indice = suma % n
print(indice)

