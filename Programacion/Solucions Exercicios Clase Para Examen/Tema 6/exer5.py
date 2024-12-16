#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
O cifrado César é un tipo de cifrado de substitución no que unha letra do texto orixinal é substituída por outra letra que é un número fixo de posicións posteriores no alfabeto.

Por exemplo se o desprazamento é 5, a 'a' cifrarase coa 'f'. Débense ignorar os espazos en branco.

Se nun desprazamento rematan as letras, volverase a comezar polo comezo do alfabeto.

Supoñer que todos os nomes están en minúsculas e están compostos só polas seguintes letras: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.

Realiza a implantación deste algoritmo na función `cifra_cesar(texto: str, desprazamento: int): str`. Recorda que os caracteres diferentes as letras se deben manter. Comproba se o tipo de datos introducidos son válidos, e senón é así lanza unha excepción `ValueError`.

O propio *script* debe utilizar ditas función para cifrar un texto introducido polo usuario para mostrar o texto cifrado por pantalla. O usuario tamén indicará por teclado o desprazamento. Ademais recorda capturar a excepción.
"""

__author__ = "Manuel Ramón Varela López"

def cifra_cesar(texto, desprazamento):
    """
    Args:
        texto (str) : o texto a traducir
        desprazamento (int) : o desprazamento para realizar o cifrado cesar

    Returns:
        str : o texto cifrado

    Raises:
        ValueError: lanza excepción se os valors dos argumentos son inválidos.
    """

    # Comprobamos o tipo de datos
    if type(texto) is not str:
        raise ValueError
    if type(desprazamento) is not int:
        raise ValueError

    # Collemos o número de letras
    número_de_letras = (ord("z") - ord("a")) + 1 

    # Se o desprazamento é maior ou igual número de letras
    if desprazamento >= número_de_letras:
        desprazamento = desprazamento % número_de_letras
    
    # COllemos os codigos ASCII de a e z
    codigo_a = ord('a')
    codigo_z = ord('z')

    # Nesta variable gardaremos o texto cifrado
    texto_cifrado = ""

    # recorremos cada letra do texto
    for letra in texto:
        # Collemos o codigo da letra
        codigo_letra = ord(letra)

        # Comprobamos se e unha letra minuscula
        if codigo_letra >= codigo_a and codigo_letra <= codigo_z :
            # Calculamos o novo codigo
            novo_codigo_letra = codigo_letra + desprazamento

            # Comprobamos se codigo da letra novo e posterior o da z
            if novo_codigo_letra > codigo_z:
                # Calculamos cantas letras se pasa
                diferencia = (novo_codigo_letra - codigo_z)
                # Calculamos a letra a partir da diferencia e a letra a
                # Restamos 1, porque se a diferencia e 1, a letra deberia ser a.
                novo_codigo_letra = codigo_a + diferencia - 1
            
            # Engadimos o novo codigo en texto ao texto cifrado
            texto_cifrado += chr(novo_codigo_letra)
        # Como non e minuscula engadimola o texto sen facer nada
        else:
            texto_cifrado += letra

    return texto_cifrado

## Programa principal
while True:
    try:
        desprazamento = int(input("Indica o desprazamento: "))
        break
    except:
        print("Introduce un número")


texto = input("Indica o texto a cifrar: ")

try:
    print(cifra_cesar(texto, desprazamento))
except:
    print("Datos inválidos")