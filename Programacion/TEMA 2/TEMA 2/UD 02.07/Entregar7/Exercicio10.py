""" O algoritmo de ordenación que se describe a continuación permite ordenar unha lista de xeito simple pero ineficiente para listas pequenas. Funciona comparando elementos adxacentes na lista e intercambiándoos se están na orde incorrecta (é dicir, se o primeiro elemento é maior que o segundo). Este proceso repítese varias veces ata que toda a lista estea ordenada. É dicir, realízanse varias pasadas sobre a lista para ordenala ata que non se produza ningún intercambio de posicións.

Escribe unha función en Python ordenar(lista: List) -> List que implante o algoritmo de ordenación descrito anteriormente para unha lista de números de menor a maior.

Aquí temos un exemplo:

# Proba con estes datos:
lista = [64, 34, 25, 12, 22, 11, 90]
# saída esperada: [11, 12, 22, 25, 34, 64, 90] """

__author__ = "Alvaro Camino Martinez"

from typing import List

def ordenar(lista: List[int]) -> List[int]:
    
    n = len(lista)
    
    # Realizamos múltiples pasadas sobre a lista
    for i in range(n):
        # Na cada pasada, facemos comparaciones entre elementos adxacentes
        for j in range(n - 1):
            # Se o elemento actual é maior que o seguinte, intercambiamos
            if lista[j] > lista[j + 1]:
                # Intercambiamos os elementos de lugar
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                
    return lista

# Ejemplo
if __name__ == "__main__":
    lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista orixinal:", lista_exemplo)
    lista_ordenada = ordenar(lista_exemplo)
    print("Lista ordenada:", lista_ordenada)


