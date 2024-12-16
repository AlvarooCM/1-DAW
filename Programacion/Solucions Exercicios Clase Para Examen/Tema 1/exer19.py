#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. 
Escribe un script que lle pida ao usuario as súas tres notas sobre 10 e indicaralle por pantalla a súa nota final sobre 10.
"""

__author__ = "Manuel Ramón Varela López"

# Solicitamos ao usuario as notas
tarefas = float(input("Introduza a nota das tarefas: "))
teorico = float(input("Introduza nota do exame teórico: "))
practico = float(input("Introduza a nota do exame práctico práctico: "))

# Calculamos a nota final
nota_tarefas = tarefas * 0.15
nota_teorico = teorico * 0.20
nota_practico = practico * 0.65
nota_final = nota_tarefas + nota_teorico + nota_practico

# Mostramos ao usuario os datos
print("A nota final do módulo é ",nota_final)
