"""Escribe unha función en Python so_pares(lista: List) -> List que reciba unha lista de números e devolva unha nova lista que conteña só os números pares da lista orixinal."""

__author__ = "Alvaro Camino Martinez"

def so_pares(lista: List) -> List:

    nova_lista = []

    for elemento in lista:
        if elemento % 2 == 0:
            nova_lista.append(elemento)

    return nova_lista