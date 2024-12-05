"""
Escribe un script que reciba un enteiro (n) maior ou igual a 1 e ofreza o resultado da seguinte suma: 1 + 1/2 + 1/3 + … 1/n

"""

__author__ = "Alvaro Camino Martinez"

# Pedimos un numero al usuario

n = float(input("Introduzca un numero entero:"))

# Introducion de las variables.

suma = 0

i = 1

if n >= 1:

# Ejecutamos el bucle e imprimimos soluciones.

    while i <= n:
        suma = suma + 1/i
        i = i + 1
    print (f"A suma total e {suma}")    
     
else:
    print ("error")
        

    
        
    


   


    
    


