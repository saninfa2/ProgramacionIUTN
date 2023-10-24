#-------------------------------- FUNCIONES  ----------------------------------

#Funcion para graficar los guiones de la letra faltante y letras adivinadas
def graficarGuiones(palabra, listaPalabrasAdivinadas):
    for i in palabra:
        if (i in listaPalabrasAdivinadas):
            print(f"{i} ", end=" ")
        else:
            print(f"_ ", end=" ")
    print(" ")
    
    
#Funcion para verificar si la letra está en la palabra
def adivinarPalabra(palabra, letra):
    if (letra in palabra):
        return True


#si todas las letras de la palabra están en la lista, el juego termina    
def cerrarjuego(word, list):
    counter = 0
    for i in word:
        if i in list:
            counter+=1
    if (counter == len(word)):
        return True


#Si el jugador se queda sin intentos lo despedimos pero si adivinó la palabra lo felicitamos  
def despedir(intents):
    if intents == 0:
        print("Ya no tienes más intentos!")
        print(f"La palabra era {word_to_guess}")
        print("Suerte para la próxima 🥴")
    else:
        print("Felicidades has adivinado la palabra! 🥳")
 
    
#De acuerdo a la cantidad de letras de la palabra el m
def cuantificarIntentos(palabra):
    intentos = 0
    if (len(palabra)< 8):
        intentos = 6
        #muneco con: cabeza, brazo inq y der, pierna izq y der y tronco
    else:
        intentos=8
        #muneco con: cabeza, brazo inq y der, pierna izq y der, pie izq y der y tronco
    return intentos
    
#------------------------- PROGRAMA PRINCIPAL ----------------------------------

import random

#Introducción al ahorcado
print("Bienvenido al juego del Ahorcado")

#Definimos la lista de palabras a adivinar
list_words_to_guess = ["MONITOR", "TECLADO", "SOFTWARE", "HARDWARE", "COMPILADOR", "INTERPRETE", "LENGUAJE", "COMPUTADOR", "PERIFERICO", "SMARTPHONE", ]

#Elegimos una al azar
word_to_guess = list_words_to_guess[random.randrange(0, 9, 1)]

#Declaracion e iniciación de variables
len_of_word_to_guess = len(word_to_guess)
list_guessed_words = []
intent = cuantificarIntentos(word_to_guess)

#Le damos una pista al jugador, diciendole cuantas letras tiene la palabra
print(f"La palabra tiene {len(word_to_guess)} letras")
print(f"Tienes {intent} intentos")
graficarGuiones(word_to_guess, list_guessed_words)

while intent != 0 and not cerrarjuego(word_to_guess, list_guessed_words):
    word_input = input("Ingresa una letra: ").upper()
    
    #Solo se permitirán entradas de longitud 1
    if (len(word_input) == 1):
        if (adivinarPalabra(word_to_guess, word_input)):
            list_guessed_words.append(word_input)
            print("Acertaste una letra!")
        else:
            print("Erraste una palabra")
            print(f"Te quedan {intent}")
            intent -= 1
    else: 
        #no será posible ingresar más de un caracter
        print("Error! Ingresa solo una letra a la vez")
    graficarGuiones(word_to_guess, list_guessed_words)

despedir(intent)
        
