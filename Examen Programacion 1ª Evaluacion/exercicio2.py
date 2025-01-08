"""Deséxase saber os días que faltan para que remate o ano. Polo tanto, escribe unha función que que reciba como parámetros:

O mes en número (1, 2, 3,... ata 12)
O día do mes en número (Dependendo do mes poden ser 28, 30 ou 31 días). Consideramos que o ano non é bisesto.
A función debe devolver os días que faltan para rematar o ano.

Comproba o tipo de datos dos parámetros, así como que se os seus valores son válidos. En caso contrario lanza unha excepción ValueError."""

__author__ = "Alvaro Camino Martinez"

def dias_restantes (mes: int, dia_mes: int):
    """dias_restantes

    Args:
        mes (int): Mes del año.
        dia_mes (int): Dia del mes.

    Raises:
        ValueError: Error de tipo de datos.
        ValueError: Error de tipo de datos.
        ValueError: Error introduccion del mes, debe ser entre 1 (Enero) y el 12 (Diciembre).
        ValueError: Error introduccion del dia del mes entre 1 y el 31 como maximo.
    """

    if type(mes) is not int:
        raise ValueError("El mes debe ser int.")
    
    if type(dia_mes) is not int:
        raise ValueError("El dia del mes debe ser int.")
    
    if mes < 1 and mes > 12:
        raise ValueError("El mes debe estar entre el 1 y el 12.")
    
    if dia_mes < 1 and dia_mes > 31:
        raise ValueError("El dia del mes debe estar entre el 1 y el 31.")
    
try:
    mes = int(input("Introduce numero de mes:"))
    dia_mes = int(input("Introduce dia del mes:"))

    enero = 31

    febrero = 28

    marzo = 31

    abril = 30

    mayo = 31

    junio = 30

    julio = 31

    agosto = 31

    septiembre = 30

    octubre = 31

    noviembre = 30

    diciembre = 31

except ValueError:
    print("Error de tipo de datos, profavor vuelva a introducirlos.")
    
