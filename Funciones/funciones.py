#--------------------------------FUNCIONES PARA REUTILIZAR---------------------------------
import math;

#Solicitar números al usuario hasta que ingrese cero. Por cada uno mostrar la suma de sus digitos
def add_digits (number):
    add = 0
    while number != 0:
        digit = number%10
        add += digit
        number //=10
    return add

#------------------------------------FUNCIONES DEL TP 5--------------------------------------------

#Funcion 1 - Valida un número de DNI 
def verificarDNI(dni): 
    longDNI = len(str(dni))
    if ((longDNI <= 7) and (longDNI >= 8)):
        return True

#Función 2 - Cuenta la longitud de la última palabra de una frase
def medirUltimaPalabra(frase):
    #Con strip eliminamos los espacios del principio y final de la frase
    fraseSinEspacios = frase.strip()
    #Con split separamos la frase en palabras
    listPalabras = fraseSinEspacios.split()
    #Luego seleccionamos la última
    ultimaPalabra = listPalabras[-1]
    return len(ultimaPalabra)

#Funcion 3 - Crea un identificar a partir del nombre, apellido y dni
def definirIdentificador(nameComplete, lastName, dni):
    firstName = nameComplete[0:nameComplete.find(" ")].capitalize()
    lenLastName = len(lastName)
    firstThreeDigits = dni[0:3]
    identifier = firstName + str(lenLastName) + firstThreeDigits
    return identifier

#Funcion 4 - Verificar si el primer número es multiplo del segundo
def verificarMultiplo(numero1, numero2):
    if((numero1 % numero2 == 0)):
        return True
    
#Funcion 5 - Sacar la temperatura media con la maxima y minima
def mediarTemperatura(maxima, minima):
    return int(((minima+maxima)/2))

#Función 6 - Agregar espacios después de cada letra
def agregarEspaciado(cadena):
    resultado = ""
    for letra in cadena:
        resultado += letra + " "
    cadena = resultado
    return cadena
 
#Función 7 - Recorrer una lista de números y devolver el mayor y el menor
def encontrarMayorMenorLista(listaNumeros):
    elMayor = 0
    elMenor = 0
    i=0
    for i in listaNumeros:
        if(listaNumeros[i]> elMayor):
            elMayor = listaNumeros[i]
        if(listaNumeros[i] < elMenor):
            elMenor = listaNumeros[i]
    mayorYMenor = [elMenor, elMayor]
    return mayorYMenor
        
#Funcion 8 - Calcular el área y perímetro de una circunferencia
def calcularAreaYPerimetroCircunferencia(radio):
    area = math.pi * (math.pow(radio, 2))
    perimetro =  2*math.pi*(radio)
    areaYPer = [area, perimetro]
    return areaYPer
        
        
#Función 9 - Simulador de login
def login(usuario, contrasenia, intento):
    acceso = False
    if (usuario == "usuario1" and contrasenia == "asdasd" and intento<3):
        acceso = True
    else:
        intento+= 1
    info = [acceso, intento]
    return info
    
    
#Función 10 - aplicar descuentos a un diccionario de precios  
def apply_discount(cart, discounts):
    total_price = 0

    for product, price in cart.items():
        if product in discounts:
            discount_percentage = discounts[product]
            discounted_price = price - (price * discount_percentage / 100)
            total_price += discounted_price
        else:
            total_price += price

    return total_price

#Función 11 - calculadora de cuadrados, funcion primaria de ejercicio 11
def square(x):
    return x*x

#Función 12 - funcion que recibe una función y una lista y devuelve una lista con el resultado de aplicar a la primera la funcion pasada como parametro
def applyOtherFucntion(fucntion, lista):
    resultOfFirstFucntion = []
    for item in lista:
        result = fucntion(item)
        resultOfFirstFucntion.append(result)
    
    return resultOfFirstFucntion
    
#FUNCION BASE PARA MOSTRAR UNA LISTA DE FORMA BONITA
def showList(list):
    for elemento in range(len(list)):
        if elemento < (len(list)-1):
            print(list[elemento], end=", ")
        else: 
            print(list[elemento])  
            

#Funcion 13 - función que recibe una frase y devuelve un diccionario con la palabra y su respectiva longitud
def wordsLengthsInPhrase(phrase): 
    words = phrase.split()
    wordLengths = {word: len(word) for word in words}
    return wordLengths

