"""Escribe nun script unha función valor_maximo(dicionario: Dict[str, int]) -> List[str] que devolva as chaves asociadas ao valor máximo nun dicionario. Devolve unha lista con todas as claves que teñan ese valor. Aquí tes un fragmento de código para probar a función:"""

__author__ = "Alvaro Camino Martinez"

def valor_maximo(dicionario: dict[str, int]) -> list[str]:

    valor_maximo = None

# Creamos lista vacia para almacenar las claves

    claves = []

# Recorremos el dicionario buscando claves y valores

    for clave, valor in dicionario.items():

# Comprobamos que valor_maximo sea none y que el valor del dicionario es mayor que el valor maximo que como no hay, ese valor pasa a ser el nuevo valor maximo 

        if valor_maximo is None or valor > valor_maximo:

# Actualizamos el nuevo valor maximo que haya

            valor_maximo = valor

# Creamos una lista con un unico elemento que son las claves

            claves = [clave]

# Si el valor es igual al valor_maximo

        elif valor == valor_maximo:

# Añadimos la clave a la lista de claves

            claves.append(clave)

    return claves






















dicionario = {'a': 5, 'b': 3, 'c': 5, 'd': 2}

print(valor_maximo(dicionario))
# Saída esperada: ['a', 'c']