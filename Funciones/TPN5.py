import funciones;
#--------------------------------------------------PROGRAMA PRINCIPAL------------------------------------------

#-----------------------------------Implimentación de función 1 - Ejercicio 1----------------------------------
print("Verificador de DNI")
dni = int(input("Ingrese su número de DNI: "))
es_valido = funciones.verificarDNI(dni)
if (es_valido):
    print(f"El DNI {dni} es correcto")
else:
    print(f"El DNI {dni} no es correcto")


#-------------------------------Implementación de funcion 2 - Ejercicio 2--------------------------------------
print("Longitud de la última palabra")
phrase = input("Ingrese una frase: ")
print(f"Letras de la última palabra: {funciones.medirUltimaPalabra(phrase)}")

#-------------------------------Implimentación de función 1 y 3 - Ejercicio 3----------------------------------
print("Registro de socios")

#Pedimos el nombre completo
nameComplete = input("Ingrese el nombre completo: ")

#Solamente el primer apellido
lastName = input("Ingrese solo un apellido: ")

#pedimos el DNI hasta que sea validado con la funcion del ejercicio 1
dni = input("Ingrese el DNI: ")
while funciones.verificarDNI(dni):
    dni = input("Ingrese el DNI: ")

#Imprimimos el resultado
print(f"ID: {funciones.definirIdentificador(nameComplete, lastName, dni)}")


#----------------------------------Implimentación de función  - Ejercicio 4-----------------------------------
print("¿Multiplo?")
#Pedimos los numeros enteros
number1 = int(input("Ingrese un número entero: "))
number2 = int(input("Ingrese otro número entero: "))

#Derivamos el retorno de la función a una variable
es_multiplo = funciones.verificarMultiplo(number1, number2)

#Mostramos una salida de acuerdo al retorno
if (es_multiplo):
    print ("El primer número es multiplo del segundo")
else:
    print("El primer número no es multuplo del segundo ")


#----------------------------------Implimentación de función 4 - Ejercicio 5----------------------------------
print("Mediar temperatura")

#Le pedimos al usuario la cantidad de días a promediar
days = int(input("Ingrese la cantidad de días que desea promediar: "))

#Inicialización de contador
day = 1

#Por cada dia de los días ingresados por el usuario pedimos las temperaturas
#y sacamos el promedio con la función
for day in range(days):
    print(f"Día {day}")
    maximumTemperature = int(input("Ingrese la temperatura máxima: "))
    minimumTemperature = int(input("Ingrese la temperatura mínima: "))
    print(f"Temperatura media: {funciones.mediarTemperatura(maximumTemperature, minimumTemperature)}")


#----------------------------------Implimentación de función 6 - Ejercicio 6----------------------------------
print("Más espacio")

#Pedimos el ingreso de una cadena de texto
text = input("Ingrese un texto: ")
print(f"Texto modificado: {funciones.agregarEspaciado(text)}")

#----------------------------------Implimentación de función 7 - Ejercicio 7----------------------------------
print("Número menor y número mayor")

#Inicializamos variables
i = 0
listNumber = []

#Pedimos el ingreso de los números
while i <= 4:
    listNumber.append(int(input("Ingrese un número entero: ")))
    i+=1

#Llamamos a la función y retornamos el resultado a una nueva lista
listOutput = funciones.encontrarMayorMenorLista(listNumber)

#Mostramos el resultado por pantalla
print(f"Número menor: {listOutput[0]}")
print(f"Número mayor: {listOutput[1]}")


#----------------------------------Implimentación de función 8 - Ejercicio 8----------------------------------
print("Área y perímetro de una circunferencia")

#Pedimos el radio de la circunferencia
radius = float(input("Ingrese el radio de la circunferencia: "))

#Recepcionamos los resultados de la función
listOfResult = funciones.calcularAreaYPerimetroCircunferencia(radius)

#Mostramos el resultado por pantalla
print(f"Área: {round(listOfResult[0], 2)}")
print(f"Perímetro: {round(listOfResult[1], 2)}")

#----------------------------------Implimentación de función 9 - Ejercicio 9----------------------------------
print("Simulador de login")

#Inicializacion de intentos
tried = 0

#Mientras queden intentos se piden usuario y contraseña
while tried<=2:
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    #Llamamos a la función y retornamos su resultado
    listReturn = funciones.login(user,password, tried)
    access = listReturn[0]
    tried = listReturn[1]
    #Si la funcion devuelve True le da la bienvenida al usuario
    if access:
        print ("Bienvenido " + user + "!")
        break
    #Si retorna falso se le informa al usaurio que tiene un intento menos
    else:
        print (f"Contraseña o usuario incorrecto. {tried}/3 intentos fallidos.")
  
