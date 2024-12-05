"""Crea un script no que se ingresen as notas de alumnos. Vai gardando todas as notas que están entre 0 e 10 nunha lista. Cando o usuario introduza a palabra “fin”, non se pediran máis notas. Ao finalizar o ingreso de notas mostra por pantalla a media de todas as notas.
"""

__author__ = "Alvaro Camino Martinez"

notas_almacenadas = []

while True:

    nota_usuario = input("Introduzca su nota: ")

    if nota_usuario == "fin":
        break

    try:
        nota_total = int(nota_usuario)
    except:
        continue

    if 0 <= nota_total and nota_total <= 10:
        notas_almacenadas.append(nota_total)
    

suma = 0
for nota_total in notas_almacenadas:
    suma = suma + nota_total

media = suma / len(notas_almacenadas)

print (media)








