#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento.

def facto(n):
    if n ==0:
        return 1
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto

numero=int(input("Ingresar numero para calcular su factorial: "))
answer=facto(numero)
print("El factorial de", numero, "es:", answer)