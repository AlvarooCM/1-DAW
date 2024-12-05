"""
 Escribe un script que pida ao usuario un ano e indique se é bisesto ou non. Coidado que a condición de ser bisesto non só é ser divisible entre 4. O algoritmo debe estar implantado dentro dunha función denominada:

"""

def comprobar_bisesto(ano: int) -> bool:
    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        return True
    elif ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False
      
ano = int(input("Introduzca un ano:"))

if ano <= 0:
    print("Error")
else:
    bisiesto = comprobar_bisesto(ano)
    if bisiesto:
        print ("Ano bisiesto")
    else:
        print("Ano non bisiesto")




