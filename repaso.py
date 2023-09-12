"""Este ejercicio se realiza en grupo, pero la entrega es individual.

Crear un programa utilizando todo lo aprendido hasta el momento.

Condicionales
Iteraciones (for / while)
Break / Continue"""
#una nave espacial que requiere para arrancar
# de todos los tripulantes y encerder el botón del motor
arranque_motor = False
presencia_tripulantes = False
contador_presentes = 0

while arranque_motor == False and presencia_tripulantes == False:
    print("1) Encender motor")
    print("2) Verificar tripulación")
    option = int(input("Ingrese la opción deseada: "))
    if option == 1:
        while arranque_motor == False:
            motor_switch = input("Para comenzar, coloque ON en la consola para prender el motor ").upper()
            if motor_switch == "ON":
                arranque_motor=True
                break
            else:
                print("Es necesario que inicie el motor para continuar")
                continue
    elif option == 2:
        print("Verificación de tripulación")
        cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
        for i in range(cantidad_tripulantes):
            print("P) Presente")
            print("A) Ausente")
            presente = input("Ingrese P o A según corresponda:").upper()
            if (presente == "P"):
                contador_presentes += 1
                print(f"Tripulante {i} presente")
            else:
                break
    else: 
        print("Opcion inválida")

