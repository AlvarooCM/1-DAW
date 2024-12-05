__author__ = "Alvaro Camino Martinez"

aprobados = 0

suspensos = 0

while True: 
    mensaxe = int(input("Introduzca una nota:"))

    nota = float (mensaxe)

    if nota < 0 or nota > 10:
        print ("Fin de introduccion de notas")
        break

    elif nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print (f"El numero de aprobados es de {aprobados}")
print (f"El numero de suspensos es de {suspensos}")






