#Ejercicio 1
print("Calculadora")
anios_computadora = int(input("Ingrese los que tiene su computadora: "))
if (anios_computadora <= 2) :
    print("Nuevo")
elif (anios_computadora > 2):
    print("Viejo")

#Ejercicio 2
print("Calculadora de edades")
anios_computadora = int(input("Ingrese los que tiene su computadora: "))
if (anios_computadora <= 2 and anios_computadora > 0) :
    print("Nuevo")
elif (anios_computadora > 2):
    print("Viejo")
else:
    print("Error! No se aceptan números negativos")

#Ejercicio 3
print("Buscador de coincidencias")
nombre_uno = input("Ingrese un nombre: ")
nombre_dos = input("Ingrese otro nombre: ")
letra_inicial_uno = nombre_uno[0:1]
letra_inicial_dos = nombre_dos[0:1]
if (letra_inicial_uno == letra_inicial_dos):
    print("Coincidencia, ambos nombres comienzan con la misma letra c:")
else:
    print("No hay coincidencia, los nombres comienzan con letras diferentes :c")

#Ejercicio 4
print("Votaciones")
print("Candidato A - Partido Rojo")
print("Candidato B - Partido Verdad")
print("Candidado C - Partido Azul")
eleccion = input("Ingrese la letra del candidato elegido: ").lower()
if (eleccion == "a"):
    print("Usted ha votado por el Partido Rojo")
elif (eleccion == "b"):
    print("Usted ha votado por el Partido Verdad")
elif(eleccion == "c"):
    print("Usted ha votado por el Partido Azul")
else:
    print("Letra inválida. Intente nuevamente")

#Ejercicio 5
print("¿Será vocal?")
caracter = input("Ingrese una letra para saber si es vocal: ").lower()
es_vocal = caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"
if (len(caracter)> 1):
    print("Error! Debe ingresar un letra")
elif(es_vocal):
    print("Es vocal!")
else:
    print("No es vocal")

#Ejercicio 6
print("¿Será año bisiesto?")
anio = int(input("Ingrese un año para saber si es bisiesto: "))
anio_bisiesto = (anio%4 == 0 and not(anio%100==0)) or (anio%4 == 0 and anio%400 == 0)
if (anio_bisiesto):
    print("Es año bisiesto.")
else:
    print("No es año bisiesto.")

#Ejercicio 7
print("El número menor")
numero_uno = int(input("Ingrese un número: "))
numero_dos = int(input("Ingrese otro número: "))
numero_tres = int(input("Ingrese otro número: "))
if(numero_uno < numero_dos):
    numero_menor = numero_uno
    if(numero_tres < numero_uno):
        numero_menor = numero_tres
elif(numero_dos < numero_tres):
    numero_menor = numero_dos
    if (numero_tres < numero_dos):
        numero_menor = numero_tres
else:
    numero_menor = numero_tres
print(f"Numero menos: {numero_menor}")

#Ejercicio 8
print("Camelot - Sign up")
usuario = input("Ingrese su nombre de usuario: ")
contrasenia = input("Ingrese su contraseña: ")
if (contrasenia == "excalibur" and usuario == "Gwenevere"):
    print("Usuario y contraseña correctos, Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#Ejercicio 9
print("¿A qué grupo pertenezco?")
nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese su sexo (Mujer/Hombre): ").lower()
if ((sexo == "mujer" and nombre[0:1] < "m") or (sexo == "hombre" and nombre[0:1] > "n")):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")
    
    
#Ejercicio 10
print("Entrada al patio de juegos")
edad = int(input("Ingrese su edad: "))
if (edad < 4):
    print ("Puede entrar gratis <3")
elif (edad >= 4 and edad <= 18):
    print("Valor de entrada: $500")
elif (edad > 18):
    print("Valor de entrada: $1000")
    
#Ejercicio 11
print("Bienvenido a la pizzería Bella Napoli")

#Declaracion de variables
eleccion = " "
vegetariano = ["pimiento", "tofu"]
no_vegetariano = ["peperoni", "jamon", "salmon"]
ingrediente_valido = False

#Validamos las opciones de pizzas
print("Responda con si o no")
while eleccion != "si" and eleccion != "no":
    eleccion = input("¿Desea una pizza vegetariana? ").lower()

#Si se elige pizza no veggie
if (eleccion == "no"):
    pizza = "No vegetariana"
    #Haciendo uso de un bucle while validamos los ingredientes, aunque se podría usar una función para no repetir código
    while ingrediente_valido == False:
        print("Opciones:")
        print(no_vegetariano)
        ingrediente_elegido = input("Ingrese el numero del ingrediente que prefiere: ").lower()
        if (ingrediente_elegido in no_vegetariano):
            ingrediente_valido = True;
            print("Ingrediente agregado")
        else: 
            print("Ingrediente no valido")
    
#Si se elige pizza veggie
elif eleccion == 'si':
    pizza = "Vegetariana"
    #Haciendo uso de un bucle while validamos los ingredientes, aunque se podría usar una función para no repetir código
    while ingrediente_valido == False:
        print("Opciones veggies")
        print(vegetariano)
        ingrediente_elegido = input("Ingrese el numero del ingrediente que prefiere: ").lower()
        if (ingrediente_elegido in vegetariano):
            ingrediente_valido = True;
            print("Ingrediente agregado")
        else: 
            print("Ingrediente no valido")
else: 
    print('Opcion invalida')

#Presentación de la pizza elegida
print(" ")
print(f"Pizza: {pizza}")
print(f"Ingredientes: tomate, mozzarella, {ingrediente_elegido}")

#Ejercicio 12
print("Calculadora de años")
anio_actual = int(input("Ingrese el año actual: "))
anio_elegido = int(input("Ingrese cualquier año: "))
if (anio_elegido> anio_actual): 
    anios = anio_elegido - anio_actual
    print(f"Faltan {anios} para el {anio_elegido}")
elif (anio_elegido < anio_actual):
    anios = anio_actual - anio_elegido
    print(f"Pasaron {anios} desde el {anio_elegido}")
    
#Ejercicio 13
print("¿Multiplo ó no?")
numero_uno = int(input("Ingrese un número entero: "))
numero_dos = int(input("Ingrese otro número entero: "))
if (numero_uno>0 and numero_dos>0):
    if (numero_uno > numero_dos):
        mayor = numero_uno
        menor = numero_dos 
    else:
        mayor = numero_dos
        menor = numero_uno
    if (mayor%menor==0):
        print(f"{mayor}es múltiplo de {menor}")
    else:
        print(f"{mayor}no es múltiplo de {menor}")
else:
    print('Error! Números inválidos.')
    
#Ejercicio 14
print("Ecuación de primer grado")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
if (a == 0 and b == 0):
    print("La ecuación tiene infinitas soluciones") 
elif (a == 0 and b != 0):
    print("La ecuación no tiene solución")
elif(a != 0):
    x=(-b/a)
    print(f"x ={x}")
    
#Ejercicio 15
import math
math.pi
print("Áreas")
print("¿Desea calcular el área de un círculo o de un triángulo?")
figura = input("Ingrese t para triángulo o c para círculo: ").lower()
if (figura == "c"):
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio**2
    figura = "círculo"
elif (figura == "t"):
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura)/2
    figura = "triángulo"
