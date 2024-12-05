"""Escribe nun script unha función agrupar_datos_por_valor(dicionario: Dict[str, List[int]]) -> Dict[int, List[str]] que reciba un dicionario onde os valores son listas e devolva un novo dicionario que agrupe as claves segundo os valores que teñen en común..Aquí tes un fragmento de código para probar a función:"""

__author__ = "Alvaro Camino Martinez"

def agrupar_datos_por_valor(dicionario: dict[str, list[int]]) -> dict[int, list[str]]:

    dicionario_nuevo = {}

    for clave, lista in dicionario.items():
      
        for numero in lista:
         
            if numero in dicionario_nuevo:

                dicionario_nuevo[numero].append(clave)

            else:

                dicionario_nuevo[numero] = [clave]
     
        return dicionario_nuevo
         

dicionario = {'a': [1, 2], 'b': [2, 3], 'c': [1, 4]}
print(agrupar_datos_por_valor(dicionario))
# Saída esperada:
# {1: ['a', 'c'], 2: ['a', 'b'], 3: ['b'], 4: ['c']}