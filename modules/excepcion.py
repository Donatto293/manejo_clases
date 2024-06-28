"""manejo de errores y entradas de datos"""
#asegura la entrada de cadenas de texto
def verificacionTexto(mensaje):
    while True:
            texto=input(mensaje)
            if texto.replace(" ","").isalpha():
                return texto
            else:
                print("digite solo caracteres  alfabeticos")

                
#asegura la entreda de datos numericos como documentos, pero los convierte en string
def verificacionNumerosSTR(mensaje):
    while True:
        try:
            texto=int(input(mensaje))
            texto=str(texto)
            if texto.isdigit():
                texto=str(texto)
                return texto
        except ValueError:
                print("digite solo caracteres  numericos")


 #asegura la entrada de numeros floats               
def solicitar_dato_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError: 
            print("Error: El valor ingresado no es un número válido. Inténtelo de nuevo.")


#verificacion de dato int
def solicitar_dato_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError: 
            print("Error: El valor ingresado no es un número válido. Inténtelo de nuevo.")