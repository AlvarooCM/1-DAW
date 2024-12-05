""" 
Escribe un script que pida o nome de usuario e contrasinal ao usuario. Indica se o inicio de sesión é correcto. O nome de usuario correcto sería “python” e o contrasinal “pip”. Crea a función
"""

__author__ = "Alvaro Camino Martinez"

# Creacion de la funcion

def login(usuario: str, contrasinal: str) -> bool:
    """Login

    Args:
        usuario (str): Nombre usuario
        contrasinal (str): Contraseña del usuario

    Returns:
        bool: Valor del return booleano
    """

    if usuario == "python" and contrasinal == "pip":
        return True
    else:
        return False
    
# Pedimos valores de las variables al usuario mas imprimimos los resultados

usuario = str(input("Introduzca su nombre de usuario:")) 
contrasinal = str(input("Introduzca su contraseña:"))  
    
login_optimo = login (usuario, contrasinal)

print (login_optimo)

