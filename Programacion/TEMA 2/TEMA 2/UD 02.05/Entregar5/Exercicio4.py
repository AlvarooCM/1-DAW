"""
Escribe unha función raiz_cadrada(numero: float/int) -> float nun script que calcule a raíz cadrada dun número. Se o parámetro non é un número ou é negativo, lanza unha excepción chamada ValueError. O propio script debe recibir un número por parte do usuario e calcula a raíz cadrada dese número utilizando a función creada anteriormente. Captura a excepción que lanza a función.
"""
__author__ = "Alvaro Camino Martinez"

# Creamos la funcion

def raiz_cadrada(numero: float) -> float:
    """_summary_

    Args:
        numero (float): Pide un numero

    Raises:
        ValueError: Error de entrada

    Returns:
        float: Calcula la raiz del numero introducido
    """
# Comprobamos que el numero sea mayor que 0 y que es un float

    if type(numero) is not (float) or (numero) is not (int):
        raise ValueError("El valor debe ser un numero.")
    
    if numero <= 0:
        raise ValueError("El valor debe ser mayor que 0.")

    return numero ** 0.5

# Ejecutamos el try e imprimos los resultados

try:
    numero = float(input("Introduce un numero:"))
    resultado = raiz_cadrada(numero)
    print(f"La raiz cuadrada de {numero} es {resultado}.")

except ValueError:
    print("Erro: Entrada non válida, por favor introduce numero y numeros enteros.")







