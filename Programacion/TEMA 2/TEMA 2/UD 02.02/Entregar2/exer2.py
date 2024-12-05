'''
Escribe un script que faga o cambio de divisas tanto de euros a libras e viceversa. Crea un menú para que o usuario escolla o cambio que desexa realizar e a continuación introducirá o valor da moeda correspondente para realizar o cambio de divisas. 1 € son 1,10 libras.
'''
__author__ = "Alvaro Camino Martinez"

#Creacion del menu

print ("Que cambio quiere realizar?")
print ("\ta Libras -> Euros")
print ("\tb Euros -> Lbras")

opcion = input (">")

#Creacion de condicional if para hacer los cambios de unidades mas imprimimos resultados

if opcion == 'a':
    libras = float(input("Cantidad de libras que desea cambiar?"))
    cambio_euro = libras / 1.10
    print (f"La cantidad de euros que tiene es de {cambio_euro}")
elif opcion == 'b':
    euros = float(input("Cantidad de euros que desea cambiar?"))
    cambio_libra = euros * 1.10
    print (f"La cantidad de libras que tiene es de {cambio_libra}")
else:
    print ("Error")