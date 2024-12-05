"""
A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. Escribe un script que lle pida ao usuario as súas tres notas sobre 10 e indicaralle por pantalla a súa nota final sobre 10.
"""

__author__ = "Alvaro Camino Martinez"

#Pedimos los datos

tarefas = float(input ("Introduzca la nota de las tareas:"))

teorico = float(input ("Introduzca la nota del examen teorico:"))

practico = float(input ("Introduzca la nota del examen practico:"))

notatotal = tarefas * 0.15 + teorico * 0.20 + practico * 0.65

#Imprimimos la solucion

print (f"A sua nota final e {notatotal}")