#----------------------------------Implimentación de función 10 - Ejercicio 10----------------------------------
#Primero creamos el diccionario de productos
cart = {
    "apple": 2.0,
    "banana": 1.0,
    "chocolate": 5.0,
}

#Luego el de descuentos
discounts = {
    "apple": 10,
    "chocolate": 15,
}

#Llamamos a la función pasandole los diccionarios
final_price = funciones.apply_discount(cart, discounts)

#Mostramos el resultado por pantalla
print(f"Total: ${final_price}")


#----------------------------------Implimentación de función 11 y 12 - Ejercicio 11----------------------------------
list_whatever = [1,2,3,4,5]
result = funciones.applyOtherFucntion(funciones.square, list_whatever)
funciones.showList(result)

#----------------------------------Implimentación de función  13 - Ejercicio 12----------------------------------
# Example usage:
phrase = "Esto es una frase de ejemplo"
result = funciones.wordsLengthsInPhrase(phrase)
word = result.keys()
lengthWord = result.values()
for word, lengthWord in result.items():
    print(word,":",lengthWord)


#----------------------------------Implementacion de la funcion 14 - Ejercicio 13------------------------------------
#Ejemplo usando un vector 2D, también serviría para un vector 3D
vector_2d = (3, 4)
#Llamamos a la función
modulus_2d = funciones.vector_modulus(vector_2d)
#Mostramos el resultado por pantalla
print("Modulus of 2D vector:", modulus_2d)


#----------------------------------Implementacion de la funcion  - Ejercicio 14------------------------------------
print("¿Será un número primo?")
number = int(input("Ingrese un número para saber si es primo: "))
result = funciones.numberPrime(number)
if result:
    print(f"{number} es un número primo")
else:
    print(f"{number} no es un número primo") 
    
   
#----------------------------------Implementacion de la funcion 16 - Ejercicio 15------------------------------------
print("Factorial de un número")
#Inicializamos las variables globales
number = 1
counterNumber = 0

#Mientras el número sea distinto de cero se buscará el factorial
#Tomamos el cero como salida porque el factorial de cero es 1
while number != 0:
    number = int(input("Ingrese un número paca sacar su factorial y 0 para salir: "))
    factorialResult = funciones.factorial(number)
    print(f"{number}! = {factorialResult}")
    if number !=0:
        counterNumber+= 1
        
#Mostramos por pantalla la cantidad de números ingresados
if counterNumber != 0:
    print(f"Cantidad de números ingresados: {counterNumber}")
else:
    print("No se ingresó ningún número")


#----------------------------------Implementacion de la funcion 17 - Ejercicio 16------------------------------------
print("Frecuencia de un número")

#Pedimos al usuario el número y digito, convientiendolos en enteros
number = int(input("Introduce un número entero: "))
digit = int(input("Introduce un dígito: "))

#Llamamos a la función pasandole como parámetros los números pedidios anteriormente
occurrence = funciones.countOccurrence(number, digit)

#Mostramos el resultado por pantalla
if occurrence != 0:
    print(f"El dígito {digit} aparece {occurrence} veces en el número {number}.")
else:
    print(f"El dígito no es frecuente en el número")
 
 
#----------------------------------Implementacion de la funcion  18 y otras- Ejercicio 17------------------------------------
print("Ejercicio mix")

#Inicializamos variables globales
number = 5
biggerNumber = 0

#mientras el numero sea primo
while funciones.numberPrime(number) != False:
    #Se pide el ingreso de numeros
    number = int(input("Ingrese un número primo o un número que no sea primo para salir: "))
    #Si es primo
    if funciones.numberPrime(number):
        #se saca la suma de los digitos y se muestra por pantalla
        sumOfDigitsOfPrimeNumber = funciones.sumOfDigit(number)
        print(f"Suma de digitos:{sumOfDigitsOfPrimeNumber}")
        #Se pide un digito y se busca la frecuencia del mismo dentro del numero anterior y se muestra por pantalla
        digitToSeach = int(input("Ingrese un digito para buscalo dentro del número ingresado: "))
        frecuency = funciones.countOccurrence(number, digitToSeach)
        if frecuency != 0:
            print(f"El dígito {digitToSeach} aparece {frecuency} veces en el número {number}.")
        else:
            print(f"El dígito no es frecuente en el número")
        
        #Buscamos el numero más grande
        if (number > biggerNumber):
            biggerNumber = number
    else: 
        #Justificamos la salida del bucle
        print("El número ingresado no es primo")
        
#Mostramos por pantalla el factorial del mayor número ingresado
factorialOfBiggerNumber = funciones.factorial(biggerNumber)
print("Factorial del mayor número ingresado:")
print(f"{biggerNumber}! = {factorialOfBiggerNumber}")
    
    


