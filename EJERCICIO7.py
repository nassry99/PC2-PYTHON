#Escriba una función de Python que tome un número como parámetro y verifique que el número sea
#primo o no.

def num_primo(num):
    #numeros menores o iguales a 1 son primos
    if num<=1:
        return False
    #numero divisible por si mismo o 1
    for i in range(2, int(num**0.5)+1):
        if num%1==0:
            return False
    return True
num=int(input("Ingresar el numero: "))
if num_primo:
    print(num, "es numero primo")
else:
    print(num, "no es numero primo")