if (figura == "triángulo" or figura =="círculo"):
    print(f"El área del {figura} es {area} ")
else:
    print("Error! Letra inválida. Intentelo nuevamente")

#Ejercicio 16
print("Calculadora básica")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
print("¿Qué operación desea realizar?")
operacion = int(input("Ingrese 1 para sumar, 2 para multiplicar, 3 para restar o 4 para dividir: "))
if (operacion == 1):
    suma = a + b
    print(f"{a} + {b} = {suma}")
elif (operacion == 2):
    producto = a*b
    print(f"{a} x {b} = {producto}")
elif (operacion == 3):
    resto = a-b
    print(f"{a} - {b} = {resto}")
elif (operacion==4 and b != 0):
    cociente = a / b
    print(f"{a} / {b} = {cociente}")
else: 
    print("Error! Vuelva a intertarlo")
    
    
#Ejercicio 17
print("¿Qué día es hoy?")
dia_actual = input("Ingrese el nombre del día de hoy: ").lower()
if (dia_actual == "lunes"):
    print("Ánimo! Buena semana! :p")
elif (dia_actual == "viernes"):
    print("Felicidades! Llegaste al fin de semana. Hoy no te tienes que bañar")
elif (dia_actual=="sabado" or dia_actual=="sábado" or dia_actual=="domingo"):
    print("Canon canon canon, canon es mi colchól")
else:
    print("Sigue adelante, pronto será año nuevo")
    
#Ejercicio 18
print ("¿Cuánto cobrarás este mes?")
horas_trabajadas = float(input("Ingresa la cantidad de horas trabajadas este mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))
if (horas_trabajadas > 48):
    horas_extras = horas_trabajadas - 48
    print(f"Trabajaste {horas_extras} horas extras!")
    extra_por_hora = (salario_por_hora*0.10) + salario_por_hora
    salario_total = (48 * salario_por_hora) + (extra_por_hora * horas_extras)
    
else: 
    salario_total = horas_trabajadas * salario_por_hora

print(f"Salario total: {salario_total}")

#Ejercicio 19
print("Descuento en lápices")
cantidad_lapices = int(input("Ingrese cuantas unidades lleva: "))
if (cantidad_lapices >= 1000):
    unidad_con_descuento = 60 - (60 * 0.07)
    total = cantidad_lapices * unidad_con_descuento
else:
    total = cantidad_lapices * 60

print(f"Valor total de la compra: ${total}")

#Ejercicio 20
print("¿Aprobado o desaprobado?")
nota_1 = float(input("Ingrese su primer calificación: "))
nota_2 = float(input("Ingrese su segunda calificación: "))
nota_3 = float(input("Ingrese su tercer calificación: "))
nota_4 = float(input("Ingrese su última calificación: "))
promedio = (nota_1 + nota_3 + nota_2 + nota_4) / 4
if (promedio >= 6): 
    print("¡APROBADO!")
else:
    print("¡DESAPROBADO!")
    





    
    

