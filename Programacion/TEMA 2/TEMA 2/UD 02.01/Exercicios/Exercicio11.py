#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="Alvaro Camino Martinez"

salariobruto_str = input("Ingrese su salario bruto:")

IRPF_str = input("Ingrese su IRPF en tanto por cien:")

salariobruto = int(salariobruto_str)

IRPF = float(IRPF_str)

salario_neto = (salariobruto - (salariobruto * IRPF))

print (salario_neto)