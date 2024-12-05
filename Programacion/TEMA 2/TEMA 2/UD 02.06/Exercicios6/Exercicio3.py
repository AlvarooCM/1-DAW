"""Escribe un script que elimine todas as consoantes dunha cadea de texto introducida por teclado e devolva unha nova cadea só coas vocais e outros caracteres. Mostra este texto por pantalla."""

__author__ = "Alvaro Camino Martinez"

# Solicita al usuario que introduzca una cadena de texto
cadena_texto = str(input("Introduce una cadena de texto:"))

# Inicializa una cadena vacía donde se almacenará el texto modificado
nova_cadea = ""

# Recorre cada carácter (letra) de la cadena introducida por el usuario
for letra in cadena_texto:

# Obtiene el código ASCII del carácter actual usando ord()
    codigo = ord(letra)

# Verifica si el código ASCII corresponde a una letra mayúscula (A-Z)
    if codigo >= 65 and codigo <= 90:

# Si la letra es una vocal mayúscula (A, E, I, O, U), se añade a 'nova_cadea'
        if letra in "AEIOU":

            nova_cadea = nova_cadea + letra
# Verifica si el código ASCII corresponde a una letra minúscula (a-z)
    elif codigo >= 97 and codigo <= 122:

# Si la letra es una vocal minúscula (a, e, i, o, u), se añade a 'nova_cadea'
        if letra in "aeiou":

            nova_cadea = nova_cadea + letra

# Si el carácter no es una letra (es decir, no está en los rangos anteriores), se añade a 'nova_cadea' tal como está
    else:
        nova_cadea = nova_cadea + letra
        
# Imprime la cadena modificada, que contiene solo las vocales
print (nova_cadea)

