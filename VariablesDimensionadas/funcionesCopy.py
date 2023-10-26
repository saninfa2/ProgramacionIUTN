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