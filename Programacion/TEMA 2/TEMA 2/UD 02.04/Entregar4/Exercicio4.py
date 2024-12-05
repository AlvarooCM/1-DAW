""" 
Escribe un script que pide ao usuario os coeficientes dunha ecuación de segundo grao e calcula a solución. Comproba se hai unha solución, dúas ou ningunha. Dependendo do caso, mostra as solucións que corresponda. Crea as seguintes funcións:

"""
__author__ = "Alvaro Camino Martinez"

# Ponemos las funciones

def descriminante(a: float, b: float, c: float) -> float:
    """
    Recoge los valores de a,b y c

    Args:
        a (float): Coeficiente 1
        b (float): Coeficiente 2
        c (float): Coeficiente 3

    Returns:
        float: Valor del return
    """

    return b**2 -4 * a * c

def numero_solucions(a: float, b: float, c: float) -> int:
    """Calcula el numero de soluciones

    Args:
        a (float): Coeficiente 1
        b (float): Coeficiente 2
        c (float): Coeficiente 3

    Returns:
        int: Valor del return
    """

    nsolucion = descriminante(a,b,c)
    if nsolucion > 0:
        return 2
    elif nsolucion == 0:
        return 1
    else:
        return 0

def solucion_unica(a: float, b: float) -> float:
    """ Solucion unica

    Args:
        a (float): Coeficiente 1
        b (float): Coeficiente 2

    Returns:
        float: Valor del return
    """
    return -b - (2 * a)

def calcula_duas_solucions (a: float, b: float, c: float) -> (float, float):
    """Calcular 2 soluciones

    Args:
        a (float): Coeficiente 1
        b (float): Coeficiente 2
        c (float): Coeficiente 3
    Returns:
        float: Valor del return
    """

    solucion1 = -b + descriminante (a,b,c) **0.5 / 2*a
    solucion2 = -b - descriminante (a,b,c) **0.5 / 2*a

    return solucion1, solucion2

# Pedimos valores a los usuarios

a = int(input("Introduzca valor de a:"))
b = int(input("Introduzca valor de b:"))
c = int(input("Introduzca valor de c:"))

num_sol = numero_solucions(a,b,c)

# Ejecucion de programa e impresion final

if num_sol == 2:
    print(f"As solucións son: {calcula_duas_solucions(a,b,c)}")

elif num_sol == 1:
    print(f"As solucións son: {solucion_unica(a,b)}")

else:
    print("Non ten solucions reais")