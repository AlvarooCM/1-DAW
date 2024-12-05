"""Escribe unha función celsius_to_farenheit(celsius: float) -> float nun script que converta unha temperatura de graos Celsius a Farenheit. Se o parámetro que se lle pasa a función non é un número ou non é un número positivo, debe lanzar unha excepción ValueError.
"""

def celsius_to_farenheit(celsius: float) -> float:
    
    if not(type(celsius) is int or type(celsius) is float):
        raise ValueError()

    if celsius < 0:
        raise ValueError()

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
        raise ValueError()

    if celsius < 0:
        raise ValueError()

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit