"""Realiza a implantación da función descifra_cesar(texto: str, desprazamento: int): str nun script que descifre unha cadea cifrada con cifrado César. Lanza tamén excepción ValueError se os argumentos da función son do tipo de datos inválidos.

O propio script debe utilizar dita función para descifrar un texto introducido polo usuario para mostrar o texto descifrado por pantalla. O usuario tamén indicará por teclado o desprazamento."""

__author__ = "Alvaro Camino Martinez"

# Defino una funcion que calcula y devuelve el resultado del descirfrado.

def descifra_cesar(texto: str, desprazamento: int) -> str:

    """_summary_

    Raises:
        ValueError: Error de tipo de datos mal introducido

    Returns:
        _type_: Devuelve el resultado del cifrado cesar
    """

# Primero de todo compruebo que el tipo de datos que introduce el usuario son validos.

    if type(texto) is not (str) or type(desprazamento) is not (int):
        raise ValueError("Tipo de datos no validos, vuelva a intentarlo.")
    
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

# Iniciamos el for para buscar en que posicion se encuentra cada caracter en el abecedario para descifrar.

    for char in texto:
 
        if char in abecedario:

            posicion = abecedario.index (char)

            posicion_nueva = (posicion - desprazamento) % 26

            resultado = resultado + abecedario [posicion_nueva]

        else:
            resultado = resultado + char

    return resultado

# Iniciamos un try y pedimos al usuario que introduzca los datos e imprimimos resultados

try: 

    texto = str(input("Introduzca alguna cadena de texto:"))
    desprazamento = int(input("Introduzca el desplazamiento de cifrado:"))
    texto_descifrado = descifra_cesar (texto, desprazamento)
    print ("Texto descifrado:", texto_descifrado)

except ValueError:
    print ("Tipo de datos no validos, vuelva a intentarlo.")
