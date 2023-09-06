#TRABAJO PRÁCTICO N°3 - PROGRAMACIÓN I

# #Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
print("Mostrar 10 veces")
word = input("Ingrese una palabra y será mostrada diez veces ")
i=0
while i < 10 :
    i=i+1
    print(word)

print("______________________________________________________________________")

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age=int(input("Ingrese su edad, para hacer una linea del tiempo"))
i=1
while i <= age :
    print(i)
    i=i+1

print("______________________________________________________________________")

#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
# desde 1 hasta ese número separados por comas.
print("Números impares hasta...")
number = int(input("Ingrese un número: "))
i = 1
while i <= number:
    if (i%2==1):
        print(i, end=",")
    i += 1
    
print("______________________________________________________________________")

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese 
#número hasta cero separados por comas.
print("Cuenta regresiva")
number = int(input("Ingrese un número: "))
i = 1
while i <= number:
    number=number-1
    print(number, end=",")

print("______________________________________________________________________")

#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla 
# el capital obtenido en la inversión cada año que dura la inversión.
print("Calculadora de inversión")
investment = float(input("Ingrese la cantidad de dinero que desea invertir:"))
annual_interest = float(input("Ingrese el interés anual:"))
number_of_years = int(input("ingrese la cantidad de años"))
for i in range(number_of_years):
    investment += (investment * annual_interest)/100
    print(f"La ganancia del año {i+1} es: {investment} ")

print("______________________________________________________________________")

#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
#de altura el número introducido.
#*
#**
#***
#****
print("Triángulo de asteriscos")
heigth = int(input("Ingrese la altura del triángulo:"))
#para cada linea repetir 1 de altura
asterisco=""
for i in range(heigth):
    asterisc = asterisc + "*"
    print(asterisc)

print("______________________________________________________________________")

#Ejercicio 7
#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10
print("Tablas de multiplicar")
for i in range(1,11):
    for f in range(1,11):
        print(f"{i} x {f} = {i*f}")

print("______________________________________________________________________")

#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#21
#321
#4321
print("Triángulo de números")
number = input("Ingrese un número entero: ")
number_ = ""
for i in range(len(number)):
    number_ =  number[i] + number_
    print(number_)

print("______________________________________________________________________")

#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
#hasta que introduzca la contraseña correcta.
print("Validación de contraseña")
password = "uwu"
validator= ""
while validator != password:
    validator = input("Ingrese la contraseña:")

print("______________________________________________________________________")

#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
print("¿Primo o no primo?")
prime = 0
number = int(input("Ingrese un número: "))
for n in range (2, number-1):
    if number%n==0:
        prime += 1
if (prime > 0):
    print("No es primo")
else:

    print("Es primo")

print("______________________________________________________________________")

#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida 
#empezando por la última.
#hola
#aloh
print("Invertir palabra")
word = input("Ingrese una palabra: ")
for i in reversed(word):
    print(i)

print("______________________________________________________________________")

#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece 
#la letra emn la frase.
print("Buscador de caracteres")
phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
count = 0
for i in phrase:
    if (i == letter):
        count += 1

if (count > 0):
    print(f"Se encontró la letra {count} veces")
else:
    print("No se encontró la letra")

print("______________________________________________________________________")

#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
print("Introduzca una palabra y salir para salir")
exit_ = "salir"
validator= ""
while validator != exit_:
    print(validator)
    validator = input("")

print("______________________________________________________________________")

#Ejercicio 14
#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
print("Pares o impares entre dos numeros")
num_a = int(input("Ingrese el primer número: "))
num_b = int(input("Ingrese el segundo número: "))
for i in range (num_a, num_b):
    if i%2==0:
        print(f"{i}, es par")
    else:
        print(f"{i}, es impar")

print("______________________________________________________________________")

