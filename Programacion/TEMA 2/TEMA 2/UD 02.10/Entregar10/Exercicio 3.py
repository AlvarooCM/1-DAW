"""Pasa a calculadora! é un xogo para dúas persoas no que se comeza cunha calculadora e cada xogador, de xeito alterno, suma un número novo, dun só díxito, ao valor acumulado ata o momento, comezando en 0. O xogador que, tras sumar o seu número, chegue a un resultado maior ou igual a 31 perde.

Ademais, en cada turno un xogador só pode utilizar os números situados na mesma fila ou columna que o díxito marcado polo seu opoñente no turno anterior, pero non pode repetir o número. Evidentemente, o número 0 non se pode utilizar nunca.

Por exemplo, imaxina que, durante unha partida, un xogador recibe aa calculadora mostrándolle o número 28, e o opoñente acaba de introducir o número 9. A partir da disposición dos números da calculadora, sabemos que nesta quenda unicamente poderá xogar os números 3, 6, 7 y 8:"""

__author__ = "Alvaro Camino Martinez"

# Diccionario de relaciones numéricas
numeros_relacionados = {
    1: [2, 3, 4, 7],
    2: [1, 3, 5, 8],
    3: [1, 2, 6, 8],
    4: [1, 5, 6, 7],
    5: [2, 4, 6, 8],
    6: [3, 4, 5, 9],
    7: [1, 4, 8, 9],
    8: [2, 5, 7, 9],
    9: [3, 6, 7, 8],
}

jugadores = [1, 2]  # Lista de jugadores

def calcular_opciones(numero_anterior: int, relacion: dict, numeros_usados: list) -> list:
    """
    Calcula los números disponibles para elegir en función del último número seleccionado.

    Args:
        numero_anterior (int): El último número jugado o `None` si es el primer turno.
        relacion (dict): Diccionario que define las relaciones entre los números.
        numeros_usados (list): Lista de números que ya han sido jugados.

    Returns:
        list: Lista de números disponibles para elegir.
    
    Raises:
        ValueError: Si el último número no es válido dentro de las relaciones definidas.
    """
    if numero_anterior is not None and numero_anterior not in relacion:
        raise ValueError(f"Número inválido ({numero_anterior}). No se encuentra en las relaciones.")
    
    if numero_anterior:
        return [num for num in relacion[numero_anterior] if num not in numeros_usados]
    else:
        return [num for num in range(1, 10) if num not in numeros_usados]

def seleccionar_numero(opciones: list) -> int:
    """
    Permite al jugador seleccionar un número de una lista de opciones disponibles.

    Args:
        opciones (list): Lista de números disponibles para elegir.

    Returns:
        int: Número seleccionado por el jugador.
    
    Raises:
        ValueError: Si el jugador introduce un número inválido.
    """
    while True:
        try:
            seleccion = int(input(f"Selecciona un número entre las opciones {opciones}: "))
            if seleccion in opciones:
                return seleccion
            else:
                print(f"El número {seleccion} no está entre las opciones disponibles.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def turno_jugador(jugador: int, total: int, relacion: dict, usados: list, ultimo: int) -> tuple:
    """
    Ejecuta el turno de un jugador, actualizando el total acumulado y los números usados.

    Args:
        jugador (int): Identificador del jugador que está jugando.
        total (int): Total acumulado de los números jugados.
        relacion (dict): Diccionario que define las relaciones entre los números.
        usados (list): Lista de números que ya han sido seleccionados.
        ultimo (int): Último número jugado o `None` si es el primer turno.

    Returns:
        tuple: El nuevo total acumulado y el número elegido por el jugador.
    
    Raises:
        ValueError: Si no hay opciones disponibles o si el total alcanza el límite del juego.
    """
    print(f"\nTurno del jugador {jugador}. Total acumulado: {total}")
    
    opciones = calcular_opciones(ultimo, relacion, usados)
    
    if not opciones:
        raise ValueError(f"El jugador {jugador} ha perdido. No tiene opciones disponibles.")
    
    eleccion = seleccionar_numero(opciones)
    total += eleccion
    usados.append(eleccion)
    
    if total >= 31:
        raise ValueError(f"El jugador {jugador} ha perdido. El total alcanzó {total}.")
    
    return total, eleccion

# Inicialización del juego
total_acumulado = 0
numeros_usados = []
numero_previo = None

try:
    while total_acumulado < 31:
        for jugador in jugadores:
            total_acumulado, numero_previo = turno_jugador(jugador, total_acumulado, numeros_relacionados, numeros_usados, numero_previo)
        # Reseteamos los números usados para la siguiente ronda
        numeros_usados = []
except ValueError as error:
    print(f"Fin del juego: {error}")

