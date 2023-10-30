import funcionesRecursivas
#Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
#Ejercicio 1
"""
def counter_digit_v2(n):
    #caso base: si ya no tiene más cifras retorna n
    if n < 10:
        count = 1
    else:
    #caso recursivo: si tiene más de una cifra debe dividirlo por diez, y llamarse a si misma
        count = 1 + counter_digit_v2(n//10)
    return count

print(counter_digit_v2(22))   
print(counter_digit_v2(222))

#Ejercicio 2
#Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b
# 16 es potencia de 4. 16 ^0 == 1 F  -- 16 ^1 = 16 f
def is_potencia(n, b):
    if b == 0 or b == 1:
        potencia = False
    else: 
        potencia = n - is_potencia(n, b-1)
        
    
print(is_potencia(16,4))

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
""" 
#Ejercicio 9
# Ejemplo de uso
caracters = ['A', 'B', 'C']
k = 3
funcionesRecursivas.combinations(caracters, k)

#Ejercicio 10 
def dimensions_peper_A(N):
    if N == 0:
        return (841, 1189)  # Medidas de la hoja A0
    else:
        before_width, before_length = dimensions_peper_A(N - 1)
        new_width = before_length
        new_length = before_width / 2
        return (new_width, new_length)

# Ejemplo de uso
N = 2  # Calcularemos las medidas de la hoja A2
width, length = dimensions_peper_A(N)
print(f"Las medidas de la hoja A{N} son {width} mm de ancho y {length} mm de largo.")