#Funcion 14 - función para calcular el modulo de un vector
#Pedimos el vector
def vector_modulus(vector):
    #Hacemos la suma del cuadro de los elementos del vector recorriendolos con un bucle for
    squared_sum = sum(x**2 for x in vector)
    print(squared_sum)
    #Sacamos la raíz de la suma de los cuadrados
    modulus = math.sqrt(squared_sum)
    #Retornamos el modulo 
    return modulus


#Funcion 15 - Funcion que recibe un número entero y determina si es primo
def numberPrime(number):
    isPrime = True
    if number==0 or number == 1 or number == 4:
        isPrime = False
    else: 
        i = 2
        while(i < number):
            if number% i == 0:
                isPrime = False
                break
            i+=1
    return isPrime

#Función 17 - frecuencia de un digito en un número
def countOccurrence(number, digit):
    # Conviertimos el número a una cadena para facilitar el procesamiento
    number_str = str(number)
    
    # Inicializa un contador para llevar el registro de las ocurrencias
    counterOccurrence = 0
    
    # Itera a través de los dígitos en la cadena del número
    for d in number_str:
        if d == str(digit):
            counterOccurrence += 1
    
    return counterOccurrence


#Función 18 - sumar los digitos de un numeros entero
def sumOfDigit(number):
    numberStr = str(number)
    sumOfDigits = 0
    for digit in numberStr:
        sumOfDigits += int(digit)
    return sumOfDigits


#-------------------FUNCIONES DE RECURSIVIDAD----------------------------

#Funcion 16 - factorial de un numero
def factorial(n):
    #CASO BASE
    if (n == 0 or n == 1):
        factor = n
    else:
        #CASO RECURSIVO
        factor = n * factorial(n - 1)
    return factor

def fibonacci (n):
    #caso base
    if n == 1:
        fibo = n
    else:
        fibo = n - 1 + fibonacci(n-2)
    return fibo

#------------------FUNCIONES TRABAJO EN CLASE - VARIABLES DIMENSIONADAS ------------------------
def add_passenger(passengers):
    name = input("Nombre del pasajero: ")
    dni = int(input("DNI del pasajero: "))
    destination = input("Destino del pasajero: ")
    passengers.append((name, dni, destination))
    print("Pasajero agregado")

def add_city(cities):
    city = input("Nombre de la ciudad: ")
    country = input("Nombre del país: ")
    cities.append((city, country))
    print("Ciudad agregada")

def city_by_dni(passengers, cities):
    dni = int(input("DNI del pasajero: "))
    for name, dni_passenger, destination in passengers:
        if dni_passenger == dni:
            for city, country in cities:
                if destination == city:
                    print(f"{name} está viajando a {city}, {country}.")
                    return
    print("DNI no encontrado.")

def passengers_by_city(passengers, cities):
    city = input("Nombre de la ciudad: ")
    count = 0
    for _, _, destination in passengers:
        if destination == city:
            count += 1
    print(f"La cantidad de personas que está viajando a {city} es {count}.")

def country_by_dni(passengers, cities):
    dni = int(input("DNI del pasajero:  "))
    for j, dni_passenger, destination in passengers:
        if dni_passenger == dni:
            for j, country in cities:
                for city, destination in cities:
                    if destination == city:
                        print(f"El pasajero está viajando a {country}.")
                        return
    print("DNI no encontrado")

def passengers_by_country(passengers, cities):
    country = input("Nombre del país: ")
    count = 0
    for city, c in cities:
        if c == country:
            for _, dni_passenger, destination in passengers:
                if destination == city:
                    count += 1
    print(f"La cantidad de personas que está viajando a {country} es {count}.")
    
#EJERCICIO 2
def get_invoice_addresses(purchases):
    addresses = set()
    for customer, _, _, address in purchases:
        addresses.add(address)
    return list(addresses)

#EJERCICIO 3
def show_number_members(members):
    print(f"La cantidad de socios en el club es {len(members)}.")

def record_fee_payment(member_number, members):
    if member_number in members:
        members[member_number]["dues_up_to_date"] = True
        print(f"El socio {member_number} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"El socio {member_number} no existe.")

def modify_entry_date(members):
    for member_number, data in members.items():
        if data["join_date"] == "13/03/2018":
            data["join_date"] = "14/03/2018"

def unsubscribe(name_surname, members):
    for member_number, data in members.items():
        if data["name"] == name_surname:
            del members[member_number]
            print(f"{name_surname} ha sido dado de baja.")

def print_members_list(members):
    print("Listado de socios:")
    for member_number, data in members.items():
        dues_status = "al día" if data["dues_up_to_date"] else "en deuda"
        print(f"Socio n°{member_number}, {data['name']}, ingresó: {data['join_date']}, cuota {dues_status}.")