#Problema 4:
#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias.
#Puede usar el siguiente esquema a manera de ejemplo
#{
#Alumno: Juan,
#Notas: [10, 12, 15]
#}
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
#completo de los alumnos.
#Nota:
#El uso de listas con diccionarios le será de utilidad

#creando el diccionario
alumnos={}
#solicitar el numero de alumnos
num_alumnado=int(input("Cuantos alumnos hay?"))

for i in range(0,num_alumnado+1):
    name=input(f"Ingrese los nombres del alumno{i}: ")
    #las 3 notas 
    notas=[int(input(f"Ingrese las notas {j+1} del alumno {i} :")) for j in range(3)]
    #almacenar las notar
    alumnos[name]=notas
print("\nListado de alumnos y sus notas:")
for name, notas in alumnos.items():
    print(f"Alumno: {name}, Notas: {notas}")