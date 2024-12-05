"""Un número de DNI ten o seguinte formato 00000000A.

Escribe un script que lle pida ao usuario o seu DNI e comprobe que sexa correcto. Para iso sigue os seguintes pasos:

Comproba a lonxitude da cadea.

Comproba que os 8 primeiros díxitos son números e o último é unha letra maiúscula. PISTA: utiliza a táboa do código ASCII.

Comproba que a letra introducida é o código de control do DNI. https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/#:~:text=Por%20ejemplo%2C%20si%20el%20n%C3%BAmero,n%C3%BAmeros%20y%20d%C3%ADgito%20de%20control.

Por último imprime Válido ou Inválido segundo corresponda."""

__author__ = "Alvaro Camino Martinez"

# Creo una funcion para que compruebe la validez del dni, ver si cumple con los requistos de logitud numerica mas calcular que su letra sea valida tambien.

def validar_dni (dni):

    """_summary_

    Returns:
        _type_: Comprobacion de la validez del DNI.
    """

# Creo una variable que almacena todas las letras disponibles para los DNI

    cadena_letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"

# Compruebo que la longitud de los digitos del DNI sea 9.

    if len(dni) != 9:
        return False

# Comprueba que de la posicion 0 a la 7 son numeros dando un total de 8 numeros.

    if not dni[:8].isdigit():
        return False

# La posicion 8 queda asignada a la letra del DNI

    if not dni[8].isalpha():
        return False

# Paso la cadena de texto de los numeros del DNI a numericos enteros. Tambien hacemos el calculo y comprobamos que la letra del DNI sea valida 

    numeros_dni = int(dni[:8])
    calculo_letra = cadena_letras_dni[numeros_dni % 23]

    return dni[8] == calculo_letra

# Pedimos el DNI al usuario

dni_usuario = input("Introduzca su DNI:")

# Comprobamos si el DNI introducido por el usuario es valido

if validar_dni(dni_usuario):
    print ("Valido")
else:
    print ("Invalido")


    
