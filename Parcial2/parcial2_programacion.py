#Función que pide una en una las cadenas de ADN, verifica sus letras y su longitud
def askForDNA():
    print("Nuevo ADN")
    #Inicialización de variables
    dna = []
    valid_letters = "ATCG"
    invalid_letter = False
    
    #Mientras la longitud sea distinta de 6 el bucle sigue
    while len(dna) != 6:
        #Se informan las condiciones al usuario
        print("La cadena de ADN se ingresará de a una en el formato XXXXXX, sin espacios")
        print("Si se ingresan más de 6 letras la cadena será cortada")
        new_dna = input("Ingrese la cadena de ADN: ").upper()
        
        #Cada elemento de la cadena se compara con las letras válidas, si se encuentra 1, la cadena ya no es válida
        for i in new_dna:
            if not(i in valid_letters):
                print("Cadena no válida. Los valores solo pueden ser A T G C")
                invalid_letter = True
                break
            else:
                invalid_letter = False
        #Se acorta la cadena por si se ingresaron más caracteres
        new_dna = new_dna[0:6]
        #Si ninguna letra de la cadena es inválida, se agrega al 
        if not(invalid_letter):
            dna.append(new_dna)
    return dna

#---------------------------------------------------- FUNCIONES DE BÚSQUEDA -----------------------------------------------------
#BÚSQUEDA VERTICAL: recibe un array de string lo transpone y llama a la busqueda de subcadena
def verticalSearch(matrix):
    #Inicialización de variables
    sentence = ""
    column = 0
    coincidences = 0
    #Por cada cadena de la matriz se buscan las letras por columna y se concatenan, luego se busca coincidencias 
    while column <= 5:
        for element in matrix:
            sentence += (element[column]) 
        result = substringSearch(sentence)
        if (result):
            coincidences+=1
        sentence = ""
        column+=1
    return coincidences


#BÚSQUEDA HORIZONTAL: por cada elemento de la matriz se busca la subcadena
def horizontalSearch(matrix):
    coincidences = 0
    for element in matrix:
        result = substringSearch(element)
        if result:
            coincidences += 1
    return coincidences
            
            
#BÚSQUEDA DE DIAGONALES SECUNDARIAS Y PRINCIPAL E INVERTIDAS: a partir de una fila inicial y columna inicial busca las diagonales
def diagonalSearch(matrix,initialRow, initialColumn):
    #Inicialización de variables
    sentence = ""
    #Se eliminan las filas anteriores a cero si la busqueda parte de una fila mayor a cero
    if (initialRow != 0):
        for i in range(initialRow):
            del matrix[0]
    
    #Por último se recorre la matriz en busca de las diagonales. Estas son almacenas como cadena en una variable
    for element in matrix:
        if initialColumn < len(matrix):
            sentence+= element[initialColumn]
            if initialColumn > 2:
                initialColumn-=1
            else: 
                initialColumn+=1
    #Para hacer compatible los resultados de las funciones de busqueda devolvemos un número, en vez de false o true
    return 1 if substringSearch(sentence) else 0


#BÚSQUEDA DE SUBCADENA: por cada letra del string busca un patrón, corta si lo encuentra
def substringSearch(sentence):
    for letter in sentence:
        sequence = letter *4
        if sequence in sentence:
            return True
        else:
            continue
    return False

#FUNCIÓN PRINCIPAL
def is_mutant():
    coincidences = 0
    result = False
    #Primero pedimos el adn 
    dna = askForDNA()
    #Búsqueda vertical
    coincidences += verticalSearch(dna)
    #Búsqueda horizontal
    coincidences += horizontalSearch(dna)
    #Búsqueda por diagonales
    coincidences += diagonalSearch(dna, 0,2)
    coincidences += diagonalSearch(dna,0,1)
    coincidences += diagonalSearch(dna,0,0)
    coincidences += diagonalSearch(dna,1,0)
    coincidences += diagonalSearch(dna,2,0)
    #Para evitar sobrecargar la función, solo se llaman a las busquedas de diagonales invertidas si el contador es menor a 1
    if (coincidences < 1):
        coincidences += diagonalSearch(dna,0,3)
        coincidences += diagonalSearch(dna,0,4)
        coincidences += diagonalSearch(dna,0,5)
        coincidences += diagonalSearch(dna,1,5)
        coincidences += diagonalSearch(dna,2,5)
    
    if coincidences >= 2:
        result = True
        
    return result
    
    
#--------------------------------------Programa principal-----------------------------------------
#Damos la bienvenida al usuario
print("Bienvenido a Mutant")

#Inicialización de variables
answer = 0

#Mientras la respuesta no sea salir, el bucle no se corta
while answer != 2:
    print("(1) Verificar mutante  (2) Salir")
    answer = int(input("Ingrese el número de la operación que desea realizar: "))
    #Si ingresa 2 el bucle se corta
    if(answer == 2):
        break
    #Si ingresa 1 se llama a la función askForDna para pedir y validar adn
    elif(answer == 1):
        if (is_mutant()):
            print("El ADN es mutante.")
        else: 
            print("El ADN no es mutante.")
    #Si la opción no es ninguna de las anteriores se le vuelve a presentar el menu
    else:
        print("Opción inválida. Intente nuevamente")
        
print("Fin del programa. Adios 🤠")


