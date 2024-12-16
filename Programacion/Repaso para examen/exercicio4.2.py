"""Escribe un script que pida as notas dun exame dos alumnos de unha clase e conte o numero de aprobados e suspensos. Pediráselle ao usuario que introduza notas por teclado ata que introduza un número inferior a 0 ou superior a 10. Mostrará primeiro o número de aprobados e despois o de suspensos."""

aprobados = 0

suspensos = 0

contador = 0

while True:
    nota = float(input("Introduzca su nota:"))
    
    if nota < 0 or nota > 10:
        print ("Fin de la introduccion de notas.")
        break

    if nota < 5:
        suspensos = suspensos + 1
    else:
        aprobados = aprobados + 1

print (aprobados)
print (suspensos)
    

    





