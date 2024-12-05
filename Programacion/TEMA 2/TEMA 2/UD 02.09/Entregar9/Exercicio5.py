"""Crea nun script unha función recursiva: anagrama(palabra1: str, palabra2: str) -> boolean que indique se unha das palabras é ou non un anagrama da outra, é dicir, que se pode obter a partir das letras da outra sen máis que reordenalas.

Considerarase que as palabras están escritas en minúsculas, sen til nin outros signos diacríticos e sen espazos en branco ou outros caracteres distintos dos alfabéticos da “A” á “Z”.

Se as dúas palabras son iguais tamén se considera que son anagrama.

Nese mesmo script proba a función obtendo unha palabra por teclado e mostra por pantalla Anagrama se é un anagrama e Non anagrama en caso contrario."""

__author__ = "Alvaro Camino Martinez"

def anagrama(palabra1: str, palabra2: str) -> bool:

    palabra1 = palabra1.lower()
    palabra1 = palabra1.replace(" ", "")

    palabra2 = palabra2.lower()
    palabra2 = palabra2.replace(" ", "")

    if len(palabra1) != len (palabra2):
        return False
    
    if not palabra1:
        return True
    
    letra = palabra1[0]
    
    if letra in palabra2:
        palabra2 = palabra2.replace(letra, "", 1)
        return anagrama(palabra1[1:], palabra2)
    else:
        return False
    
palabra1 = input("Introduce la primera palabra:")

palabra2 = input("Introduce la segunda palabra:")

if anagrama(palabra1, palabra2):
    print("Anagrama")
else:
    print("Non Anagrama")

        

    
