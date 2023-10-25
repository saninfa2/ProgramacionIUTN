import math

#Funciones extraidas del tp5
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
   
    
#Función 6 - Agregar espacios después de cada letra
def agregarEspaciado(cadena):
    resultado = ""
    for letra in cadena:
        resultado += letra + " "
    cadena = resultado
    return cadena

    
#Función 11 - calculadora de cuadrados, funcion primaria de ejercicio 11
def square(x):
    return x*x


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


#Funcion 5 - Sacar la temperatura media con la maxima y minima
def mediarTemperatura(maxima, minima):
    return int(((minima+maxima)/2))

    
