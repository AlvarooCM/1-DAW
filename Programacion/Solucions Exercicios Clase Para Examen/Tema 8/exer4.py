#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Realiza unha aplicación co seguinte menú:

- `a) Ingresar datos alumno`

- `b) Eliminar datos alumno`
    - Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a eliminar segundo o índice co seguinte formato: `indice. apelidos_alumno, nome: nota`.

- `c) Modificar nota alumno`
    - Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a modificar a nota o índice co seguinte formato: `indice. apelidos_alumno, nome: nota`.

- `d) Ver nomes e apelidos de alumnos aprobados`
    - Débese mostrar co seguinte formato: `indice. apelidos_alumno, nome: nota`

- `e) Mostra alumnos alfabeticamente`: 
    - Débese mostrar co seguinte formato: `indice. apelidos_alumno, nome: nota`
    - Podes modificar a función do método da burbulla de tarefas anteriores.

- `f) Ver a nota media`.

- `g) Sair`.

Para cada alumno necesitaremos gardar os seguintes datos:

- Nome
- Apelidos
- Nota con decimais.

Axuda:
- A información de cada alumno almacenarase nun dicionario.
- Para gardar a información de cada alumno utilizaremos unha lista.

"""

__author__ = "Manuel Ramón Varela López"

def comprobar_nota(nota):
    """
    Comproba que unha nota é correcta

    Args:
        nota (): A nota a comprobar
    Returns:
        boolean: verdadeiro se un float entre 0 e 10, falso en caso contrario
    """
    if not(type(nota) is float or type(nota) is int):
        return False
    if nota > 10 or nota <0:
        return False
    return True


def crear_alumno(nome, apelidos, nota):
    """
    Crea un dicionario que representa un alumno

    Args:
        nome (str): Nome do alumno
        apelidos (str): Apelidos do alumno
        nota (float): Nota do alumno
    Returns:
        dict: dicionario que representa o alumno
    Raises:
        ValueError: Se o nome e apelidos non son str ou se a nota non é un número
    """
    if not(type(nome) is str):
        raise ValueError
    if not(type(apelidos) is str):
        raise ValueError
    if not comprobar_nota(nota):
        raise ValueError

    return {
        "nome": nome,
        "apelidos": apelidos,
        "nota": nota
    }

def comprobar_alumno(alumno):
    """
    Comproba que o dicionario alumno ten os atributos que necesitamos e como tipo de datos

    Args:
        alumno (dict): Alumno
    Returns:
        boolean: verdadeiro se o dicionario que representa ao alumno e correcto 
    """
    if not(type(alumno) is dict):
        return False
    if "nome" not in alumno or "apelidos" not in alumno or "nota" not in alumno:
        return False
    if type(alumno["nome"]) is not str or type(alumno["apelidos"]) is not str or not comprobar_nota(alumno["nota"]):
        return False
    return True 

def engadir_alumo(alumnado, alumno):
    """
    Engade un alumno a lista

    Args:
        alumnado (list): Lista de alumnado
        alumno (dict): Alumno
    Raises:
        ValueError: Se a lista non é un list, ou se os seus elementos non son dicionarios que representen un alumno
    """
    # Comprobamos o tipo de datos
    if not(type(alumnado) is list):
        raise ValueError
    if not comprobar_alumno(alumno):
        raise ValueError
    
    # Gardamolo na lista
    alumnado.append(alumno)

def imprimir_alumnado(alumnado):
    """
    Imprime unha lista dos alumnos co seu respectivo indice

    Args:
        alumnado (list): A lista de alumnado
    Raises:
        ValueError: Se a lista non é un list, ou se os seus elementos non son dicionarios que representen un alumno
    """
    # Comprobamos que sexa unha lista
    if not(type(alumnado) is list):
        raise ValueError

    for valor in alumnado:
        # Comprobamos que sexa un alumno
        if not comprobar_alumno(valor):
            raise ValueError

    for indice, valor in enumerate(alumnado):
        alumno_str = str(indice) + ". " + valor["apelidos"] + ", " + valor["nome"] + ": " + str(valor["nota"])
        print(alumno_str)


def eliminar_alumno(alumnado, indice):
    """
    Elimina un alumno

    Args:
        alumnado (list): A lista do alumnado
        indice (int): O índice a eliminar

    Raises:
        ValueError: Se o índice non é correcto ou a lista non é unha list
    """
    # Comprobamos que sexa unha lista
    if not(type(alumnado) is list):
        raise ValueError
    if not(type(indice) is int):
        raise ValueError
    if indice >= 0  and indice < len(alumnado):
        alumnado.pop(indice)
    else:
        raise ValueError

def modificar_nota(alumnado, indice, nova_nota):
    """
    Modifica a nota dun alumno

    Args:
        alumnado (list): A lista do alumnado
        indice (int): O indice do alumno
        nova_nota (float): A nova nota

    Raises:
        ValueError: Se a lista non é unha lista, se a nota non é válida ou se o índice na lista non existe
    """
    # Comprobamos que sexa unha lista
    if not(type(alumnado) is list):
        raise ValueError
    if not(type(indice) is int):
        raise ValueError

    if not comprobar_nota(nova_nota):
        raise ValueError    

    if indice >= 0  and indice < len(alumnado):
        alumno = alumnado[indice]
        alumno["nota"] = nova_nota
        alumnado[indice] = alumno
    else:
        raise ValueError

def alumnado_aprobado(alumnado):
    """
    Obtemos unha lista de aprobados

    Args:
        alumnado (list): A lista de todo o alumnado

    Returns:
        list: A lista co alumnado aprobado
    Raises:
        Se a lista non é un list, ou se os seus elementos non son dicionarios que representen un alumno
    """
    if not(type(alumnado) is list):
        raise ValueError
    
    aprobados = []
    for alumno in alumnado:
        if not comprobar_alumno(alumno):
            raise ValueError
        if alumno["nota"] >= 5:
            aprobados.append(alumno)
    return aprobados

def nota_media(alumnado):
    """
    Obtemos a media de notas

    Args:
        alumnado (list): A lista de todo o alumnado

    Returns:
        float: A media das notas
    Raises:
        Se a lista non é un list, ou se os seus elementos non son dicionarios que representen un alumno
    """
    if not(type(list) is list):
        raise ValueError
    suma = 0
    for alumno in alumnado:
        if not comprobar_alumno(alumno):
            raise ValueError
        suma += alumno["nota"]
    if len(alumnado) > 0:
        return suma/len(alumnado)
    else:
        return 0


def burbulla(alumnado):
    """
    Función que ordena unha lista de alumnos

    Args:
        lista (str): Lista a ordenar
    Raises:
        Se a lista non é un list, ou se os seus elementos non son dicionarios que representen un alumno
    """
    # Comprobamos o tipo de datos
    if not(type(alumnado) is list):
        raise ValueError
    
    for alumno in alumnado:
        if not comprobar_alumno(alumno):
            raise ValueError

    # Iniciamos a variable que indica que existeu cambio de posicions a verdadeiro
    movido_elemento = True

    # Mestres que se movera algun elemento seguimos comprobando se esta ordenada a lista
    while movido_elemento:

        # Antes de comezar a mover, indicamos que inda non ficemos ningun movemento
        movido_elemento = False

        # Recorremos tódolos índices menos o último
        for indice in range(len(alumnado) - 1):

            # Collemos o valor dun indice e o do seu seguinte
            elemento_esquerda = alumnado[indice]
            elemento_dereita = alumnado[indice + 1]

            # Comprobamos se os elementos estan en orde
            elemento_dereita_str = (elemento_dereita["apelidos"] + " " + elemento_dereita["nome"]).lower()
            elemento_esquerda_str = (elemento_esquerda["apelidos"] + " " + elemento_esquerda["nome"]).lower()
            if  elemento_dereita_str < elemento_esquerda_str:
                # Como non o estan, intercambiámolos
                alumnado[indice] = elemento_dereita
                alumnado[indice + 1] = elemento_esquerda
                # Indicamos que realizamos un movemento
                movido_elemento = True

### Programa principal
alumnado = []

while True:
    print("Elixe unha opción: ")
    print("a) Ingresar datos dun alumno.")
    print("b) Eliminar datos dun alumno.")
    print("c) Modificar nota alumno.")
    print("d) Ver o alumnado aprobado")
    print("e) Mostrar alumnado alfabeticamente")
    print("f) Ver a nota media")
    print("g) Saír")
    opcion = input("> ")

    ## a) Ingresar datos dun alumno.
    if opcion == "a":
        try:
            # Collemolos datos
            nome = input("Introduce o nome: ")
            apelidos = input("Introduce os apelidos: ")
            nota = float(input("Introduce a súa respectiva nota: "))

            # Creamos o alumno representado nun dicionario e engadimolo
            alumno = crear_alumno(nome, apelidos, nota)            
            engadir_alumo(alumnado, alumno)
        except:
            print("Introduce valores válidos.")

    ## b) Eliminar datos dun alumno.
    elif opcion == "b":
        try:
            # Imprimimos o alumnado
            imprimir_alumnado(alumnado)
            indice = int(input("Índice do alumno a borrar: "))
            eliminar_alumno(alumnado, indice)
        except:
            print("Introduce un índice válido")

    ## c) Modificar nota alumno.
    elif opcion == "c":
        try:
            # Imprimimos o alumnado
            imprimir_alumnado(alumnado)
            indice = int(input("Índice do alumno a modificar: "))
            nova_nota = float(input("Introduce a nova nota: "))
            modificar_nota(alumnado, indice, nova_nota)
        except:
            print("Introduce un índice válido")

    ## d) Ver o alumnado aprobado
    elif opcion == "d":
        try:
            # Imprimimos o alumnado aprobado
            imprimir_alumnado(alumnado_aprobado(alumnado))
        except:
            print("Aconteceu un problema coa lista")

    ## e) Mostrar alumnado alfabeticamente
    elif opcion == "e":
        try:
            # Ordenamos a lista
            burbulla(alumnado)
            # Imprimimos
            imprimir_alumnado(alumnado)
        except:
            print("Aconteceu un problema coa lista")

    ## f) Ver a nota media
    elif opcion == "f":
        try:
            print(nota_media(alumnado))
        except:
            print("Aconteceu un problema coa lista")

    elif opcion == "g":
        break

    else:
        print("Opcion incorrecta")