""" 
 Escribe un script que calcule o salario dun traballador. O programa recibirá por parte do usuario as horas traballadas ao día e os € por cada hora de traballo. A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. A partir da súa resposta calcula o salario mensual neto.
"""

__author__ = "Alvaro Camino Martinez"

# Creacion de las funciones

def neto(sueldo_dia: float, horas_trabajadas: float,) -> float:
    """Sueldo neto

    Args:
        sueldo_dia (float): Sueldo diario
        horas_trabajadas (float): Horas trabajadas
    Returns:
        float: Calcula el valor del return del sueldo neto
    """

    sueldo_dia = horas_trabajadas * sueldo_dia
    sueldo_mes = sueldo_dia * 22

    return sueldo_mes


def bruto(sueldo_neto_dia: float, horas_trabajadas: float, porcentaje_irpf: float) -> float:
    """Sueldo bruto

    Args:
        sueldo_neto_dia (float): Sueldo neto diario
        horas_trabajadas (float): Horas trabajadas
        porcentaje_irpf (float): Porcentaje % de irpf 0-100

    Returns:
        float: Calcula el valor return del sueldo bruto
    """

    porcentaje_irpf = irpf / 100
    sueldo_neto_dia = (sueldo_neto_dia * horas_trabajadas) - porcentaje_irpf * (sueldo_neto_dia * horas_trabajadas)
    sueldo_neto_mes = sueldo_neto_dia * 22

    return sueldo_neto_mes

# Inicializacion de las variables mas creacion del menu
print ("Salario mensual:")
print ("\ta) Neto:")
print ("\tb) Bruto:")

option = input (">")

# Creacion de la condicional if para calcular los salarios e imprimir los resultados

if option == 'a':
    sueldo_dia = float(input("Ingrese la cantidad de dinero neto a recibir en un dia:"))
    print (f"Su salario mensual neto es de {neto(sueldo_dia)} euros.")
elif option == 'b':
    irpf = float(input("Introduzca su porcentaje de irpf:"))
    sueldo_neto_dia = float(input("Ingrese la cantidad de dinero neto a recibir en un dia:"))
    print (f"Su salario mensual bruto es de {bruto(sueldo_neto_dia) } euros.")
else:
    print("Error")