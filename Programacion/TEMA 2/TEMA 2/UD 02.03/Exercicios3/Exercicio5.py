'''
 Escribe un script que imprima os números pares comprendidos nun intervalo (a,b), un en cada liña. Os valores a e bserán introducidos por teclado polo usuario. Unha vez introducido o intervalo, verificar se a é menor que b. Senón é así, invertede os valores. Se os números son iguais imprime Erro.

'''
__author__ = "Alvaro Camino Martinez"

a = int(input("Introduzca un valor:"))
b = int(input("Introduzca un valor:"))

if a < b:
    if a % 2 != 0:
        a = a + 1
    while a < b:
        print (a)
        a = a + 2
elif b < a:
    if b % 2 != 0:
        b = b + 1
    while b < a:
        print (b)
        b = b + 2
else:
    print ("Erro")
