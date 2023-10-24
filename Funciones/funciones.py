#FUNCIONES PARA REUTILIZAR
import math;
#--------------------------------FUNCIONES----------------------------------------
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
    
    
#Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios
#y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.
#Función 10 - aplicar descuentos a un diccionario de precios
def aplicarDescuento(diccionario):
    precioConDescuento = 0
    for i in diccionario:
        #Sacamos el precio total con descuento
        descuento = diccionario[i] * diccionario[(i+1)]
        precioConDescuento = diccionario[i] + descuento
        
        #Lo agregamos al final del diccionario
        diccionario["descuento{i}"] = precioConDescuento;
        
#Solicitar números al usuario hasta que ingrese cero. Por cada uno mostrar la suma de sus digitos
def add_digits (number):
    add = 0
    while number != 0:
        digit = number%10
        add += digit
        number //=10
    return add

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