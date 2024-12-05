"""Escribe un script en Python que conte o número de palabras nunha cadea de texto introducida por teclado e o mostre por pantalla. Considera que as palabras están separadas por un ou máis espazos. Coidado cos dobres, triples ou máis espazos e cos espazos ao comezo e o final do texto."""

__author__ = "Alvaro Camino Martinez"

# Solicita al usuario que introduzca una cadena de texto
cadena_texto = str(input("Introduce una cadena de texto:"))

# Inicializa una variable para almacenar la letra anterior en el bucle
letra_anterior = None

# Inicializa una cadena vacía que almacenará la versión de la cadena sin múltiples espacios consecutivos
novo_texto = ""

# Recorre cada carácter (letra) de la cadena introducida por el usuario
for letra in cadena_texto:

# Si el carácter actual es un espacio y el anterior no lo era, añade un único espacio a 'novo_texto'
    if letra == " " and letra_anterior != " ":

        novo_texto = novo_texto + letra

# Si el carácter actual no es un espacio, añádelo a 'novo_texto'
    elif letra != " ":

        novo_texto = novo_texto + letra

# Actualiza 'letra_anterior' para almacenar el carácter actual
    letra_anterior = letra

# Elimina los espacios en blanco al principio y al final de 'novo_texto'
novo_texto = novo_texto.strip()

# Inicializa un contador para el número de palabras
numero_palabras = 0

# Comprueba si 'novo_texto' no está vacío
if len(novo_texto) > 0:

# Recorre cada carácter de 'novo_texto' para contar los espacios
    for letra in novo_texto:

# Si se encuentra un espacio, incrementa el contador de palabras
        if letra == " ":

            numero_palabras = numero_palabras + 1

# Añade 1 al contador, porque el número de palabras es el número de espacios + 1
    numero_palabras = numero_palabras + 1

else:
# Si 'novo_texto' está vacío, el número de palabras es 0
    numero_palabras = 0

# Imprime el número total de palabras
print (numero_palabras)