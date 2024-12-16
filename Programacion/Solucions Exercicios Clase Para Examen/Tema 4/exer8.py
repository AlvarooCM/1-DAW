#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. 
Escribe un script que lle pedirá ao usuario as súas tres notas sobre 10. 
Indicaralle por pantalla se obtivo Sobresaliente, Notable, Ben, Suficiente ou Insuficiente.

Deduce o número necesario de funcións e defíneas.
"""


def calificacion_numero_a_texto (nota):
	"""
    Funcion que devolve a nota en texto a partir da nota numerica
    
	Args:
		nota(float): valor numerico da nota
    
	Returns:
		str: cadea de texto ca nota en texto, None se a nota de entrada non e valida
		
    """
	#Segundo a nota devolvemos a calificacion en texto
	if nota > 10 or nota < 0:
		return None
	elif nota >= 9:
		return "Sobresaliente"
	elif nota >= 7:
		return "Notable"
	elif nota >= 6:
		return "Ben"
	elif nota >= 5:
		return "Suficiente"
	else:
		return "Insuficiente"


def calcula_calificacion_final(nota_tarefas, nota_teorico, nota_practico):
    """
    Funcion que devolve a nota final a partir das notas dos seguintes itéms de valoración
    
	Args:
		nota_tarefas(float): Nota das tarefas
        nota_teorico(float): Nota das proba teorica
        nota_practico(float): Nota da proba práctica
    
	Returns:
		float: nota final
		
    """
    return nota_tarefas * 0.15 + nota_teorico * 0.2 + nota_practico * 0.65

# Collemos os datos
n_tarefas = float(input("Introduce a nota das tarefas: "))
n_teorico = float(input("Introduce a nota da proba teórica: "))
n_practico = float(input("Introduce a nota da proba práctica: "))

# Facemos os calculos
nota_final = calcula_calificacion_final(n_tarefas, n_teorico, n_practico)
nota_textual = calificacion_numero_a_texto(nota_final)

# Indicamos os datos
print("Esta é a túa nota: ", nota_textual)