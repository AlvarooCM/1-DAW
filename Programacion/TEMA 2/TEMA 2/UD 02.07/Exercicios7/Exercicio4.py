"""Escribe unha función en Python contar_lonxitudes(lista: List) -> List que reciba unha lista de palabras e devolva unha lista coa lonxitude de cada palabra."""

__author__ = "Alvaro Camino Martinez"

def contar_lonxitudes(lista: List) -> List:

    nova_lista = []

    for elemento in lista:
        nova_lista.append(len(elemento))

    return nova_lista
        
