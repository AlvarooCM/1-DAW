#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="Alvaro Camino Martinez"

radio_str = input("Ingrese el radio de la esfera:")

radio = int(radio_str)

volumen = (radio**3 * 3.1416 * (4/3))

print (volumen)
