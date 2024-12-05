__author__ = "Alvaro Camino Martinez"

# Pedimos el valor de n al usuario.

n = int(input("Introduzca valor de n:"))

# Ponemos el valor de las variables "suma" y "contador". Suma va a ser 0 porque no tiene ningun valor almacenado aun y contador va a estar en 1 porque estamos en la primera acción.

suma = 0

contador = 1

# Iniciamos el bucle hasta obtener el resultado. 

while contador <= n:

    suma += contador
    contador = contador + 1

print ("La suma total es:", suma)

    







