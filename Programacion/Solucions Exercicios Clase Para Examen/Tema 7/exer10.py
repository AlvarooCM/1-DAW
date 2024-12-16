#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A **ordenación por burbulla** é un algoritmo de ordenación simple pero ineficiente para listas pequenas. 
Funciona comparando elementos adxacentes na lista e intercambiándoos se están na orde incorrecta (é dicir, se o primeiro elemento é maior que o segundo). 
Este proceso repítese varias veces ata que toda a lista está ordenada.

Cada "burbulla" (elemento grande) "sube" ata a súa posición correcta, movéndose cara ao final da lista en cada pasada. 

Escribe unha función en Python `burbulla(lista: List) -> List` que implante o algoritmo de ordenación por burbulla para ordenar unha lista de 
números de menor a maior.

"""


__author__ = "Manuel Ramón Varela López"

def burbulla(lista):
    """
    Función que ordena unha lista

    Args:
        lista (int): Lista a ordenar
    """

    # Iniciamos a variable que indica que existeu cambio de posicions a verdadeiro
    movido_elemento = True

    # Mestres que se movera algun elemento seguimos comprobando se esta ordenada a lista
    while movido_elemento:

        # Antes de comezar a mover, indicamos que inda non ficemos ningun movemento
        movido_elemento = False

        # Recorremos tódolos índices menos o último
        for indice in range(len(lista) - 1):

            # Collemos o valor dun indice e o do seu seguinte
            elemento_esquerda = lista[indice]
            elemento_dereita = lista[indice + 1]

            # Comprobamos se os elementos estan en orde
            if elemento_dereita < elemento_esquerda:
                # Como non o estan, intercambiámolos
                lista[indice] = elemento_dereita
                lista[indice + 1] = elemento_esquerda
                # Indicamos que realizamos un movemento
                movido_elemento = True
    

lista = [64, 34, 25, 12, 22, 11, 90]
burbulla(lista)
print(lista)