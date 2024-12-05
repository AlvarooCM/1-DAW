"""Escribe unha función calcular_desconto_irpf(soldo_bruto: float/int, irpf: int) -> float nun script o soldo bruto e o IRPF en tanto por cen. Comproba que estes dous valores son números, que o soldo é maior que 0 e que o IRPF é un valor válido. Se algunha destas condicións non se cumpre, lanza a excepción ValueError. O propio script deberá recibir estes datos por teclado, e utilizar a función creada para calcular o desconto do IRPF. Captura a excepción que lanza a función."""

__author__ = "Alvaro Camino Martinez"

# Creamos la funcion

def calcular_desconto_irpf(soldo_bruto: float, irpf: int) -> float:
    """_summary_

    Args:
        soldo_bruto (float): Pide soldo bruto
        irpf (int): Pide porcentaje irpf

    Raises:
        ValueError: Error, debe ser un numero mayor que 0
        ValueError: Error, debe ser un numero entero mayor que 0

    Returns:
        float: Devuelve el sueldo neto 
    """
# Validar que soldo_bruto é un número maior que 0.

    if type(soldo_bruto) is not (float) or soldo_bruto is not (int):
        raise ValueError("O soldo debe ser float o int.")

# Validar que soldo_bruto sea mayor que 0.

    if soldo_bruto <= 0:
        raise ValueError("O soldo debe ser un numero mayor que 0.")
    
# Validar que irpf é un número enteiro maior que 0 e menor que 100.

    if type(irpf) is not (int) or not (irpf <= 0 and irpf < 100):
        raise ValueError("O IRPF debe ser un número enteiro maior que 0 e menor que 100.")
    
# Calcular o desconto do IRPF.

    desconto = soldo_bruto * (irpf / 100)
    soldo_neto = soldo_bruto - desconto
    return soldo_neto

# Ejecutar try e imprimimos resultados. 

try:
    soldo_bruto = float(input("Introduce o teu soldo bruto: "))
    irpf = int(input("Introduce o teu IRPF en tanto por cento: "))
    
    resultado = calcular_desconto_irpf(soldo_bruto, irpf)
    print(f"O soldo neto e {resultado}")

except ValueError as erro:
    print(f"Erro: {erro}")
