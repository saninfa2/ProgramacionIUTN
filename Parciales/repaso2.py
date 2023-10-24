"""#EJERCICIO DE REPASO - PARTE 2
#Ejercicio 1
#Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres 
#de largo, el programa le sumará un signo de exclamación al final, y si no es de 4 caracteres 
#el programa le sumará un signo de interrogación al final. El programa mostrará después la 
#frase final.
print("Frase")
phrase = input("Ingrese una frase o palabra: ")
phrase_leng = len(phrase)
if (phrase_leng == 4):
    phrase += "!"
else:
    phrase += "?"
print(f"Frase final: {phrase}")
"""
#Ejercicio 2
#Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que 
#adivinarla letra por letra. Proporciona un número limitado de intentos y utiliza un bucle 
#while para controlar el juego.
import random
print("Adivina la palabra")
words = ["manzana", "sandia", "frutilla", "mandarina", "naranja", "anana"] 
chosen_word = words[random.randrange(0,5,1)]
tried = 5
exist_words = []
print(f"La palabra tiene {len(chosen_word)} letras")
print(f"Tienes {tried} intentos para adivinar")
while tried > 0:
    answer = input("Ingresa una letra: ")
    #Generamos un booleano que verifique si la letra está en la palabra 
    answer_okey = answer in chosen_word 
    #y otro para ver si está en la lista de palabras adivinadas
    answer_repeat = answer in exist_words

    if (answer_okey and not(answer_repeat)):
        print(f"Correcto! La letra {answer} existe en la palabra")
        exist_words += answer
        print(f"Letras válidas: {exist_words}")
    elif (answer_okey and answer_repeat):
        print(f"La letra ya existe.")
        print(f"{answer} se repite {chosen_word.count(answer)}")
    else:
        print(f"{answer}, no existe en la palabra.")
        tried -= 1
        print(f"Te quedan {tried} intentos")
    
    if (len(exist_words)%2==0):
                print("¿Sabes cuál es la palabra?")
                complete_word = input("Ingrese la palabra: ")
                if (complete_word == chosen_word):
                    print("Correcto!")
                    break
                else:
                    print("Incorrecto! Las palabras no coinciden, sigue intentadolo")
                    tried -= 1 
print(f"La palabra era {chosen_word} 🥳")
print(f"Intentos fallidos: {5-tried}")

    