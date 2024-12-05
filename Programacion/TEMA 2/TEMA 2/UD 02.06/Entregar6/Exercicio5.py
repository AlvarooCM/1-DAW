"""O cifrado César é un tipo de cifrado de substitución no que unha letra do texto orixinal é substituída por outra letra que é un número fixo de posicións posteriores no alfabeto.

Por exemplo se o desprazamento é 5, a "a" cifrarase coa "f". Débense ignorar os espazos en branco.

Se nun desprazamento rematan as letras, volverase a comezar polo comezo do alfabeto.

Supoñer que todos os nomes están en minúsculas e están compostos só polas seguintes letras: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.

Realiza a implantación deste algoritmo na función cifra_cesar(texto: str, desprazamento: int): str. Recorda que os caracteres diferentes as letras se deben manter. Comproba se o tipo de datos introducidos son válidos, e senón é así lanza unha excepción ValueError.

O propio script debe utilizar ditas función para cifrar un texto introducido polo usuario para mostrar o texto cifrado por pantalla. O usuario tamén indicará por teclado o desprazamento. Ademais recorda capturar a excepción."""

__author__ = "Alvaro Camino Martinez"

# Defino una funcion que calcula y devuelve el resultado del cifrado.

def cifra_cesar(texto: str, desprazamento: int) -> str:

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

            posicion_nueva = (posicion + desprazamento) % 26

            resultado = resultado + abecedario [posicion_nueva]

        else:
            resultado = resultado + char

    return resultado

# Iniciamos un try y pedimos al usuario que introduzca los datos e imprimimos resultados

try: 

    texto = str(input("Introduzca alguna cadena de texto:"))
    desprazamento = int(input("Introduzca el desplazamiento de cifrado:"))
    texto_cifrado = cifra_cesar (texto, desprazamento)
    print ("Texto cifrado:", texto_cifrado)

except ValueError:
    print ("Tipo de datos no validos, vuelva a intentarlo.")