"""
Implantar unha aplicación que calcule o menor de tres números introducidos por teclado polo usuario e o mostre por pantalla. Comproba antes de nada que ningún par de números é igual. Se isto é así, indícallo mostra por pantalla Erro e non calcules cal é o menor dos 3. Define dúas e utiliza estas dúas funcións:
"""

__author__ = "Alvaro Camino Martinez"

def comprobar_valores_iguais(numero1: int, numero2: int, numero3: int) -> bool:

    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return True
    return False

def calcular_menor_numero(numero1: int, numero2: int, numero3: int) -> int:

    if numero1 < numero2 and numero1 < numero3:
        return numero1
    elif numero2 < numero1 and numero2 < numero3:
        return numero2
    else:
        return numero3

# Pedimos o primeiro numero
numero1 = int(input("Ingrese un numero por consola: "))
numero2 = int(input("Ingrese un numero por consola: "))
numero3 = int(input("Ingrese un numero por consola: "))

# Comprobamos se son iguais os numeros
son_iguais = comprobar_valores_iguais(numero1, numero2, numero3)

# Se son iguais non facemos nada
if son_iguais:
    print("Erro")

# Se son distintos, calculamos o menor dos tres numeros
else:
    menor = calcular_menor_numero (numero1, numero2, numero3)
    print(menor)