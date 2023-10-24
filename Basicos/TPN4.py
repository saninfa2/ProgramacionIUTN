#TRABAJO PRÁCTICO N° 4: CONTINUE Y BREAK
#Ejercicio 1
#1. Cree un bucle while con las siguientes características:
#El valor inicial de la variable x será 0.
#El valor del incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución debe interrumpirse cuando x es igual a 15.
# Debes imprimir la siguiente frase cada vez que se ejecuta el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con el valor de x en 4, 6 y 10.
# En cada salto de ejecución, debe mostrar los valores saltados con este mensaje: 'El valor ' + x ' de x fue omitido'.
# Cuando se interrumpe la ejecución del bucle se debe mostrar un mensaje indicándolo: 'La ejecución del bucle se interrumpe cuando x era' + x.

print("Cuenta progresiva")
x=0
while x <=30:
    x+=1
    if (x ==4) or (x ==6) or (x ==10):
        print(f"El valor {x} de x fue omitido")
        continue
    elif (x==15):
        print(f'La ejecución del bucle se interrumpe cuando x era {x}')
        break
    else:
        print(f"El valor del bucle es {x}")
       
        
#Ejercicio 2
#Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
#Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
print("Lineas en mayusculas")
line = False
while line == False:
    phrase = input("Ingrese una frase para continuar y espacio en blanco para salir: ").upper()
    print(" ")
    if phrase == "":
        line==True
        break
    else:
        print(phrase)
      
        
#Ejercicio 3
#Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
#La bitácora de operaciones tiene la siguiente forma:
#D 100
#R 50
print("Simulacion bancaria")
option = " "
money=0
while option != "":
    option= input("Ingrese D para depositar o R para retirar, seguido de su monto deseado comience con un deposito, al colocar una linea en blanco, el programa se cerrara :").upper()
    if option[0:1] == "D":
        count = int(option[2::])
        money += count
        continue
    elif option[0:1] == "R":
        count = int(option[2::])
        money -= count
        continue
    else:
        break
print(money,"$")


#Ejercicio 4
#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados. 
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
print("Total de numeros primos")
prime_counter = 0
while True:
    number = int(input("Ingrese un número (0 para salir): "))
    if number == 0:
        break
    if number <= 1:
        continue
    prime= True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        prime_counter += 1
print(f"La cantidad de números primos ingresados es de : {prime_counter}")


#Ejercicio 5
#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
print("Años biciestos entre años elegidos")
start = int(input("Ingrese el año de inicio: "))
end = int(input("Ingrese el año de fin: "))
for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            print(year)
        else:
            continue
    else:
        continue


#Ejercicio 6
#Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración 
#continue para omitir los números impares.
print("Numeros pares del 1 al 20")
for number in range(1, 21):
    if number % 2 != 0:
        continue 
    print(number)
    
    
#Ejercicio 7
#Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
#Cuando encuentres el número, usa break para salir del bucle.
print("Buscador de numeros")
listOfNumber = [1,2, 3, 4, 5, 6, 7, 8]
number = int(input("Ingrese un numero del 1 al 8: "))
for n in listOfNumber:
    if n == number:
        print("Número encontrado!")
        break


#Ejercicio 8
#Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
# Utiliza un bucle while para permitir al usuario seleccionar una opción. 
# Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
print("TRES FRASES")
option=4
while option >0:
    option=int(input("Ingrese 1,2 o 3 para mostrar una frase. si ingresa 0 saldrá del programa "))
    if option == 0:
        break
    elif option == 1:
        print("Hello moto")
    elif option == 2:
        print("Hi5")
    elif option == 3:
        print("Bye bye")