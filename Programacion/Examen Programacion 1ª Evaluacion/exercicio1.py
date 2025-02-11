"""Exercicio 1. Un radar de tramo consta de dous radares fixos separados por unha certa distancia. Se un vehículo percorre dita distancia nunha velocidade media permitida a maior, este vehículo recibirá unha multa.

Escribe unha función que reciba 3 parámetros:

Distancia en metros entre dous radares fixos.
Velocidade máxima permitida en quilómetros/hora.
Número de segundos que tardou o vehículo en recorrer o tramo entre os dous radares.
A función debe devolver verdadeiro se o vehículo debe recibir unha multa, e falso se non é así.

Comproba o tipo de datos dos parámetros, así como que se os seus valores son válidos. En caso contrario lanza unha excepción ValueError."""

__author__ = "Alvaro Camino Martinez"

def radar (distancia: float, velocidade_maxima_tramo: float, segundos: float) -> bool:
    """radar

    Args:
        distancia (float): Distancia entre radares
        velocidade_maxima (float): Velocidade maxima permitida en km/h
        segundos (float): Segundos que tard el vehiculo en recorrer el tramo entre radares

    Raises:
        ValueError: Error de tipo de datos
        ValueError: Error de tipo de datos
        ValueError: Error de tipo de datos

    Returns:
        bool: Verdadeiro ou Falso
    """
    
    if type(distancia) is not float:
        raise ValueError("El valor debe ser float")
    
    if type(velocidade_maxima_tramo) is not float:
        raise ValueError("El valor debe ser float")
    
    if type(segundos) is not float:
        raise ValueError("El valor debe ser float")
    
    distancia_kilometros = distancia / 1000

    tiempo_en_horas = segundos / 3600

    velocidade_vehiculo = distancia_kilometros / tiempo_en_horas
    
    if velocidade_vehiculo >= velocidade_maxima_tramo:
        return True
    else:
        return False
    
try:
    distancia = float(input("Introduce la distancia entre radares en metros:"))
    velocidade_maxima_tramo = float(input("Introduce a velocidade maxima permitida en el tramo en km/h:"))
    segundos = float(input("Introduce o numero de segundos que tardou o vehiculo en recorrer o tramo entre os dous radares:"))

    multa = radar (distancia, velocidade_maxima_tramo, segundos)

    print (multa)

except ValueError:
    print("Error de tipo de datos, porfavor vuelva a introducirlos.")

# El programa devuelve True si el vehiculo debe ser multado y False sino debe ser multado.






        


















    


    
    
    

    
    
    
