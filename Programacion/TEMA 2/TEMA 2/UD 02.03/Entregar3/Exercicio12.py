"""
Escribe un script que elixirá no seu comezo un número ao azar entre 1 e 25. A continuación o usuario introducirá números por teclado ata que acerte o número seleccionado ao azar. Cada vez que se introduza un número incorrecto, o script proporcionaralle pistas ao usuario: “o número e maior” ou “o número é menor”. Unha vez que o usuario acerte o número, indicaráselle por pantalla se gañou o xogo ou non. Para gañar, o usuario deberá acertar o número en menos de 5 intentos.
"""

__author__ = "Alvaro Camino Martinez"

import random
numero_aleatorio = random.randint(1, 25)

contador = 0

# Inicializamos el bucle mas imprimimos las posibles soluciones/pistas.

while True:

    numero = int(input("Introduzca un numero del 1 al 25:"))

    if numero == numero_aleatorio:
        print ("Has acertado.")
        break

    if numero > numero_aleatorio:
        print ("Pista: El numero es menor.")

    if numero < numero_aleatorio:
        print ("Pista: El numero es mayor.")

    contador += 1

# Imprimimos lo que pasa al superar el limite de intentos.

if contador > 5:
    print("Has perdido, has superado el limite de intentos.")
else:
    print("Has ganado.")