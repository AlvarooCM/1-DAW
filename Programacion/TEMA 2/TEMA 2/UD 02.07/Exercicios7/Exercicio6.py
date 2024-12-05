""" Escribe unha función en Python piramide(lonxitude: int) que imprima unha pirámide de números. Esta recibe un enteiro que indica a lonxitude da pirámide."""

__author__ = "Alvaro Camino Martinez"

def piramide(lonxitude: int):

    for elemento in range(1,lonxitude + 1):
        fila = ""
        for elemento2 in range(1, elemento + 1):
            fila = fila + str(elemento2) + " "
        fila = fila[:-1]
        print (fila)