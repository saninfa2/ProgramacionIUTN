#----------------------------------METODOS DE BUSQUEDA------------------------------------
#El proceso para encontrar un elemento particular en un arreglo se llama búsqueda.

#-------------------------------------BUSQUEDA LINEAL-------------------------------------
#La busqueda lineal consiste en recorrer un array desde el principio hasta el fin (de ahí su nombre)
#en busqueda de un elemento.Cuando dicho elemento es encontrado, la busqueda termina
def search_element(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False

#------------------------------------BUSQUEDA BINARIA-------------------------------------
#La busqueda binaria consiste en iniciar la busqueda de un elemento en el centro de la matriz,
#ya que se aplica en matrices ordenadas, si el elemento a buscar es menor que eñ elemento central
#entonces la busqueda sigue por izquierda, caso contrario va por derecha.
def binary_search(array, element):
    #Se define la izquierda como el primer indice del array y derecha como el último
    left = 0
    right = len(array)-1

    #Mientras haya indices izquierdos menores o iguales al derechos
    while left <= right:
        #Se busca el indice medio
        half = (left + right) // 2

        #Si el elemento buscado coincide con el array en posicion medio, se acaba el programa y
        #se retorna el indice del mismo
        if array[half] == element:
            return half 
        #Si no se cumple lo anterior y en el indice medio hay un valor es menor al elemento
        #a left, que inicialmente era cero, se le suma 1 (Busqueda izquierda)
        elif array[half] < element:
            left = half + 1
        
        #Si tampoco se comple lo anterior, entoces se busca por derecha
        else:
            right = half - 1

    #Retorna -1 cuando no se encuentra el elemento en la lista  
    return -1 