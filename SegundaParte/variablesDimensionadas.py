""""Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Por ejemplo:
*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa."""

#FUNCIONES 
def buscarPasajeros(destino, dni, tupla1, tupla2):
    if (destino == 1):
        tupla = tupla1
    elif(destino == 2):
        tupla = tupla2
   
            
        
            


#PROGRAMA PRINCIPAL 
print("Control de pasajeros - Ejercicio 1")

#Inicializamos las variables
listTuplePassengers = []
listTupleCountry = []
j = 1
exit_ = 0

print("Bienvenido. Ingrese al opción que desee realizar: ")
print("(1) para agregar pasajeros o ciudades - (2) para buscar por DNI, ciudad o país - (3) para salir")
option = int(input("Ingrese el número de la opción elegida: "))
optionValid = option == 1 or option == 2 or option == 3
if (optionValid and exit_ != 1):
    if (option == 1):
        print("¿Desea ingresar pasajeros o ciudades?")
        optionAdd = int(input("Ingrese 1 para agregar pasajeros o 2 para agregar ciudades: "))
        if optionAdd == 1:
            #Se piden los datos personales del pasajeto 
            print("Ingrese los datos de los pasajos")
            name_complete = input("Ingrese el nombre completo del pasajero: ").capitalize()
            dni = int(input("Ingrese el DNI del pasajero: "))
            destination = input("Ingrese el lufar de destino del pasajero: ").capitalize()
            tuple = {name_complete, dni, destination}
            listTuplePassengers += tuple
        elif (optionAdd == 2):
            province = input("Ingrese la provincia o ciudad de la que proviene el pasajero: ").capitalize()
            country = input("Ingrese el país de proveniencia del pasajero: ").capitalize()
            tuple2 = {province, country}
            listTupleCountry += tuple2
        else: 
            print("Error! Opción invalida")
    elif (option == 2):
        print("Bienvenido a la sección de busqueda")
        
        #Para simplificar código generalizamos en la opciones de busqueda
        print("(1) para buscar el destino de un pasajero según su DNI")
        print("(2) para buscar cuántos pasajeros viajan a determinado destino")
        optionAdd = int(input("Ingrese la opción elegida: "))
        if (optionAdd == 1):
            DNIAnswer = int(input("Ingrese el DNI del pasajero"))
            print("¿Desea buscar por ciudad o por país?")
            optionCityOrCounty = int(input("Ingrese 1 para ciudad y 2 para país: "))
            buscarPasajeros(optionCityOrCounty, DNIAnswer, listTuplePassengers)
    elif (option == 3):
        exit_ = 1
    else:
        print("Error! Opción invalida")
    
        









while(j != 0):
    
    
    #También pedimos los datos del lugar de proveniencia del pasajero 
    
    
    #Condición de salida: si se ingresa 0 sale sino no
    j = input("¿Desea salir? Ingrese 0 para salir y cualquier número para agregar más pasajeros")
    
    