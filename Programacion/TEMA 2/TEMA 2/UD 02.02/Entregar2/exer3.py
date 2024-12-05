'''
Escribe un script que pida o nome de usuario e contrasinal ao usuario. Indica se o inicio de sesión é correcto. O nome de usuario sería “python” e o contrasinal “pip”.

'''
__author__ = "Alvaro Camino Martinez"

#Pedimos datos 

nome_usuario = "python"
contrasinal = "pip"

usuario = str(input("Introduzca su nombre de usuario:"))
clave = str(input("Introduzca su contraseña:"))

#Creacion da condicional if mais impresion do resultado

if usuario == nome_usuario and clave == contrasinal:
    print ("Los datos introducidos son correctos")

else:
    print ("Los datos introducidos no son correctos")