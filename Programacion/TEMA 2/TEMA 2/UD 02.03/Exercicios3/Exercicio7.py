"""
Escribe un *script* que pida que se introduzan números por teclado ata que o total da suma de tódolos números introducidos sexa 100 ou máis. 
Ao rematar indica por pantalla a cantidade de números introducidos.

"""

__author__ = "Alvaro Camino Martinez"

suma = 0
cantidade = 0
while True:
    numero = int(input("Introduzca un numero entero:"))
    suma = suma + numero
    cantidade += 1
    if suma >= 100:
        break
print (cantidade)


