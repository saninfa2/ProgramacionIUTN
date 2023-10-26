import funcionesCopy
#--------------------------VARIABLES DIMENSIONADAS---------------------------------
#-------------------------------EJERCICIO 1---------------------------------------
passengers = []
cities = []
option_valid = False

while option_valid != True:
    print("\nMenu: 1. Agregar pasajero  2. Agregar ciudad  3. Buscar ciudad por DNI  ")
    print("4. Buscar cuántos pasajeros por ciudad  5. Buscar país por DNI")
    print("6. Buscar cuántos pasajeros por país  7. Salir")

    choice = input("Seleciona una opción: ")

    if choice == "1":
        funcionesCopy.add_passenger(passengers)
        option_valid = True
    elif choice == "2":
        funcionesCopy.add_city(cities)
        option_valid = True
    elif choice == "3":
        funcionesCopy.city_by_dni(passengers, cities)
        option_valid = True
    elif choice == "4":
        funcionesCopy.passengers_by_city(passengers, cities)
        option_valid = True
    elif choice == "5":
        funcionesCopy.country_by_dni(passengers, cities)
        option_valid = True
    elif choice == "6":
        funcionesCopy.passengers_by_country(passengers, cities)
        option_valid = True
    elif choice == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción invalida. Por favor selecciona una opciona valida")
        option_valid = False

#------------------------------- EJERCICIO 2 ---------------------------------------
# Ejemplo de lista de compras
compras = [
    ('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'),
    ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
    ('Nuria Costa', 12, 567.8, 'Calle 1 - 456'),
    ('Luis Martinez', 15, 987.0, 'Calle 3 - 123')
]

domicilios_factura = funcionesCopy.get_invoice_addresses(compras)
print("Domicilios a los que se debe enviar una factura:")
for domicilio in domicilios_factura:
    print(domicilio)

#-------------------------------- EJERCICIO 3 -------------------------------------------
# Datos iniciales
members = {
    1: {"name": "Amanda Núñez", "join_date": "17/03/2009", "dues_up_to_date": True},
    2: {"name": "Bárbara Molina", "join_date": "17/03/2009", "dues_up_to_date": True},
    3: {"name": "Lautaro Campos", "join_date": "17/03/2009", "dues_up_to_date": True}
}

option_valid = False

while option_valid != True:
    print("\nMenú:  1. Informar cantidad de socios  2. Registrar pago de cuotas  3. Modificar fecha de ingreso")
    print("4. Dar de baja a un socio  5. Imprimir listado de socios  6. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        funcionesCopy.show_number_members(members)
        option_valid = True
    elif option == "2":
        member_number = int(input("Ingrese el número de socio que ha pagado todas las cuotas: "))
        funcionesCopy.record_fee_payment(member_number, members)
        option_valid = True
    elif option == "3":
        funcionesCopy.modify_entry_date(members)
        option_valid = True
        print("Fechas de ingreso modificadas.")
    elif option == "4":
        name_surname = input("Ingrese el nombre y apellido del socio a dar de baja: ")
        funcionesCopy.unsubscribe(name_surname, members)
        option_valid = True
    elif option == "5":
        funcionesCopy.print_members_list(members)
        option_valid = True
    elif option == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        option_valid = False