#Ejercicio 15
#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
print("Los divisores de un número")
num= int(input("Ingrese un numero para mostrar sus divisores"))
for i in range(1,num+1):
    if num%i==0:
        print(i ," es divisor de ", num)
        
print("______________________________________________________________________")

#Ejercicio 16
#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
print("Contador de números negativos")
count= int(input("Ingrese la cantidad de numeros a contar:"))
amountNegative = 0
for i in range(count):
    number= int(input("Ingrese un numero:"))
    if 0>number:
        amountNegative +=1
print(amountNegative, "de los numeros que ingresó son negativos")

print("______________________________________________________________________")

#Ejercicio 17
#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).
phrase = input("Ingrese una frase: ")
vowels= "aeiou"
listv = " "
for letter in phrase:
    if letter in vowels and not(letter in listv):
        listv = listv + letter
print(f"Se encontró {listv}")

print("______________________________________________________________________")

#Ejercicio 18
#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y,
# a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
print("Fibonacci")
fibSequence = [0, 1]
for i in range(10):
    nextNumber = fibSequence[-2]+fibSequence[-1]
    fibSequence.append(nextNumber)
print(fibSequence)

print("______________________________________________________________________")

#Ejercicio 19
#Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero 
# que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, 
# hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
objetive= int(input("Inserte la cantidad de valor a la qué le gustaría llegar "))
actually= 0
while actually < objetive:
    mount= int(input("Ingrese su ahorro diario "))
    actually= actually + mount
    print(f"actualmente su billetera cuenta con {actually}$")

print("______________________________________________________________________")

#Ejercicio 20
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números 
# ingresados.
number = 1
total=0
while number > 0 or number <0:
    number=int(input("Ingrese un numero, si ingresa 0 la lista se cortara, si ingresa otro valor se sumara a los anteriormente ingresados"))
    total= total + number
print("La suma de sus numeros es igual a ", total)

print("______________________________________________________________________")   

#Ejercicio 21
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
print("El mayor de los números ingresados")
close = 1
the_oldest = 0
while close != 0:
    number = int(input("Ingrese un número entero y cero para salir: "))
    if (number > the_oldest):
        the_oldest = number
    elif(number == 0):
        close = 0
print(f"Número mayor: {the_oldest}")

print("______________________________________________________________________")

#Ejercicio 22
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo 
# componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el 
# usuario fueron números pares.
odd=0
while True:
    number=input("Ingrese un numero, si este es -1 saldrá del comando ")
    if number =="-1":
        break
    else:
        count=0
        for i in number:
            i=int(i)
            count+=i
        print("La suma de ambos numeros es ", count)
        if int(number)%2==0:
            odd+=1
print("La cantidad de numeros impares es ", odd)

print("______________________________________________________________________")

#Ejercicio 23
#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos 
# que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
print("Compras del cliente X")
close = 1
sale = 0
acount = []
while close != 0:
    sale = float(input("Ingrese el monto de la compra o cero para salir "))
    if (sale > 0):
        acount.append(sale)
    elif(sale == 0):
        close = 0
print(f"Compras: {acount}")

print("______________________________________________________________________")

#Ejercicio 24
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a 
# pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
print("Compras del cliente X")
close = 1
sale = 0
acount = []
total_sale = 0
while close != 0:
    sale = float(input("Ingrese el monto de la compra o cero para salir "))
    if (sale > 0):
        acount.append(sale)
        total_sale += sale
    elif(sale == 0):
        close = 0
print(f"Total: {total_sale}")
if(total_sale > 1000):
    discountPurchase = total_sale - (total_sale * 0.10)
    print(f"Total con descuento: {discountPurchase}")

print("______________________________________________________________________")

#Ejercicio 25
# Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números 
# enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
print("Factorial de un número")
number = int(input("Ingresa un número entero positivo: "))
factorial = 1
if (number <= 0):
    factorial = 1
else:
    while number > 0 :
        factorial = factorial * number 
        number -= 1
print(f"Factorial: {factorial}")