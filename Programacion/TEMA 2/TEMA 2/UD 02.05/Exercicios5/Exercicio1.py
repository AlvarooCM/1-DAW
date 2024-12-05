"""  Escribe un script que solicite ao usuario dous números e a continuación mostre o resultado de dividir o primeiro número polo segundo. Asegúrate de manexar as excepcións no caso de que o usuario intente dividir entre cero ou introduza por teclado un valor que non sexa un número. Para realizar isto deberás capturar as excepcións ZeroDivisionError e ValueError. Para cada unha das mensaxes mostra unha mensaxe de erro diferente:
"""

__author__ = "Alvaro Camino Martinez"


try:
    numero1 = float(input("Introduzca un numero:"))
    numero2 = float(input("Introduzca otro numero:"))
    resultado = numero1/numero2
    print (resultado)

except ZeroDivisionError:
    print("Erro: Non se pode dividir entre cero")
except ValueError:
    print("Erro: Entrada non válida, por favor introduce números...")

