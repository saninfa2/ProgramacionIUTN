import random
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
        
#FUNCION BASE PARA MOSTRAR UNA LISTA DE FORMA BONITA
def showList(list):
    for elemento in range(len(list)):
        if elemento < (len(list)-1):
            print(list[elemento], end=", ")
        else: 
            print(list[elemento])  
 
#--------------------------------TRABAJO PRACTICO N6-----------------------------------------
#Funcion que pide números hasta que se ingrese cero, guardando solo los números distintos a cero
def setlistNumber():
    number = 1
    listNumbers = []
    while number != 0:
        number = int(input("Ingrese un número para agregar a la lista o 0 para salir:"))
        if number!= 0:
            listNumbers.append(number)
    return listNumbers

#Funcion que busca un número y elimina su primera aparición en una lista
def search_number_and_delete(list, number):    
    if not(number in list):
        print("El número no aparece en la lista")
    else: 
        list.remove(number)
    return list

def sum_of_numberslist(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def create_list_small_than(list, number):
    new_list = []
    j = 0
    for i in range(len(list)):
        if list[i] < number:
            new_list.append(list[i]) 
            j+=1
    return new_list

def counter_number_repeat_number(list):
    list_result =[]
    tuple = ()
    ocurrence = []
    count = 0
    #por cada indice de list este for da una vuelta
    for i in list:
        count
        if i in ocurrence:
            count +=1
        else: 
            ocurrence.append(i)
    tuple = (list[i], count)
    list_result.append(tuple)    
    return list_result

#Ejercicio 6
#Función que permite ingresar datos a una lista hasta que se ingresa x
def input_string_before_x():
    list_sentence = []
    while True:
        sentence = input("Ingrese el valor: ").capitalize()
        if sentence == 'X':
            break
        list_sentence.append(sentence)
    return list_sentence


#Función que apartir de dos listas crea un conjunto y lo muestra
def inform_whitout_repeat(list1, list2):
    #Utilizar conjuntos nos asegura que no hay elementos repetidos
    total_list = set(list1 + list2)
    for element in total_list:
        print(element)
    
#Utilizamos la interseccion de conjuntos para mostrar los elementos que comparten en ambas listas dadas
def inform_repeat_element(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)
    list_of_repeat_elements = set_list1 & set_list2
    for element in list_of_repeat_elements:
        print(element)
        
#Utilizando el mismo principio en la función anterior, utilizamos la interseccion de conjuntos 
#para mostras aquellos valores que estan en la primera lista dada pero no en la segunda
def inform_element_whitout_repeat_list1(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)
    list_of_repeat_elements = set_list1 - (set_list1 & set_list2)
    for element in list_of_repeat_elements:
        print(element)
        
#Ejercicio 9 - tablero memorytest
def create_table(row, columns):
    number = list(range(1, (row * columns) // 2 + 1)) * 2
    random.shuffle(number)
    table = [[0] * columns for _ in range(row)]

    for i in range(row):
        for j in range(columns):
            table[i][j] = number.pop()

    return table

def print_table(table, guessed_cart):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if (i, j) in guessed_cart:
                print(f"{table[i][j]:2}", end="  ")
            else:
                print("X ", end="  ")
        print()

def main():
    rows = 4
    columns = 4
    guessed_cart = set()
    table = create_table(rows, columns)
    
    trieds = 0
    
    while len(guessed_cart) < rows * columns:
        print_table(table, guessed_cart)
        trieds += 1
        
        row1 = int(input("Elige una fila para la primera carta: "))
        row1 -= 1
        column1 = int(input("Elige una columna para la primera carta: "))
        column1 -= 1
        
        if (row1, column1) in guessed_cart:
            print("Esa carta ya la adivinaste. Elige otra.")
            continue
        
        print_table(table, guessed_cart)
        
        row2 = int(input("Elige una fila para la segunda carta: ") )
        row2 -= 1
        column2 = int(input("Elige una columna para la segunda carta: "))
        column2 -= 1
        
        if (row2, column2) in guessed_cart:
            print("Esa carta ya la adivinaste. Elige otra.")
            continue
        
        if table[row1][column1] == table[row2][column2]:
            print("¡Encontraste una pareja!")
            guessed_cart.add((row1, column1))
            guessed_cart.add((row2, column2))
        else:
            print("¡Las cartas no coinciden!")

    print("¡Has encontrado todas las parejas en", trieds, "intentos!")
    
#Ejercicio 10
def get_diagonals(matriz):
    n = len(matriz)
    
    main_diagonal = [matriz[i][i] for i in range(n)]
    invert_diagonal = [matriz[i][n - 1 - i] for i in range(n)]
    
    return main_diagonal, invert_diagonal
