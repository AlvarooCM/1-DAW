#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pasa a calculadora! é un xogo para dúas persoas no que se comeza cunha calculadora e cada xogador, de xeito alterno, 
suma un número novo, dun só díxito, ao valor acumulado ata o momento, comezando en 0. O xogador que, tras sumar o seu número, 
chegue a un resultado maior ou igual a 31 perde.

Ademais, en cada turno un xogador só pode utilizar os números situados na mesma fila ou columna que o díxito marcado polo seu opoñente no turno anterior, 
pero non pode repetir o número. Evidentemente, o número 0 non se pode utilizar nunca.

Por exemplo, imaxina que, durante unha partida, un xogador recibe aa calculadora mostrándolle o número 28, 
e o opoñente acaba de introducir o número 9. A partir da disposición dos números da calculadora, 
sabemos que nesta quenda unicamente poderá xogar os números 3, 6, 7 y 8:
""" 

__author__ = "Manuel Ramón Varela López"


def calcular_numeros_validos(numero_anterior):
    """
    Funcion que calcula os numeros validos que pode introducir o usuario

    Args:
        numero_anterior (int): É o número que se xogou no anterior paso

    Raises:
        ValueError: se numero_anterior non é un enteiro comprendido entre 1 e 9

    Returns:
        list: Lista de enteiros cos números que se poden xogar
    """
    if type(numero_anterior) is not int:
        raise ValueError
    if numero_anterior > 9 or numero_anterior < 0:
        raise ValueError

    # A fila conseguimola restando 1 ao numero e collendo a division enteira entre 3
    fila = (numero_anterior - 1) // 3
    # A columna consesguimola restando 1 ao numero e collendo o resto de dividir entre 3
    columna = (numero_anterior - 1) % 3

    # Collemos os numeros da da fila
    numeros_fila = [(fila * 3 ) + i for i in range(1, 4)]
    # Numeros da columna
    numeros_columna = [(columna + 1) + 3 * i for i in range(0,3)]

    # Collemos os validos tan so, mirando que non se repitan e que non sexa o numero anterior
    numeros_validos = []
    for n in numeros_fila + numeros_columna:
        if n not in numeros_validos and n != numero_anterior:
            numeros_validos.append(n)

    # Ordenamos a lista antes de enviala
    numeros_validos.sort()
    return numeros_validos

##########3 Programa principal
suma_total = 0
ultimo_numero = None
numeros_posibles = [i for i in range(1, 10)]
turno_a = True
partida_en_curso = True

while partida_en_curso:
    # Indicamos que xogador está xogando
    if turno_a:
        print("Turno do Xogador A.")
    else:
        print("Turno do Xogador B")
    
    # Pedimos un número válido
    while True:
        try:
            print("\tA suma actual é de", suma_total)
            print("\tSelecciona un número dos seguintes: ", numeros_posibles)
            numero_xogado = int(input("\t> "))
            if numero_xogado not in numeros_posibles:
                print("\tEse número non se pode xogar.")
            else:
                break
        except:
            print("\tIntroduce un numero.")

    # Sumamos ao total o número
    suma_total += numero_xogado

    # Se a suma total e igual ou maior a 31 perde o usuario que esta xogado
    if suma_total >= 31:
        # Finalizamos a partida
        partida_en_curso = False
    else:
        # Calculamos os novos números válidos
        numeros_posibles = calcular_numeros_validos(numero_xogado)
        # Cambiamolo turno
        turno_a = not turno_a

# Imprimimoso perdedor
if turno_a:
    print("O xogador A perdeu")
else:
    print("O xogador B perdeu")




    
