#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="Alvaro Camino Martinez"

radio_str = input("Ingrese el radio del cilindro:")

altura_str = input("Ingrese la altura del cilindro:")

radio= float(radio_str)

altura = float(altura_str)

volumen = (3.1416 * altura * radio**2)

print (volumen)