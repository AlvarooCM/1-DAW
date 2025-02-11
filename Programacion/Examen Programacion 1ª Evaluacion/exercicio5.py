"""Exercicio 5. Débese realizar unha aplicación para xestionar as vivendas que ten a disposición unha inmobiliaria. Para cada vivenda débese saber a dirección na que se encontra, se esta está en venta ou en alugamento e o prezo de venta ou alugamento en cada caso.

A aplicación constará do seguinte menú:

a) Ingresar datos vivenda

b) Eliminar datos vivenda

Débese mostrar unha lista de vivendas nun menú e seleccionar a vivenda a eliminar segundo o índice co seguinte formato: <índice>) <dirección>. <venta|alugamento> - <prezo> €.
c) Modificar estado de venta a alugamento, ou viceversa

Débese mostrar unha lista de vivendas nun menú e seleccionar a vivenda a eliminar segundo o índice co seguinte formato: <índice>) <dirección>. <venta|alugamento> - <prezo> €.
d) Mostrar vivendas en alugamento

Débese mostrar co seguinte formato: <índice>) <dirección>. <venta|alugamento> - <prezo> €.
e) Ver o prezo de alugamento máis repetido.

En caso de empate de prezos, indica o máis baixo.
Pista: utiliza dicionarios para realizar dito cálculo.
Se non hai vivendas de alugamento devolve None
f) Ver o prezo de venta máis repetido.

En caso de empate de prezos, indica o máis baixo.
Pista: reutiliza funcións.
Se non hai vivendas en venda devolve None
g) Sair.

"""

__author__ = "Alvaro Camino Martinez"

viviendas = []

def ingresar_datos(direccion: str, estado: str, prezo: float):
    """ingresar_datos

    Args:
        direccion (str): Direccion de la vivienda
        estado (str): Estado en el que se encuentra la vivienda alugamento|venta.
        prezo (float): Prezo alugamento|venta da vivienda.

    Raises:
        ValueError: Erro tippo de datos
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
    """

    if type(direccion) is not str:
        raise ValueError
    
    if type(estado) is not str:
        raise ValueError
    
    if type (prezo) is not float:
        raise ValueError
    
    vivienda = {direccion:"direccion", estado:"venta|alugamento", prezo:"prezo"}
    viviendas.append(vivienda)

def eliminar_datos(viviendas: list, indice: int):
    """eliminar_datos

    Args:
        viviendas (list): Lista con las viviendas que se introdujeron
        indice (int): Indice para saber que vivienda se va a eliminar

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
    """

    if type(viviendas) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    viviendas.pop(indice)

def modificar_estado(viviendas: list, indice: int, nuevo_estado: str):
    """modificar_estado

    Args:
        viviendas (list): Lista con las viviendas que se introdujeron
        indice (int): Indice para saber que vivienda vamos a modificar
        nuevo_estado (str): Nuevo estado en el que se encuentra la vivienda

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error, o es venta o es alugamento 
    """

    if type(viviendas) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if type(nuevo_estado) is not str:
        raise ValueError
    
    if nuevo_estado is not 'venta' or nuevo_estado is not 'alugamento':
        raise ValueError
    
    viviendas[indice]["venta|alugamento"] = nuevo_estado

def mostrar_vivendas(viviendas: list, indice: int):
    """mostrar_vivendas

    Args:
        viviendas (list): Lista con las viviendas que se introdujeron
        indice (int): Indice para saber que vivienda es cada una

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error lista vacia
    """

    if type(viviendas) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if len(viviendas) == 0:
        raise ValueError
    
    print(viviendas)

def alugamento_repetido(viviendas: list, indice: int,):
    """alugamento_repetido

    Args:
        viviendas (list): Lista con las viviendas que se introdujeron
        indice (int): Indice para saber que vivienda es cada una

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error lista vacia
    """

    if type(viviendas) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if len(viviendas) == 0:
        raise ValueError

def venta_repetida(viviendas: list, indice: int, prezo: float):
    """venta_repetida

    Args:
        viviendas (list): Lista con las viviendas que se introdujeron
        indice (int): Indice para saber que vivienda es cada una

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error lista vacia
    """

    if type(viviendas) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if len(viviendas) == 0:
        raise ValueError
    
    precio_mas_repetido = []
    
    for indice in viviendas:

        if indice in viviendas:

            viviendas[prezo] = precio_mas_repetido [prezo] + 1 
    
def sair ():
    """sair
    """
    while True:
        print("Menú:")
        print("a) Ingresar datos vivienda")
        print("b) Eliminar datos vivienda")
        print("c) Modificar estado de venta a alugamento, ou viceversa")
        print("d) Mostrar vivendas en alugamento")
        print("e) Ver o prezo de alugamento mais repetido")
        print("f) Ver o prezo de venta mais repetido")
        print("g) Salir")

        opcion = input("Elixe unha opcion:")

        if opcion == 'a':
            direccion = input("Introduza a direccion da vivenda:")
            estado = input("Introduza o estado da vivenda (venta|alugamento):")
            prezo = float(input("Introduza o prezo da vivenda:"))
            ingresar_datos(direccion, estado, prezo)

        elif opcion == 'b':
            indice = int(input("Introduza o índice da vivenda a eliminar: "))
            eliminar_datos(viviendas, indice)

        elif opcion == 'c':
            indice = int(input("Introduza o índice da vivenda a eliminar:"))
            nuevo_estado = float(input("Introduza o novo estado da vivenda: "))
            modificar_estado(viviendas, indice, nuevo_estado)

        elif opcion == 'd':
            mostrar_vivendas(indice, viviendas)

        elif opcion == 'e':
            alugamento_repetido(viviendas, indice, ) 

        elif opcion == 'f':
            venta_repetida(viviendas, indice)

        elif opcion == 'g':
            sair()
            break
        else:
            print("Opción non válida. Tenta de novo.")