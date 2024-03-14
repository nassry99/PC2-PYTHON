#Problema 2:
#Escriba un programa en Python para construir el siguiente patrón.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

# numero de filas hasta la mitad
filas = 5

# imprimir la parte de arriba
for i in range(filas):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# imprimir la parte de abajo
for i in range(filas - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()