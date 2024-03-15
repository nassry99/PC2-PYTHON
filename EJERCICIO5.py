#Problema 5:
#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
#Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
#Ejemplo:
#Número ingresado: 15789000 y Dígito: 0
#Cantidad de veces 0 en el número: 4
#Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método count.

def contar_digitos( numero, digito):
    numero_txt=str(numero)
    contador=0
    #crear un cadena for
    for i in numero_txt:
        if i == str(digito):
        #incrementar el contador 
            contador=+1
    return contador
#ingresar datos 
numero_dato=int(input("Ingrese numero entero: "))
digito_contador=int(input("Ingresar digito a contar: "))

cantidad=contar_digitos(numero_dato,digito_contador)
print(f"cantidad de veces {digito_contador} en el numero {numero_dato}")

