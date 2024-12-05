"""Escribe nun script unha función contar_frecuencia(lista: List[str]) -> Dict[str, int] que conte a frecuencia de cada palabra nunha lista de palabras. A función debe devolver un dicionario onde as chaves son as palabras e os valores son as frecuencias. Aquí tes un fragmento de código para probar dita función:

lista_palabras = ['mazá', 'banana', 'mazá', 'laranxa', 'banana', 'mazá']

print(contar_frecuencia(lista_palabras))"""

__author__ = "Alvaro Camino Martinez"

def contar_frecuencia(lista: list[str]) -> dict[str, int]:

# Creamos un diccionario vacio

    contador = {}

# Recorremos la lista

    for palabra in lista:

# Si nuestra palabra se encuentra en el diccionario vacio (basicamente que se repite) le sumaremos 1 por cada vex que se repita.

        if palabra in contador:

            contador[palabra] = contador[palabra] + 1

        else:
# Si la palabra esta solo una vez en el diccionario se queda con el valor 1.
            contador[palabra] = 1

    return contador
        
lista_palabras = ['mazá', 'banana', 'mazá', 'laranxa', 'banana', 'mazá']

print(contar_frecuencia(lista_palabras))