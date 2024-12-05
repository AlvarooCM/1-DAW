""" 
Escribe un script que faga o cambio de divisas tanto de euros a libras e viceversa. Crea un menú para que o usuario escolla o cambio que desexa realizar. Realiza unha función para cada un dos cambios:

"""

__author__ = "Alvaro Camino Martinez"

# Creacion de funciones

def libras_to_euros(libras: float) -> float:
    """Cambio libras a euros

    Args:
        libras (float): Calculo de libras

    Returns:
        float: Calculo del return
    """

    return libras / 1.10


def euros_to_libras(euros: float) -> float:
    """Cambio euros a libras

    Args:
        euros (float): Calculo de euros

    Returns:
        float: Calculo del return
    """

    return euros * 1.10

# Creacion del menu

print ("Que cambio quiere realizar?")
print ("\ta Libras -> Euros")
print ("\tb Euros -> Libras")

opcion = input (">")

# Pedimos valores mas inicializamos el if mas imprimimos los resultados

if opcion == 'a':
    num_libras = float(input("Introduzca el número de libras que desea cambiar:"))
    cambio_euros = libras_to_euros(num_libras)
    print (f"Sus libras equivalen a un total de {cambio_euros}€.")

elif opcion == 'b':
    num_euros = float(input("Introduzca el número de euros que desea cambiar:"))
    cambio_libras = euros_to_libras(num_euros)
    print (f"Sus libras equivalen a un total de {cambio_libras}€.")

else:
    print ("Error")

