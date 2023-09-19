#El siguiente programa debería imprimir el número 2 si se le ingresan los valroes x=5, y =1
#pero en su lugar imprimer 5 ¿que debería corregir?

#DEFINICIÓN DE FUNCIONES

def most(a,b):
    if(a>b):
        return a
    else:
        return b

def least (a,b):
    if(a<b):
        return a
    else:
        return b

#PROGRAMA PRINCIPAL
x = int(input('Un número: ')) 
y = int(input('Otro número: '))
print(most(x-3, least (x+2, y-5)))

#El problema era que los parametros dentro de la definición de la función 
#tomaban el nombre de las variables declaradas dentro del programa principal
#En su lugar, debería llamar a las variables con los nombres de los parametros