#Ejercicio en clase - Iteradores for y while
#Ejercicio 1 - for
#Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, 
# que consiste en correr cada letra del mensaje –considerando la posición de cada una en el 
# alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la 
#palabra “ATAQUE” se transforma en “CVCSWG”. Cada día, el “jefe” del equipo debe enviar un mensaje
#a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. 
#El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de 
#comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.

corrimiento = int(input("Ingrese la cantidad de valores que se correra su frase "))
abece="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for i in range(5):
    frase= input("Ingrese una frase ").upper()
    frase_enc= ""
    for letra in frase:
        if letra in abece:
            indice = abece.find(letra) 
            indice= (indice+corrimiento)%27
            frase_enc += abece[indice]
        else:
            frase_enc +=letra
    print(frase_enc)

#Ejercicio 2 - while
#Crear un programa que solicite el ingreso de números enteros positivos, 
# hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y 
# cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de 
# dígitos impares leídos en total.
print("Números positivos")
numero=1
total_par=0
total_impar=0
while numero != "0":
    numero = input("Ingrese una numeros enteros positivos o 0 (cero) para salir: ")
    par=0
    impar=0
    for i in numero:
        cifra = int(i)
        if (cifra%2==0) :
            par= par+1
            total_par=total_par+1
        else:
            impar= impar+1
            total_impar=total_impar+1
    print(f"Sus numeros pares son {par} Sus numeros impares son {impar}")
print(f"Cifras pares totales: {total_par}")
print(f"Cifras impares totales: {total_impar}")
        
        
