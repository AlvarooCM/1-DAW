"""Desenvolva un script para determinar se unha cadea de caracteres (palabra/frase) é palíndromo, é dicir, se se pode ler igual de esquerda a dereita que de dereita a esquerda. Un exemplo de palíndromo é a palabra “radar”.

Desenvolva a seguinte función recursiva:

Función palindromo: cos parámetros de entrada que considere preciso para resolver de forma recursiva se unha palabra/frase é palíndromo. O valor de retorno será True ou False en función do caso. (Exemplo:“radar” é palíndromo, polo tanto, a función devolverá True).
Nese mesmo script proba a función obtendo unha palabra ou frase por teclado e mostra por pantalla Palídromo se é un palñindromo e Non palíndromo en caso contrario."""

__author__ = "Alvaro Camino Martinez"

def palindromo (palabra: str) -> bool:
    """Palindromo

    Args:
        palabra (str): Palabra introducida por el usuario

    Returns:
        bool: Devuelve TRUE or FALSE
    """

    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")


    if len(palabra) == 0:
        return True

    elif len(palabra) == 1:
        return True

    elif palabra[0] != palabra[-1]:
        return False
    
    return palindromo(palabra[1:-1])


palabra = input("Ingrese unha palabra: ")

palabra_output = palindromo(palabra)
try:
    if palabra_output:
        print("Palíndromo")
    else:
        print("Non palíndromo")
except ValueError as erro:
    print(f"Erro: {erro}")