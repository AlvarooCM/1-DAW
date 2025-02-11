"""Exercicio 4. Os números de teléfono completos teñen o seguinte formato: +prefixo-número-extensión. Por exemplo: +34-913724710-56. Tanto o prefixo, número e extensión poden ter un número variable de cifras que só poden ser numéricas.

Escribe unha función que reciba como parámetro un número de telefono, e devolva verdadeiro se o parámetro ten formato válido de teléfono ou falso en caso contrario.

Comproba que o tipo de datos do parámetro sexa unha cadea. En caso contrario lanza unha excepción ValueError."""

__author__ = "Alvaro Camino Martinez"

def telefono (num_telefono: int):
    """telefono

    Args:
        num_telefono (int): Numero de telefono

    Raises:
        ValueError: Error tipo de datos

    Returns:
        _type_: False
    """

    cadena_telefono= "0123456789"

    if type(num_telefono) is not int:
        raise ValueError("El numero de telefono debe ser int.")
    
    if len(num_telefono) != 9:
        return False
    
    numeros_telefono = int(num_telefono[:8])

    return num_telefono[9]

telefono_usuario = input("Introduce tu numero de telfono:")


    


    


    
