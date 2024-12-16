#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crea nun script unha función recursiva: anagrama(palabra1: str, palabra2: str) -> boolean que 
indique se unha das palabras é ou non un anagrama da outra, é dicir, que se pode obter a partir das letras da outra sen máis que reordenalas.

Considerarase que as palabras están escritas en minúsculas, 
sen til nin outros signos diacríticos e sen espazos en branco ou outros caracteres distintos dos alfabéticos da “A” á “Z”.

Se as dúas palabras son iguais tamén se considera que son anagrama.

Nese mesmo script proba a función obtendo dúas palabras por teclado e mostra por pantalla Anagrama se é un anagrama e Non anagrama en caso contrario.
"""

__author__ = "Manuel Ramón Varela López"


def is_anagrama(palabra1, palabra2):
    """
    Indica se as dúas palabras son anagramas entre si

    Args:
        palabra1 (str): palabra a comprobar
        palabra2 (str): palabra a comprobar

    Raises:
        ValueError: Se algún dos parámetros non é unha palabra

    Returns:
        boolean: True en caso de que as palabras sexan anagramas, FAlse en caso contrario
    """

    if type(palabra1) is not str:
        raise ValueError
    
    if type(palabra2) is not str:
        raise ValueError

    # Caso base 1: se non teñen a mesma lonxitude non e un anagrama
    if len(palabra1) != len(palabra2):
        return False
    
    # Collemos a primeira letra, por coller unha
    letra = palabra1[0]
    
    # Caso base 2: a letra collida ten que estar na segunda palabra
    if letra not in palabra2:
        return False
    
    ### Collemos unha subcadea de cada unha das palabras quitando a letra anterior

    # Neste caso quitamos a primeira letra
    nova_palabra1 = palabra1[1:]

    # Caso base 3: se a cadea queda baleira e que xa e un anagrama (a segunda subcadea é totalmente igual)
    if len(nova_palabra1) == 0:
        return True

    # Temos que quitar a letra anterior. Non usamos un replace, porque poderiamos borrar todas as letras iguais
    quitada = False
    # Cadea baleira na que imos engadindo todas as letras
    nova_palabra2 = ""

    # Recorremos todas as letras da segunda palabra
    for l in palabra2:
        # Se xa quitamos a letra, metemos todas as letras
        if quitada:
            nova_palabra2 += l
        else:
            # Non quitamos a letra, e a letra e a que se debe quitar
            if l == letra:
                # Indicamos que a letra esta quitada e non a engadimos a cadea nova
                quitada = True
            else:
                # A letra non e a que se debe quitar, polo que a metemos na cadea
                nova_palabra2 += l

    # Chamada recursiva: chamamos a función con duas novas subcadeas
    return is_anagrama(nova_palabra1, nova_palabra2)


# Test
try:
    print(is_anagrama("nacionalista","altisonancia")) # Verdadeira
    print(is_anagrama("cara","arca")) # Verdadeira
    print(is_anagrama("lacteo","coleta")) # Verdadeira
    print(is_anagrama("retener","enterre")) # Verdadeira
    print(is_anagrama("seto","esto")) # Verdadeira
    print(is_anagrama("lobo","bolo")) # Verdadeira
    print("---------------------------------------------------")
    print(is_anagrama("nacionaliute","altisonancia")) # Falso
    print(is_anagrama("cara","aca")) # Falso
    print(is_anagrama("lactuu","coleta")) # Falso
    print(is_anagrama("reener","entere")) # Falso
    print(is_anagrama("eito","este")) # Falso
    print(is_anagrama("obo","olo")) # Falso
except:
    print("Aconteceu un erro")
