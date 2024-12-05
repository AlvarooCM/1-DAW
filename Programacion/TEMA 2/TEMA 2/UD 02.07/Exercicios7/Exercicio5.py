"""Escribe unha función en Python coller_comúns(lista1: List, lista2: List) -> List que reciba dúas listas e devolva unha lista cos elementos comúns."""

__author__ = "Alvaro Camino Martinez"

def coller_comúns(lista1: List, lista2: List) -> List:

    comuns = []

    for elemento in lista1:
        
        if elemento in lista2 and elemento not in comuns:
            comuns.append(elemento)

    return comuns