"""Escribe un script que en Python que conte o número de vogais nunha cadea de texto introducida por teclado. Por último imprimirá por pantalla o número de vogais. Recorda contar tanto as maiúsculas como as minúsculas."""

__author__ = "Alvaro Camino Martinez"

#Solicita al usuario que introduzca una cadena de texto
cadena_texto = str(input("Introduce una cadena de texto:"))

# Inicializa un contador para las vogal
contador_vogais = 0

# Recorre cada carácter (letra) de la cadena introducida por el usuario
for letra in cadena_texto:

# Comprueba si la letra es una vogal
    if letra == "a" or letra == "A":

# Incrementa el contador si la letra es 'a' o 'A'
        contador_vogais = contador_vogais + 1

    elif letra == "e" or letra == "E":

# Incrementa el contador si la letra es 'e' o 'E'
        contador_vogais = contador_vogais + 1

    elif letra == "i" or letra == "I":

# Incrementa el contador si la letra es 'i' o 'I'
        contador_vogais = contador_vogais + 1

    elif letra == "o" or letra == "O":

 # Incrementa el contador si la letra es 'o' o 'O'      
        contador_vogais = contador_vogais + 1

    elif letra == "u" or letra == "U":

# Incrementa el contador si la letra es 'u' o 'U'
        contador_vogais = contador_vogais + 1

# Imprime el número total de vogais encontradas en la cadena
print (f"Ten {contador_vogais} vogais")



        