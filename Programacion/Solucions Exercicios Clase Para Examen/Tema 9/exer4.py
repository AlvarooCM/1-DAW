#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desenvolva un script para determinar se unha cadea de caracteres (palabra/frase) é palíndromo, é dicir, se se pode ler igual 
de esquerda a dereita que de dereita a esquerda. Un exemplo de palíndromo é a palabra “radar”.

Desenvolva a seguinte función recursiva:

Función palindromo: cos parámetros de entrada que considere preciso para resolver de forma recursiva se unha palabra/frase é palíndromo. 
O valor de retorno será True ou False en función do caso. (Exemplo:“radar” é palíndromo, polo tanto, a función devolverá True).
Nese mesmo script proba a función obtendo unha palabra ou frase por teclado e mostra por pantalla Palídromo se é un palíndromo e Non palíndromo en caso contrario.
"""

__author__ = "Manuel Ramón Varela López"

def is_palindromo(palabra):
    """
    Indica se unha palabra ou frase é palíndromo

    Args:
        palabra (str): A palabra ou frase a testear

    Raises:
        ValueError: Se palabra non é unha cadea

    Returns:
        boolean: True se a palabra ou frase é palíndromo, FAlse en caso contrario
    """

    if type(palabra) is not str:
        raise ValueError

    # Poñemos todo en minúscula e quitamos os espazos para poder utilizar frases
    palabra = palabra.lower()
    palabra = palabra.replace(" ","")
    
    # Caso base 1: se a lonxitude é 1, é palíndroma
    if len(palabra) <= 1:
        return True
    
    # Comparamos a primeira e última letra
    if palabra[0] == palabra[-1]:
        # Chamada recursiva: Se a subcadea de dentro é palíndroma, esta palabra tamén o é porque a primeira e ultima letra son iguais
        return is_palindromo(palabra[1:-1])
    else:
        # Caso base 2: coma a primeira e ultima letra son diferentes xa non é un palindromo
        return False


# Test: isto so o poño para probar
try:
    print(is_palindromo("radar")) # Verdadeiro
    print(is_palindromo("Se es o no se es")) # Verdadeiro
    print(is_palindromo("Anita lava la tina")) # Verdadeiro
    print(is_palindromo("Eva usaba rimel y le miraba suave")) # Verdadeiro

    print("-----------------------------")

    print(is_palindromo("rader")) # Falso
    print(is_palindromo("Se es o ne se es")) # Falso
    print(is_palindromo("Anita leva la tina")) # Falso
    print(is_palindromo("Eva usaba rimeo y le miraba suave")) # Falso
except:
    print("Aconteceu un erro")
