#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que calcule o salario dun traballador. O programa recibirá por parte do usuario as horas traballadas ao día e os € por cada hora de traballo. 
A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. A partir da súa resposta calcula o salario mensual neto.

Os días laborables ao mes son 22.
Se o usuario indica que o custe da hora é en bruto, indícalle ao usuario que introduza o IRPF en tanto por cen para poder calcularlle o salario neto.
Deduce o número necesario de funcións e defíneas.
"""


__author__ = "Manuel Ramón Varela López"

dias_laborables = 22

def culcular_salario_neto(horas_diarias, soldo_hora):
    """
    Función que calcula o salario neto mensual

    Args:
        horas_diarias (int): As horas que un traballador traballa ao día
        soldo_hora (float): O que cobra o traballador neto a hora

    Returns:
        (float): O soldo neto que cobra un traballador
    """
    soldo_diario = horas_diarias * soldo_hora
    return soldo_diario * dias_laborables


def calcular_salario_neto_con_irpf(horas_diarias, soldo_hora, irpf):
    """
    Función que calcula o salario neto mensual

    Args:
        horas_diarias (int): As horas que un traballador traballa ao día
        soldo_hora (float): O que cobra o traballador bruto a hora
        irpf (float): O IRPF en porcentaxe

    Returns:
        (float): O soldo neto que cobra un traballador
    """
    soldo_bruto = culcular_salario_neto(horas_diarias, soldo_hora)
    return soldo_bruto * (1 - irpf/100)

# Menú
print("Indica se o soldo introducido é bruto ou neto")
print("\ta) Neto")
print("t\b Bruto")
opcion = input(">")

# Calculo sen IRPF
if opcion == "a":
    horas = int(input("Cantas horas traballas ao día: "))
    soldo_hora = float(input("Canto cobras a hora en neto: "))

    salario_neto = culcular_salario_neto(horas, soldo_hora)

    print("O teu salario mé de ", salario_neto, "€")

# Calculo con IRPF
elif opcion == "b":
    horas = int(input("Cantas horas traballas ao día: "))
    soldo_hora = float(input("Canto cobras a hora en bruto: "))
    irpf = float(input("Que IRFP se che aplica en %: "))

    salario_neto = calcular_salario_neto_con_irpf(horas, soldo_hora, irpf)

    print("O teu salario mé de ", salario_neto, "€")

else:
    print("Opción incorrecta")