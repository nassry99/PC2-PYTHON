#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
#fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
#1636!
#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
#la lista abajo:
#definir meses
def numero_mes(mes):
    meses = {
        "Enero":"01",
        "Febrero":"02",
        "Marzo":"03",
        "Abril":"04",
        "Mayo":"05",
        "Junio":"06",
        "Julio":"07",
        "Agosto":"08",
        "Septiembre":"09",
        "Octubre":"10",
        "Noviembre":"11",
        "Diciembre":"12",
    }
    return meses.get(mes)
#definir la conversion
def conversion_fechas(fecha):
    part=fecha.split()
    if len(part)==3:
        mes, dia , año =part
        num_mes=numero_mes(mes)
        fecha_form=f"{num_mes}/{dia}/{año}"
    elif "/" in fecha:
        mes, dia, año=fecha.split("/")
        fecha_form=f"{mes}/{dia}/{año}"
    else:
        fecha_form=fecha
    return fecha_form

#imprimiendo valores
fecha=input("Ingrese una fecha en mes-día-año o mes/día/año: ")
fecha_form=conversion_fechas(fecha)
print("Fecha en formato MM/DD/YYYY:", fecha_form)