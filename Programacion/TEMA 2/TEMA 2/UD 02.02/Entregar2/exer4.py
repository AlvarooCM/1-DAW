'''
Escribe un script que calcule o salario dun traballador. O programa recibirá as horas traballadas ao día e os € por hora dese traballo por parte do usuario. A continuación preguntaralle ao usuario se a tarifa é en bruto ou en neto. A partir da súa resposta calcula o salario mensual neto.
'''
__author__ = "Alvaro Camino Martinez"

#Pedimos datos al usuario

horas_trabajadas = int (input("Introduzca el número de horas trabajadas en 1 día:"))
euros_hora = float (input("Introduzca su salario por hora trabajada:"))

print ("Salario mensual:")
print ("\ta) Neto:")
print ("\tb) Bruto:")

option = input (">")

#Creacion de la condicional if para calcular los salarios e imprimir los resultados

if option == 'a':
    sueldo_dia = horas_trabajadas * euros_hora
    sueldo_mes = sueldo_dia * 22
    print (f"Su salario mensual neto es de {sueldo_mes} euros.")

elif option == 'b':
    irpf = float(input("Introduzca su porcentaje de irpf:"))
    porcentaje_irpf = irpf / 100
    sueldo_neto_dia = (euros_hora * horas_trabajadas) - porcentaje_irpf * (euros_hora * horas_trabajadas)
    sueldo_neto_mes = sueldo_neto_dia * 22
    print (f"Su salario mensual neto es de {sueldo_neto_mes} euros.")
else:
    print("Error")





