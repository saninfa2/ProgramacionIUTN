#Ejercicio 3
def found_position(a, b, index=0):
    # Inicializar una lista para almacenar las posiciones encontradas
    position = []

    # Buscar la primera ocurrencia de b en a a partir del índice actual
    occurrence_index = a.find(b, index)

    if occurrence_index != -1:
        # Si se encuentra una ocurrencia, agregarla a la lista de posiciones
        position.append(occurrence_index)
        # Llamar a la función de manera recursiva para buscar más ocurrencias
        position.extend(found_position(a, b, occurrence_index + 1))

    return position

#Ejercicio 4
def pair(n):
    if n == 0:
        return True  # 0 se considera un número par
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False  # 1 se considera un número impar
    else:
        return pair(n - 1)
    
    
#Ejercicio 5
def found_max(list):
    if len(list) == 1:
        return list[0]
    else:
        max_remaining = found_max(list[1:])
        if list[0] > max_remaining:
            return list[0]
        else:
            return max_remaining
        
#Ejercicio 6
def reply(list, n):
    if not list:
        return []
    else:
        element, *remaining = list
        return [element] * n + reply(remaining, n)
    
#Ejercicio 7
def calculate_sum(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_sum(n - 1, p)
    
#Ejercicio 8
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
    
#Ejericicio 9
def combinations(list, k, cadena_actual=""):
    if k == 0:
        print(cadena_actual)
        return
    for caracter in list:
        combinations(list, k - 1, cadena_actual + caracter)