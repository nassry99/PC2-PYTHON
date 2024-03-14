#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.
#Ejemplo:
#“Desea ingresar un número?”: SI
#“Ingrese el número:” 5
#“¿Desea ingresar un número?”: SI
#“Ingrese el número: ” 7
#……
#“Desea ingresar un número?”: NO
#Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
#Cantidad de números pares: 5
#Cantidad de números impares: 4

#definir 
num=[]
pares=0
impares=0

#definir while
while True:
    answer=input("Desea ingresar un numero?: ").upper()
    if answer == "SI":
        numero= int(input("ingresar numero?:"))
        num.append(numero)
        if numero % 2 == 0:
            pares+=1
        else:
            impares+=1
    elif answer == "NO":
        break
    else: 
        print("Respuesta invalida. Responda si o no.")
print("numeros ingresados", num)
print("Muestres los numeros pares", pares )
print("muestre los numero impares", impares)