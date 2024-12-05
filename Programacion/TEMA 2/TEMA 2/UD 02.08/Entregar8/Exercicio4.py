"""Realiza unha aplicación co seguinte menú:

a) Ingresar datos alumno

b) Eliminar datos alumno

Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a eliminar segundo o índice co seguinte formato: indice. apelidos_alumno, nome: nota.
c) Modificar nota alumno

Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a modificar a nota o índice co seguinte formato: indice. apelidos_alumno, nome: nota.
d) Ver nomes e apelidos de alumnos aprobados

Débese mostrar co seguinte formato: indice. apelidos_alumno, nome: nota
e) Mostra alumnos alfabeticamente:

Débese mostrar co seguinte formato: indice. apelidos_alumno, nome: nota
Podes adaptar o algoritmo de ordenación da tarefa anterior.
f) Ver a nota media.

g) Sair.

Para cada alumno necesitaremos gardar os seguintes datos:

Nome
Apelidos
Nota con decimais."""

__author__ = "Alvaro Camino Martinez"

alumnos = []

def ingresar_datos(apelidos: str, nome: str, nota: float):
    """ingresar datos

    Args:
        apelidos (str): apelidos alumno
        nome (str): nome alumno
        nota (float): nota alumno

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
    """
    # Verifica que o nome, apelidos e nota sexan do tipo adecuado
    if type(nome) is not str:
        raise ValueError
    
    if type(apelidos) is not str:
        raise ValueError
    
    if type(nota) is not float:
        raise ValueError
    
    # Verifica que a nota estea dentro do rango válido
    if nota < 0 or nota > 10:
        raise ValueError
    
    # Engade os datos do alumno á lista de alumnos
    alumno = {nome:"nombre", apelidos:"apelidos", nota:"nota"}
    alumnos.append(alumno)


def eliminar_datos(alumnos: list, indice: int):
    """eliminar datos

    Args:
        alumnos (list): lista alumnos
        indice (int): indice lista

    Raises:
        ValueError: Error tipo de datos
        ValueError: Error tipo de datos
        ValueError: Error lista vacia
    """
    # Verifica que os parámetros sexan correctos
    if type(alumnos) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    # Verifica que o índice sexa válido
    if indice < 0 or indice > len(alumnos):
        raise ValueError
    
    # Elimina o alumno na posición indicada
    alumnos.pop(indice)


def modificar_nota(alumnos: list, indice: int, nueva_nota: float):
    # Verifica que os parámetros sexan correctos
    if type(alumnos) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if type(nueva_nota) is not float:
        raise ValueError
    
    # Verifica que o índice sexa válido
    if indice < 0 or indice > len(alumnos):
        raise ValueError
    
    # Verifica que a nova nota sexa válida
    if nueva_nota < 0 or nueva_nota > 10:
        raise ValueError
    
    # Modifica a nota do alumno no índice indicado
    alumnos[indice]["nota"] = nueva_nota


def ver_aprobados(alumnos: list, indice: int, nota: float):
    # Verifica que os parámetros sexan correctos
    if type(alumnos) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    if type(nota) is not float:
        raise ValueError
    
    # Verifica que a lista de alumnos non estea vacía
    if len(alumnos) == 0:
        raise ValueError
    
    alumnos_aprobados = []

    # Filtra os alumnos aprobados (nota >= 5)
    for alumno in alumnos:
        if alumnos["nota"] >= 5:
            alumnos_aprobados.append(alumno)
    
    # Mostra os alumnos aprobados
    if len(alumnos_aprobados) == 0:
        print("Non hai alumnos aprobados.")
    else:
        print("Alumnos aprobados:")

        for indice, alumno in enumerate(alumnos_aprobados):
            print(f"{indice}. {alumno['apelidos']}, {alumno['nome']}: {alumno['nota']}")

def mostrar_alfabeticamente(alumnos: list, indice: int):
    # Verifica que os parámetros sexan correctos
    if type(alumnos) is not list:
        raise ValueError
    
    if type(indice) is not int:
        raise ValueError
    
    # Verifica que a lista de alumnos non estea vacía
    if len(alumnos) == 0:
        raise ValueError

    n = len(alumnos)

    i = 0

    # Ordena os alumnos alfabéticamente por apelidos e nome
    while i < n:
        j = 0
        while j < n - i - 1:
            if (alumnos[j]['apelidos'] > alumnos[j + 1]['apelidos'] or
               (alumnos[j]['apelidos'] == alumnos[j + 1]['apelidos'] and
                alumnos[j]['nome'] > alumnos[j + 1]['nome'])):
                alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
            j += 1
        i += 1

    # Mostra os alumnos ordenados alfabéticamente
    print("Alumnos ordenados alfabeticamente:")

    i = 0

    while i < len(alumnos):
        alumno = alumnos[i]
        print(f"{i}. {alumno['apelidos']}, {alumno['nome']}: {alumno['nota']}")
        i += 1


def nota_media(alumnos: list):
    # Verifica que os parámetros sexan correctos
    if type(alumnos) is not list:
        raise ValueError

    # Verifica que a lista de alumnos non estea vacía
    if len(alumnos) == 0:
        raise ValueError

    suma_notas = 0
    contador = 0

    # Suma as notas válidas
    for alumno in alumnos:
        if 'nota' in alumno and type(alumno['nota']) in (int, float):
            suma_notas += alumno['nota']
            contador += 1
        else:
            raise ValueError

    # Verifica que hai alumnos con nota válida
    if contador == 0:
        raise ValueError

    # Calcula e mostra a media das notas
    media = suma_notas / contador
    print(f"A nota media dos alumnos e {media}.")


def sair():
    # Imprime mensaxe de saída
    print("Saindo do menú")


def menu():
    while True:
        # Mostra o menú de opcións
        print("Elixe unha opción:")
        print("a) Ingresar datos alumno")
        print("b) Eliminar datos alumno")
        print("c) Modificar nota alumno")
        print("d) Ver nomes e apelidos de alumnos aprobados")
        print("e) Mostrar alumnos alfabéticamente")
        print("f) Ver a nota media")
        print("g) Sair")

        opcion = input("Elixe unha opcion:")

        # Chama á función correspondente según a opción seleccionada
        if opcion == 'a':
            nome = input("Introduza o nome do alumno: ")
            apelido = input("Introduza o apelido do alumno: ")
            nota = float(input("Introduza a nota do alumno: "))
            ingresar_datos(apelido, nome, nota)

        elif opcion == 'b':
            indice = int(input("Introduza o índice do alumno a eliminar: "))
            eliminar_datos(alumnos, indice)

        elif opcion == 'c':
            indice = int(input("Introduza o índice do alumno a modificar a nota: "))
            nova_nota = float(input("Introduza a nova nota: "))
            modificar_nota(alumnos, indice, nova_nota)

        elif opcion == 'd':
            ver_aprobados(alumnos)

        elif opcion == 'e':
            mostrar_alfabeticamente(alumnos)

        elif opcion == 'f':
            nota_media(alumnos)

        elif opcion == 'g':
            sair()
            break
        else:
            print("Opción non válida. Tenta de novo.")

# Chama á función do menú
menu()





