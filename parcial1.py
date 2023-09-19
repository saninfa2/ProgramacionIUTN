#PARCIAL - PROGRAMACIÓN 1 

print("Juegos")
#Pedimos el nombre del usuario
name = input("Ingresa tu nombre: ").capitalize()
print(f"¡Hey! ¡{name} bienvenid@! ")


#Inicialización de variables
option = 0
total = 0
average = 0
oddCounter = 0
aCounter = 0
eCounter = 0
iCounter = 0
oCounter = 0
uCounter = 0
number = 1
bigger = 0


#Presentamos el menú de opciones hasta que se ingrese una respuesta válida
while option != 1 and option != 2:
    print("¡Vamos a jugar!")
    print("1) Juego de números ")
    print("2) Juego de palabras ")
    option = int(input("Ingresa el número del juego seleccionado: "))
    
#JUEGO DE NUMEROS
if (option == 1):
    #Introducción al juego de números
    print(f"¡Bienvenid@ al juego de números {name}!")
    while number != 0: 
        number = int(input("Ingresa un número entero para jugar ó 0 (cero) para salir: "))
        #Verificamos numero positivos
        if number>0:
            #verificamos numero par
            if (number%2==0):
                if (number> bigger):
                    bigger = number
            #Verificamos numero impar
            elif (number%2==1):
                total += number
                oddCounter += 1 
        #los numeros negativos no son válidos
        elif (number<0):
            print(f"Error! {name}, no se pueden ingresar números negativos!")
                
    #sacamos el promedio de los números impares ingresados si el contador(divisor) es distinto de 0
    if oddCounter != 0:
        average = total/oddCounter
        
    #Mostramos los resultados del juego
    print("Fin del juego")
    print(f"{name}, aquí están los resultados: ")
    print(f"MAYOR NÚMERO PAR: {bigger}")
    print(f"PROMEDIO DE NÚMEROS IMPARES: {average}")

#JUEGO DE PALABRAS
elif (option == 2):
    #Introducción al juego de palabras
    print(f"Bienvenid@ al juego de palabras {name}")
    #pedimos la frase
    phrase = input("Ingresa una frase: ").upper()
    
    #recorremos la frase con un for en busca de vocales
    #sumamos 1 al contador cada vez que encontremos una
    for i in phrase:
        if ( i == "A"):
            aCounter += 1
        elif ( i == "E"):
            eCounter += 1
        elif ( i == "I"):
            iCounter += 1
        elif ( i == "O"):
            oCounter += 1
        elif ( i == "U"):
            uCounter += 1

    #Mostramos los resultados del juego
    print("Fin del juego")
    print(f"{name}, aquí están los resultados: ")
    print("La frase ingresada contiene: ")
    print(f"{aCounter} veces A")
    print(f"{eCounter} veces E")
    print(f"{iCounter} veces I")
    print(f"{oCounter} veces O")
    print(f"{uCounter} veces U")

        
print(f"¡Hasta pronto {name}!")
