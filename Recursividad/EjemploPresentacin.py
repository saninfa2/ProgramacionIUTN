#-----------------------------------------FACTORIAL---------------------------------------
#El factorail de un número es el producto de los números entre ese número y 1
def factorial(n):
    #CASO BASE
    if (n == 0 or n == 1):
        factor = n
    else:
        #CASO RECURSIVO
        factor = n * factorial(n - 1)
    return factor
    

number = int(input("Ingrese un numero para sacar factorial: "))
print(f"{number}! = {factorial(number)}")

#-----------------------------------------FIBONACCI---------------------------------------
#La sucesión comienza con dos números dos números naturales cualesquiera y a partir de estos,
#«cada término es la suma de los dos anteriores»,

def fibonacci (n):
    #caso base
    if n == 1:
        fibo = n
    else:
        fibo = n - 1 + fibonacci(n-2)
    return fibo

number2 = int(input("Ingrese un numero para sacar factorial: "))
print(f"{number2}! = {fibonacci(number2)}")