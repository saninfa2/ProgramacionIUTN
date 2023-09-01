#Ejercicio en clase - Iteradores for y while
#Ejercicio 1 - for
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
print("Números positivos")
numero=1
total_par=0
total_impar=0
while numero != "0":
    numero = input("Ingrese una cifra para desglozarla ")
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
        
        
