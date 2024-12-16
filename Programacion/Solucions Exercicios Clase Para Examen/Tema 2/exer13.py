#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que calcule o salario dun traballador. 
O programa recibirá as horas traballadas ao día e os € por hora dese traballo por parte do usuario. 
A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. A partir da súa resposta calcula o salario mensual neto.

Os días laborables ao mes son 22.
Se o usuario indica que o custe da hora é en bruto, indícalle ao usuario que introduza o IRPF en tanto por cen para poder calcularlle o salario neto.
"""

__author__ = "Manuel Ramón Varela López"

# Días laborables ao mes
dias_laborales_mes = 22 

# Mostramos o menú
print("Elixe unha das opcions:")
print("\ta) Calculo soldo neto")
print("\tb) Calculo soldo bruto")
print("\tCalquera outro caracter para sair")
eleccion = input("> ")


# Eliximos a opción do menu
# Opcion 1: soldo neto
if eleccion == "a":
    
    # Pedimos os datos
    horas_dia = int(input("Introduce as horas traballadas ao día: "))
    tarifa_hora = float(input("Introduce os euros que se pagan por hora: "))

    # Calculamos o salario neto
    salario = horas_dia * tarifa_hora * dias_laborales_mes
    print("O salario a cobrar é de ", salario, "€")

# Opción 2: soldo bruto
elif eleccion == "b":
    
    # Pedimos os datos
    horas_dia = int(input("Introduce as horas traballadas ao día: "))
    tarifa_hora = float(input("Introduce os euros que se pagan por hora: "))
    irpf = float(input("Introduce o IRPF en %: "))
    
    # Calculamos o salario bruto
    salario_bruto = horas_dia * tarifa_hora * dias_laborales_mes

    # Calculamos o irpf en decimal
    irpf = irpf/100

    # Calculamos o salario neto
    salario = salario_bruto * (1-irpf)
    print("O salario a cobrar é de ", salario, "€")

# Escollese sair
else:
    print("Adios")


