#Trabajo práctico N° 1 - Parte 2

#Ejercicio 1
print("Área y perímetro de un rectángulo")
print("Ingrese la base del restángulo:")
base_rectangulo = float(input())
print("Ingrese la altura del rectángulo:")
altura_rectangulo = float(input())
perimetro_rectangulo = (base_rectangulo*2)+(altura_rectangulo*2)
area_rectangulo = base_rectangulo * perimetro_rectangulo
print(f"Perimetro:{perimetro_rectangulo}")
print(f"Área: {area_rectangulo}")

#ejercicio 2
print("Calcular la hipotenusa")
print("Ingrese el valor del cateto opuesto:")
cateto_opuesto = float(input())
print("Ingrese el valor del cateto adyacente:")
cateto_adyacente = float(input())
hipotenusa = (cateto_opuesto**2 + cateto_adyacente**2)**(1/2)
print(f"Hipotenusa: {hipotenusa}")

#ejercicio 3
print("Sumar, Restar, Dividir y Multiplicar dos numeros.")
print("Ingrese un número:")
numero_uno = float(input())
print("Ingrese otro número:")
numero_dos = float(input())
print(f"{numero_uno} - {numero_dos} = {numero_uno-numero_dos}")
print(f"{numero_uno} + {numero_dos} = {numero_uno+numero_dos}")
print(f"{numero_uno} x {numero_dos} = {numero_uno*numero_dos}")
print(f"{numero_uno} / {numero_dos} = {numero_uno/numero_dos}")

#ejercicio 4
print("Conversor de Temperatura de F a C")
print("Ingrese los grados Fahrenheit:")
fahrenheit = float(input())
celsius=((fahrenheit-32)*(5/9))
print(f"Celsius: {celsius}")

#ejercicio 5
#¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#Ejercicio a
#A = input(nombre, “¿Cuál es tu canción favorita?”)
#Con la función imput no podemos mostrar una variable, porque espera 1 argumento no dos; y el nombre de la variable a la que le estamos asignando la canción favorita no es muy descriptiva

#ejercicio b
#precio = input(“Precio: “)
#total = precio + (precio * 0.1)
#Antes de realizar operaciones con la variable precio debemos convertirla a un valor de tipo numerico, ya sea int o float; ya que la función input recibe string

#ejercicio c
#edad = int(input(“Edad: “))
#print(tu edad es, edad)
#El problema viene a la hora de imprimir, se intentó usar los f strings pero no está bien escrito. Sería [print(f"tu edad es {edad}")]

#ejercicio d
#edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)
#No estamos comparardo la variable edad con 18, si no reasignandola. Deberia se [==] no [=]


#ejercicio 6
print("Sacar promedio de 3 números")
numero_uno = float(input("Ingrese un número:"))
numero_dos = float(input("Ingrese otro número"))
numero_tres = float(input("Ingrese el último número"))
suma = numero_uno + numero_dos + numero_tres
promedio = suma/3
print(f"Media: {promedio}")

#ejercicio 7
print("Conversor de minutos a horas y minutos")
minutos_entrada = float(input("Ingrese la cantidad de minutos que desea convertir: "))
horas= int(minutos_entrada/60)
minutos_salida = int(minutos_entrada%60)
print(f"{horas} horas y {minutos_salida} minutos")

#ejercicio 8
print("Calculadora de comisiones")
sueldo_base = float(input("Ingrese el sueldo base: "))
comision = (sueldo_base*0.10) 
print(f"Conceptos de comisión por las 3 ventas del mes {comision*3}")
sueldo_total = sueldo_base + comision*3
print(f"Sueldo total(con comisión): {sueldo_total}")

#ejercicio 9
print("Calculadora de descuentos")
compra = float(input("Ingrese valor de la compra:"))
descuento = 0.15
compra_con_descuento = compra - (compra*descuento) 
print(f"Total a pagar: $ {compra_con_descuento}")

