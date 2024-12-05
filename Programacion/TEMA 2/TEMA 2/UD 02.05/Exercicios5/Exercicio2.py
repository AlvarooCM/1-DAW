""" 
Escribe un script que pida ao usuario un número enteiro positivo. Se o usuario introduce un valor incorrecto (e dicir, un valor que non sexa un número ou non é positivo), o programa debe de volver a pedir o número ata que o usuario introduza un valor válido. Para finalizar o script mostra o número de veces que se intentou introducir un número ata que este fose un enteiro positivo.
"""

__author__ = "Alvaro Camino Martinez"


intentos = 0
while True:
    try:
        intentos = intentos + 1
        numero = int(input("Introduce un numero entero:"))
        if numero < 0:
            continue
        break
    
    except:
        pass
    print (f"Ha realizado {intentos} intentos.")