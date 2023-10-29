#--------------------------------METODOS DE ORDENAMIENTO----------------------------------
#Son aquellos metodos que permiten ordenar una lista de elementos mediante algún procedimiento
#Hay muchos metodos, la implimentación de uno u otro se basará en la conveniencia, 

#---------------------------------------BUBBLE SORT----------------------------------------
#Es un metodo extenso y poco eficiente que compara uno por uno los elementos de una lista
#Prácticamente recorrer elemento por elemento buscando poner primero aquellos valores pequeño
#y por el contrario los valores grandes "burbujean" al final de la lista
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
#---------------------------------------SELECT SORT----------------------------------------
#Este proceso costa de recorrer el array y seleccionar (😉) el valor más pequeño del array para 
#llevarlo al principio, y así sucesivamente con todo el array.
def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

#---------------------------------------INSERT SORT----------------------------------------
 
def insert_sort(arr):
    n = len(arr)
    
    # Recorremos desde el segundo elemento hasta el último
    for i in range(1, n):
        # Guardamos el valor actual para compararlo e insertarlo en la posición correcta
        current_value = arr[i]
        position = i
        
        # Movemos los elementos mayores hacia la derecha
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value

#---------------------------------------MERGE SORT----------------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
  
def countsort(A, k): 
    # crea una lista de enteros de tamaño `k + 1` para almacenar el recuento de cada entero
    # en la lista de entrada
    freq = [0] * (k + 1)
 
    # usando el valor de cada elemento en la lista de entrada como un índice,
    # almacena el conteo de cada entero en `freq[]`
    for i in A:
        freq[i] += 1
 
    # sobrescribe la lista de entrada con orden ordenado
    index = 0
    for i in range(k + 1):
        while freq[i] > 0:
            A[index] = i
            index += 1
            freq[i] -= 1
  
def dictionary_sort(list, key):
    return sorted(list, key=lambda x: x[key])
                 
#Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden
#ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción    
def insert_sort_string(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        j = i - 1
        while j >= 0 and len(current_string) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = current_string
        
        
def bubble_sort_mix(arr):
    list_number = []
    list_string = []
    
    for i in range(len(arr)):
        for element in arr:
            if element == int(element):
                list_number.append(element)
            else:
                list_string.append(element)
    bubble_sort(list_number)
    bubble_sort(list_string)
    list_number.append(list_string)
    arr = list_number
    
#FUNCION BASE PARA MOSTRAR UNA LISTA DE FORMA BONITA
def showList(list):
    for elemento in range(len(list)):
        if elemento < (len(list)-1):
            print(list[elemento], end=", ")
        else: 
            print(list[elemento])  