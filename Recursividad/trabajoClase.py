import random

#Ejercicio 1
def defined_path():
    path = random.choice([1,2,3])
    return path

def try_exit():
    counter = 0
    path = defined_path()
    if (path == 1):
        counter += 3
        print("Camino tomado: 1")
        print("No puedes salir de la jaula")
        print("Te quedaras 3 minutos en la jaula")
    elif(path == 2):
        counter += 5
        print("Camino tomado: 2")
        print("No puedes salir de la jaula")
        print("Te quedaras 5 minutos en la jaula")
    elif(path == 3):
        print("Camino tomado: 3")
        counter += 7
        print("Te quedaras 7 minutos en la jaula")
        print("Puedes salir de la jaula")

try_exit()


#Ejercicio 2
def f(n):
    s = str(n)
    print(s)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

f(434554)
#Escribir una función recursiva que dado un número entero muentre por pantalla un triángulo inverdo cuya base esté conformada 
#por todas sus cifras y cuya punta sea la primer cifra del número. Por ejemplo:
#1234
#123
#12
#1
