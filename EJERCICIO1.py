#Problema 1:
#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

#numeros divisibles 
num_divisibles=[]

#iteraccion for
for numero in range(1500,2700):
    #divisores 5 y 7 
    if numero % 7 and numero % 5 == 0:
        #si cumple ambas
        num_divisibles.append(numero)
#impresion 
print("Los numeros divisibles entre 1500 y 2700 divisores de 5 y 7 son:" )
print(num_divisibles)