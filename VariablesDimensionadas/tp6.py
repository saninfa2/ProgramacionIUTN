import funcionesCopy

#Ejercicio 1
print("Creando una lista de números:")
list_of_number_int = funcionesCopy.setlistNumber()
print("Lista: ")
funcionesCopy.showList(list_of_number_int)


#Ejercicio 2
#A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
#eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
print("Buscando un número")
print("El número ingresado será buscado en la lista y se eliminará su primer ocurrencia")
number_for_delete = int(input("Ingrese un número:  "))
list_whit_number_delete = funcionesCopy.search_number_and_delete(list_of_number_int, number_for_delete)
print("Lista original:")
funcionesCopy.showList(list_of_number_int)
print("Lista actual:")
funcionesCopy.showList(list_whit_number_delete)


#Ejercicio 3
#Imprimir la sumatoria de todos los números de la lista
print("Sumatoria de todos los números de una lista")
result = funcionesCopy.sum_of_numberslist(list_of_number_int)
print(f"Resultado: {result}")

#Ejercicio 4
#Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
#que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
print("Buscando otro número")
print("El número ingresado será buscado en la lista y se creará otra con los números menores a este")
biggerNumber = int(input("Ingrese un número:  "))
smaller_of_number_list = funcionesCopy.create_list_small_than(list_of_number_int, biggerNumber)
print("Lista original:")
funcionesCopy.showList(list_of_number_int)
print("Lista actual:")
funcionesCopy.showList(smaller_of_number_list)

#Ejercicio 5
#Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta 
#por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, 
#si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]
print("¿Cuántas veces aparecerá cada número?")
list_of_tuple = funcionesCopy.counter_number_repeat_number(list_of_number_int)
funcionesCopy.showList(list_of_tuple)
print(list_of_tuple)

#Ejercicio 6    
print("Nombres de pila")
#Se piden los nombres de primaria
print("Ingresa los nombres de pila de los alumnos de primaria:")
print("Ingresa x para salir")
primary_students_list = funcionesCopy.input_string_before_x()

#Luego los de secundaria
print("Ingresa los nombres de pila de los alumnos de secundaria:")
print("Ingresa x para salir")
secondary_students_list = funcionesCopy.input_string_before_x()

#Se muestran los nombres isn repeticiones
print("Todos los nombres sin repeticiones:")
funcionesCopy.inform_whitout_repeat(primary_students_list, secondary_students_list)

#Se muestran los nombres sin repeticiones
print("Nombres que se repiten en el nivel primario y secundario:")
funcionesCopy.inform_repeat_element(primary_students_list, secondary_students_list)

#Se muestran los nombres de alumnos del primario que no se repiten en el secundario
print("Nombres del nivel primario que no se repiten en el nivel secundario: ")
funcionesCopy.inform_element_whitout_repeat_list1(primary_students_list, secondary_students_list)

  
#Ejericicio 7

#Inicialización de variables
#diccionario para guardar las ocurrencias
dic_ocurrence = {}
counter = 0

#Mientras el contador sea menor a 50 se pediran string, a la vez que se repasan
#y contabilizan sus caracteres
while counter < 50:
    string = input("Ingrese un string: ")
    for caracter in string:
        if caracter in dic_ocurrence:
            dic_ocurrence[caracter] += 1
        else:
            dic_ocurrence[caracter] = 1
    counter += 1

#Mostramos por pantalla las ocurrencias de cada caracter
print("Cantidad total de ocurrencias de cada carácter:")
for caracter, amount in dic_ocurrence.items():
    print(f"'{caracter}': {amount}")

#Ejercicio 8
# Definir el cuadro de goles en un arreglo de dos dimensiones
goals = [
    [0, 2, 1, 3, 4, 0, 1, 2, 3, 0],
    [1, 0, 2, 0, 1, 2, 0, 1, 0, 1],
    [1, 0, 0, 2, 0, 1, 0, 1, 2, 0],
    [0, 3, 2, 0, 1, 0, 2, 0, 3, 0],
    [4, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 2, 0, 1, 1],
    [3, 2, 0, 1, 1, 0, 0, 2, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0]
]

# Inicializar listas para almacenar victorias, empates, perdidas, goles marcados y goles recibidos
wins = [0] * 10
equals = [0] * 10
loses = [0] * 10
goals_given = [0] * 10
goals_received = [0] * 10

# Calcular los resultados de los partidos
for i in range(10):
    for j in range(10):
        if i != j:
            goals_team_i = goals[i][j]
            goals_wins_j = goals[j][i]
            if goals_team_i > goals_wins_j:
                wins[i] += 1
            elif goals_team_i < goals_wins_j:
                loses[i] += 1
            else:
                equals[i] += 1
            goals_given[i] += goals_team_i
            goals_received[i] += goals_wins_j

# Calcular los puntos obtenidos por cada equipo (3 puntos por triunfo, 1 punto por empate)
points = [wins[i] * 3 + equals[i] for i in range(10)]

# Mostrar los resultados para cada equipo
for i in range(10):
    print(f"Equipo {i + 1}: victorias: {wins[i]}, empates: {equals[i]}, Derrotas: {loses[i]}")
    print(f"Goles marcados: {goals_given[i]}, Goles recibidos: {goals_received[i]}")
    print(f"Diferencia de Goles: {goals_given[i] - goals_received[i]}, Puntos: {points[i]}\n")

#Ejercicio 9
print("Bienvenido a MemoryTest")
funcionesCopy.main()

#Ejercicio 10
# Ejemplo de uso
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

main_diagonal, invert_diagonal = funcionesCopy.get_diagonals(matriz)

print("Diagonal Principal:", main_diagonal)
print("Diagonal Inversa:", invert_diagonal)


#Ejercicio 11
# Definir el diccionario de divisas
dict_badge = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Pedir al usuario una divisa
badge = input("Ingresa el nombre de una divisa: ").capitalize()

# Comprobar si la divisa está en el diccionario y mostrar el símbolo o un mensaje de aviso
if badge in dict_badge:
    simbol = dict_badge[badge]
    print(f"El símbolo de {badge} es {simbol}")
else:
    print("La divisa no está en el diccionario")


#Ejercicio 12
# Pedir al usuario que ingrese su nombre, edad, dirección y teléfono
name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")
adress = input("Ingresa tu dirección: ")
tel = input("Ingresa tu número de teléfono: ")

# Crear un diccionario con la información ingresada por el usuario
info = {
    "nombre": name,
    "edad": age,
    "dirección": adress,
    "teléfono": tel
}

# Mostrar la información del usuario
mensaje = f"{info['nombre']} tiene {info['edad']} años, vive en {info['dirección']} y su número de teléfono es {info['teléfono']}."
print(mensaje)


#Ejercicio 13
# Crear un diccionario con los precios de las frutas
fruit_price = {
    'manzana': 1.0,
    'banana': 0.5,
    'naranja': 0.75,
    'pera': 1.2,
    'uva': 2.0
}

# Pedir al usuario que ingrese una fruta y la cantidad en kilos
fruit = input("Ingresa una fruta: ").lower()
kilos = float(input("Ingresa la cantidad en kilos: "))

# Verificar si la fruta está en el diccionario y calcular el precio
if fruit in fruit_price:
    total_price = fruit_price[fruit] * kilos
    print(f"El precio de {kilos} kilos de {fruit} es ${total_price:.2f}")
else:
    print("La fruta no está en la lista de precios.")


