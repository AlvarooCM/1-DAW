#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Un número de DNI ten o seguinte formato `00000000A`.

Escribe un *script* que lle pida ao usuario o seu DNI e comprobe que sexa correcto. Para iso sigue os seguintes pasos:

- Comproba a lonxitude da cadea.

- Comproba que os 8 primeiros díxitos son números e o último é unha letra maiúscula. *PISTA*: utiliza a táboa do código ASCII.

- Comproba que a letra introducida é o código de control do DNI. http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie

Por último imprime `Válido` ou `Inválido` segundo corresponda.
"""

__author__ = "Manuel Ramón Varela López"

# Collemos o DNI
dni_str = input("Introduce o DNI: ")

# Este e o orde das letras, o resto do número correspondese co seu DNI
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

# Entendemos que o DNI é válido polo que buscamos se nalgún momento é inválido
valido = True

# Comprobamos se son 9 caracteres
if len(dni_str) == 9:
    # Collemos os 8 primeiros caracteres
    numeros_str = dni_str[:8]
    try:
        # Tratamos de pasalos a un numero
        numeros = int(numeros_str)
        
        # Miramos se a letra é maiuscula
        letra = dni_str[8]
        if letra >= "A" and letra <= "Z":
            # Calculamos a letra
            resto = numeros % 23
            letra_verdadeira = letras[resto]
            # Comprobamos se a letra introducida e a mesma que a calculada
            if letra_verdadeira != letra:
                valido = False
        else:
            # A letra non é maiuscula
            valido = False
    except:
        # Os 8 primeiros caracteres non son números
        valido = False
else:
    # Non son 9 caracteres
    valido = False

# Imprimimos se é válido ou non
if valido:
    print("Válido")
else:
    print("Inválido")



