"""Escribe unha función en Python eliminar_duplicados(lista: List) -> List que reciba unha lista con elementos duplicados e devolva unha nova lista sen duplicados, mantendo a orde orixinal."""

__author__ = "Alvaro Camino Martinez"

def eliminar_duplicados(lista: List) -> List:

    nova_lista = []
    
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)

    return nova_lista