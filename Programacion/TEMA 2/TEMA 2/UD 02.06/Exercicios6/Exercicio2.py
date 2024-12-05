"""Escribe un script que determine se unha cadea de texto introducida por teclado é un palíndromo. Un palíndromo é unha palabra ou frase que se le da mesma maneira de esquerda a dereita que de dereita a esquerda, ignorando espazos e maiúsculas. Se é palíndromo mostrará por pantalla É palíndromo e se non o é Non é palíndromo."""

__author__ = "Alvaro Camino Martinez"

# Solicita al usuario que introduzca una cadena de texto
cadena_texto = str(input("Introduzca una cadena de texto:"))

# Inicializa una cadena vacía para almacenar el texto procesado sin espacios
texto_nuevo = ""

# Recorre cada carácter (letra) de la cadena introducida por el usuario
for letra in cadena_texto:

# Si la letra no es un espacio, se añade a 'texto_nuevo'
    if letra != " ":
        texto_nuevo = texto_nuevo + letra

# Convierte el texto procesado a minúsculas para que la comparación no sea sensible a mayúsculas/minúsculas
texto_nuevo = texto_nuevo.lower()

# Crea una versión invertida del texto usando slicing
texto_reves = texto_nuevo [::-1]

# Compara el texto original (sin espacios y en minúsculas) con su versión invertida
if texto_reves == texto_nuevo:

# Si son iguales, se trata de un palíndromo
    print ("É palíndromo.")

else:

# Si no son iguales, no es un palíndromo
    print ("Non é palíndromo")