#ejercicio 10
print("¿Habré aprobado Algoritmos?")
#parciales
primer_parcial = float(input("Ingrese la calificación del primer parcial: "))
segundo_parcial = float(input("Ingrese la calificación del segundo parcial: "))
tercer_parcial = float(input("Ingrese la calificación del tercer parcial: "))
promedio_parciales = (primer_parcial + segundo_parcial + tercer_parcial) / 3
#examen final
examen_final = float(input("Ingrese la nota del exámen final: "))
#trabajo final
trabajo_final = float(input("Ingrese la nota del trabajo final: "))
#calificación
calificacion = (promedio_parciales*0.55) + (examen_final*0.30) + (trabajo_final*0.15)
print(f"Calificación de Algoritmos: {calificacion}")


#ejercicio 11
print("Distancia entre dos números")
numero_uno = float(input("Ingrese un número:"))
numero_dos = float(input("Ingrese otro número:"))
distancia = abs(numero_uno-numero_dos)

#ejercicio 12
print("Raíz cuadrada y cúbica de número")
numero = float(input("Ingrese un número:"))
raiz_cuadrada = numero**(1/2)
raiz_cubica = numero**(1/3)
print(f"Raíz cuadrada: {raiz_cuadrada}")
print(f"Raíz cúbica: {raiz_cubica}")

#ejercicio 13
print("Números invertidos")
numero = input("Ingrese un número:")
parte_delantera = numero[1:]
parte_trasera = numero[0:1]
print(f"Número invertido: {parte_delantera + parte_trasera}")

#ejercicio 14
print("Invertidor de variables")
A = float(input("Ingrese el valor de A:"))
B = float(input("Ingrese el valor de B:"))
C = A
A = B
B = C
print(f"A = {A}")
print(f"B = {B}")

#ejercicio 15
print("Calculadora de distancias en segundos")
hh = int(input("Ingrese la hora de partida:"))
mm = int(input("Ingrese los minutos de partida: "))
ss = int(input("Ingrese los segundos de partida:"))
t = int(input("Ingrese los segundos que tarde hasta el punto B:"))
segundos_llegada = hh*3600 + mm*60 + ss + t
hh_llegada = segundos_llegada/3600
mm_llegada = (segundos_llegada%3600)/60
ss_llegada = segundos_llegada%60
print(f"Hora de llegada: {hh_llegada}:{mm_llegada}:{ss_llegada}")

#ejercicio 16
print("Iniciales de un nombre completo")
nombre = input("Ingrese un nombre:")
apellido_uno = input("Ingrese un primer apellido:")
apellido_dos = input("Ingrese un segundo apellido:")
print(f"Iniciales del nombre completo: {nombre[0:1]}. {apellido_uno[0:1]}. {apellido_dos[0:1]}.")

#ejercicio 17
print("Registro en la Matrix")
nombre = input("Ingrese su nombre:")
print(f"Ahora estás en la matrix,{nombre}")

#ejercicio 18
print("Impuestos de una cena")
precio_cena = input("Ingresa lo que costó la cena: ")
concepto_de_servicio = 0.062
propina = 0.10
monto_final = precio_cena + (precio_cena*concepto_de_servicio) + (precio_cena*propina)
print(f"Monto total: ${monto_final}")

#ejercicio 19
print("Formateando fecha")
dia_nacimiento = int(input("Ingrese su día de nacimiento: "))
mes_nacimiento = int(input("Ingrese el número del mes de nacimiento: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
print(f"Fecha de nacimiento: {dia_nacimiento}/{mes_nacimiento}/{anio_nacimiento}")

#ejercicio 20
print("Formateando fecha - V-2")
dia_nacimiento = input("Ingrese su día de nacimiento: ")
mes_nacimiento = input("Ingrese el número del mes de nacimiento: ")
anio_nacimiento = input("Ingrese el año de nacimiento: ")
fecha_nacimiento = dia_nacimiento + mes_nacimiento + anio_nacimiento
print(f"Fecha de nacimiento: {fecha_nacimiento}")

#ejercicio 21
print("Calculadora de combustible")
km_x_litro = float(input("Ingrese cuantos kilometro puede recorrer su moto con 1 litro de combustible: "))
capacidad_tanque = float(input("Ingrese la capacidad de litros del tanque de su moto: "))
km_x_recorrer = float(input("Ingrese la cantidad de km que desea recorrer: "))
combustible_necesario = km_x_recorrer * 1 / km_x_litro
cantidad_tanques = combustible_necesario /capacidad_tanque
print(f"Cantidad de tanques necesarios: {cantidad_tanques}")