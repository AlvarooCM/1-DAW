#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Realiza a implantación da función `descifra_cesar(texto: str, desprazamento: int): str` nun *script* que descifre unha cadea 
cifrada con cifrado César. Lanza tamén excepción `ValueError` se os argumentos da función son do tipo de datos inválidos.

O propio *script* debe utilizar dita función para descifrar un texto introducido polo usuario para mostrar o texto descifrado por pantalla. 
O usuario tamén indicará por teclado o desprazamento.
"""

__author__ = "Manuel Ramón Varela López"

def descifra_cesar(texto, desprazamento):
    """
    Args:
        texto (str) : o texto a traducir
        desprazamento (int) : o desprazamento para realizar o descifrado

    Returns:
        str : o texto descifrado

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
            novo_codigo_letra = codigo_letra - desprazamento

            # Comprobamos se codigo da letra novo e anterior o de a
            if novo_codigo_letra < codigo_a:
                # Calculamos cantas letras se pasa
                diferencia = (codigo_a - novo_codigo_letra)
                # Calculamos a letra a partir da diferencia e a letra a
                # Sumamos 1, porque se a diferencia e 1, a letra deberia ser z.
                novo_codigo_letra = codigo_z - diferencia + 1
            
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
    print(descifra_cesar(texto, desprazamento))
except:
    print("Datos inválidos")