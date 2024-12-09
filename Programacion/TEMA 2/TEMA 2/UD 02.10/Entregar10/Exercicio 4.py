"""Os números 17, 341 y 62 teñen en común que a suma dos seus díxitos dan o mesmo valor, 8. Hai moitos outros números así; de todos eles, o 17 é o máis pequeno.

Implanta un programa que recibirá por teclado un número entre 1 e 1000 e a continuación se mostre o número decimal máis pequeno que as súas cifras sumen a mesma cantidade que a suma das cifras do número introducido por teclado.

Por exemplo, se o usuario introduce o número 92, deberase imprimir o número 29."""

__author__ = "Alvaro Camino Martinez"

def suma_dixitos(num: int):
    """suma_dixitos

    Args:
        num (int): Numero introducido por el usuario.

    Returns:
        suma: Devuelve el valor de suma una vez acabado el bucle
    """
    suma = 0

    while num > 0:

        suma += num % 10  
        
        num //= 10  

    return suma

def buscar_numero_co_suma_dixitos(dixitos_sum: int):
    """buscar_numero_suma_dixitos

    Args:
        dixitos_sum (int)

    Returns:
       bool: Devuelve el valor None 
    """

    for num in range(1, 1000):  # Desde 1 hasta 999
        if suma_dixitos(num) == dixitos_sum:  # Si la suma de los dígitos es igual
            return num  # Devuelves el número
    return None

# Entrada
numero = int(input("Introduce un número entre 1 e 1000:"))

# Suma de los dígitos del número introducido
suma = suma_dixitos(numero)

# Busca el número más pequeño con esa suma de dígitos
resultado = buscar_numero_co_suma_dixitos(suma)

# Imprime el resultado
print(f"O número máis pequeno cunha suma de díxitos igual a {suma} é: {resultado}")
