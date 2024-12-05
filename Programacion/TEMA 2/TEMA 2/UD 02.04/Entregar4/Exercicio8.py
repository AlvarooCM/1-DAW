""" 
A avaliación deste módulo é a seguinte: 15% de tarefas, 20% exame teórico e 65% exame práctico. Escribe un script que lle pedirá ao usuario as súas tres notas sobre 10. Indicaralle por pantalla se obtivo Sobresaliente, Notable, Ben, Suficiente ou Insuficiente.
"""

__author__ = "Alvaro Camino Martinez"

# Creacion de las funciones

def tarefas(nota_tarefas: float) -> float:
    """ Nota Tarefas

    Args:
        nota_tarefas (float): Nota tarefas

    Returns:
        float: Calcula el valor return de la nota de las tarefas
    """
    return nota_tarefas * 0.15

def teorico(nota_teorico: float) -> float:
    """Nota Teorico

    Args:
        nota_teorico (float): Nota examen teorico

    Returns:
        float: Calcula el valor return de la nota del examen teorico
    """
    return nota_teorico * 0.20

def practico(nota_practico: float) -> float:
    """Nota Practico

    Args:
        nota_practico (float): Nota Practico

    Returns:
        float: Calcula el valor return de la nota del examen teorico
    """
    return nota_practico * 0.65

def nota_total(nota_practico: float, nota_teorico: float, nota_tarefas: float) -> float:
    """Nota total

    Args:
        nota_practico (float): Nota practico
        nota_teorico (float): Nota teorico
        nota_tarefas (float): Nota tarefas

    Returns:
        float: Suma las 3 notas en el return  
    """
    nota_final = (nota_practico + nota_teorico + nota_tarefas)/3

    return nota_final


def tipo_notas (nota_final: float) -> float:
    """Devuelve el tipo de nota del alumno

    Args:
        nota_final (float): Nota final del alumno

    Returns:
        float: Valor que devuelve el return
    """
    if nota_final >= 9:
        return "Sobresaliente"
    
    elif nota_final > 7 and nota_final < 9:
        return "Notable"
    
    elif nota_final > 5 and nota_final < 7:
        return "Ben"
    
    elif nota_final == 5:
        return "Suficiente"
    
    else:
        return "Insuficiente"

# Pedimos valores al usuario
nota_tarefas = float(input("Introduzca la nota de sus tareas:"))
nota_teorico = float(input("Introduzca la nota de sus teorico:"))
nota_practico = float(input("Introduzca la nota de sus practico:"))


nota_final = nota_total(nota_tarefas, nota_teorico, nota_practico)

# Inicializamos la condicional mas imprimimos los resultados
print(f"{nota_total(nota_tarefas, nota_teorico, nota_practico)} = {tipo_notas(nota_final)}")
    
