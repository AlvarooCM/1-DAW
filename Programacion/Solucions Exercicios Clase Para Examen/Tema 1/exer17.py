#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribe un script que pida ao usuario o número de quilómetros recorridos na súa última viaxe en coche, 
o consumo do coche en litros cada 100 quilómetros e o prezo en euros dun litro de combustible. Calcula o custo da viaxe 
e móstrallo ao usuario por pantalla.
"""

__author__ = "Manuel Ramón Varela López"

# Solicitamos datos ao usuario
km = float(input("Cantos kilometros recorriches? "))
consumo = float(input("Cal é o consumo do seu coche cada 100 km? "))
prezo_combustible = float(input("Cal é o prezo do combustible por litro en €? "))

# Realizamos os calculos
combustible_consumido = km * (consumo/100)
custo = combustible_consumido * prezo_combustible

# Mostramos o resultado
print("O gasto da viaxe foron", custo, "€")
