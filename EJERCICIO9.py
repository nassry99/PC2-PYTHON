#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
#minúsculas.

def vocales_quitar(twittear):
    vocales=['a','e','i','o','u','A','E','I','O','U']
    twittear_sin=""
    for q_vocales in twittear:
        if q_vocales not in vocales:
            twittear_sin+=q_vocales
    return twittear_sin
twittear=(input("Ingrese el twitter: "))
twittear_sin=vocales_quitar(twittear)
print("twittear abreviado:", twittear_sin)