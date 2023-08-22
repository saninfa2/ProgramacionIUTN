#EJERCITACIÓN DE CONDICIONALES

print("Regristro de clases - Instituto de Inglés")

#Primero pedimos la fecha
print("Ingrese la fecha a continuación.")
print("Bajo el formato: día, DD/MM")
print("Ejemplo: Lunes, 12/04")
fecha = input()
fecha = fecha.lower()

#Luego, separamos el string en día, número de día y mes
dia_semana = str(fecha[0: fecha.find(",")])
dia_numero = int(fecha[fecha.find(" ")+1 : fecha.find("/")])
mes = int(fecha[fecha.find("/")+1 :])

#Validamos el día
dia_valido = dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles" or dia_semana == "jueves" or dia_semana == "viernes"

#Validación número de día
numero_dia_valido =(dia_numero>0) and (dia_numero<=31)

#Validacaión del mes
mes_valido = (mes>0) and (mes<= 12)

#Validar si pudo haber examenes
dia_con_examenes = dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles"

if (dia_valido and numero_dia_valido and mes_valido):
    if (dia_con_examenes):
        print ("¿Hubo examen?")
        print("Ingrese si o no")
        examen = input().lower()
        if (examen == "si"):
            #si hubo examen, pedimos la cantidad de aprobados
            print("Ingrese los alumnos que aprobaron:")
            alumnos_aprobados = int(input())
            
            #También la cantidad de desaprobados
            print("Ingrese los alumnos que desaprobaron:")
            alumnos_desaprobados = int(input())
            
            #Y por último sacamos el promedio de aprobación
            porcentaje_aprobados = (alumnos_aprobados*100) / (alumnos_aprobados+alumnos_desaprobados)
            print(f"Porcentaje de aprobados: {porcentaje_aprobados}%")
            print("Operación terminada")
        else:
            print("Operación terminada")
    elif(dia_semana == "jueves"):
        print("Ingrese el porcentaje de asistencia:")
        porcentaje_asistentes = float(input())
        if (porcentaje_asistentes > 50):
            print("Asistió la mayoría")
            print("Operación terminada")
        else: 
            print("No asistió la mayoría")
            print("Operación terminada")
    elif (dia_semana == "viernes"):
        if((dia_numero == 1 and mes == 1) or mes == 7):
            print("Comienzo de nuevo ciclo")
            
            #Se pide la cantidad de alumnos del nuevo ciclo
            print("Ingrese la cantidad de alumnos del nuevo ciclo:")
            alumnos_nuevo_ciclo = int(input())
            
            #Y el arancel por cada uno de ellos
            print("Ingrese el arancel en $ por cada alumno: ")
            arancel = float(input())
            
            #Total de arancel a pagar
            print(f"Ingreso total: $ {arancel*alumnos_nuevo_ciclo}")
            print("Operación terminada")
        else:
            print("Operación terminada")
else:
    print("ERROR!Fecha inválida. Vuelva a intentarlo")


