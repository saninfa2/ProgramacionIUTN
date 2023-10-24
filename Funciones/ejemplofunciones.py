#Solicitar números al usuario hasta que ingrese cero. Por cada uno mostrar la suma de sus digitos
def add_digits (number):
    add = 0
    while number != 0:
        digit = number%10
        add += digit
        number //=10
    return add
#Programa principal
number = int(input("Número a procesar: "))
sumatoria = 0
while number != 0:
    suma = add_digits(number)
    print(f"Suma:{add_digits(number)}")
    number = int(input("Número a procesar: "))
    print(f"Suma de suma: {add_digits(suma)}")


#Al finalizar mostrar la sumatoria de todos los numeros ingresados y la suma de sus digitos
