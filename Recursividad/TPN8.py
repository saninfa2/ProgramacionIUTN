import funcionesRecursivas

#Ejercicio 1
print(funcionesRecursivas.counter_digit_v2(22))   
print(funcionesRecursivas.counter_digit_v2(222))

#Ejercicio 2
print(funcionesRecursivas.is_potencia(16,4))

#Ejercicio 3
# Ejemplo de uso
a = "abracadabra"
b = "a"
position = funcionesRecursivas.found_position(a, b)
print(f"Las posiciones de '{b}' en '{a}' son: {position}")

#Ejercicio 4
# Ejemplos de uso
number = 6
if funcionesRecursivas.pair(number):
    print(f"{number} es par.")
else:
    print(f"{number} es impar.")

number = 7
if funcionesRecursivas.odd(number):
    print(f"{number} es impar.")
else:
    print(f"{number} es par.")

#Ejercicio 5
# Ejemplo de uso
list = [12, 45, 23, 67, 8, 100, 34, 56]
max = funcionesRecursivas.found_max(list)
print(f"El elemento máximo en la lista es {max}.")

#Ejercicio 6
# Ejemplo de uso
list = [1, 3, 3, 7]
n = 2
result = funcionesRecursivas.reply(list, n)
print(result)

#Ejercicio 7
# Solicitar al usuario que ingrese n y p
n = int(input("Ingresa el valor de n: "))
p = int(input("Ingresa el valor de p: "))

# Calcular la sumatoria K(n, p) usando la función recursiva
result = funcionesRecursivas.calculate_sum(n, p)

# Imprimir el resultado
print(f"K({n}, {p}) = {result}")

#Ejercicio 8
# Ejemplo de uso
n = 5
k = 2
resultado = funcionesRecursivas.pascal(n, k)
print(f"El valor en la fila {n} y columna {k} del Triángulo de Pascal es {resultado}.")

#Ejercicio 9
# Ejemplo de uso
caracters = ['A', 'B', 'C']
k = 3
funcionesRecursivas.combinations(caracters, k)

#Ejercicio 10 
# Ejemplo de uso
N = 2  # Calcularemos las medidas de la hoja A2
width, length = funcionesRecursivas.dimensions_peper_A(N)
print(f"Las medidas de la hoja A{N} son {width} mm de ancho y {length} mm de largo.")




