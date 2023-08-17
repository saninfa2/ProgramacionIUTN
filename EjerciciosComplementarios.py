# consigna 1
#Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 5
print(f"Número uno: {numero1}")

#consigna 2
#No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = 5.5
print(f"Número dos: {numero2}")

#consigna 3
#Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2
print(f"{numero1} + {numero2} = {suma}")

#consigna 4
#Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división. Imprime estas variables
resto = numero2 - numero1
print(f"{numero2} - {numero1} = {resto}")

cociente = numero1/numero2
print(f"{numero1} / {numero2} = {cociente}")

producto = numero2 * numero1
print(f"{numero2} x {numero1} = {producto}")

#consigna 5
#Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Sabina"
print(f"Mi nombre es: {nombre}")

#consigna 6 
#Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.
precio = 22.8
print(f"Precio del artículo ficticio: {precio}")

#consigna 7
#Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo. 
#Por ejemplo, si le quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el valor 0 al 0%.
descuento = 0.10
print(f"El descuento obtenido es del {descuento}")

#consigna 8
#Ahora, intenta calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final". 
# Para ello vas a tener que aplicar la lógica de matemáticas.
precio_final = precio - (descuento * precio)
print(f"El precio final es: {precio_final}")

#consigna 9
#Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.
cadena = "Lorem Ipsum"
print(f"String: {cadena}")

#consigna 10
#Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". 
# En ella, vas a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de Python.
longitud = len(cadena)
print(f"Longitud del String: {longitud}")

#consigna 11
#Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y conviértelo en número entero.
# Lo puedes hacer en la misma variable o en otra, da lo mismo
precio = int(33.4)
print(f"Precio actualizado: {precio}")

#consigna 12
#Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas en una tercera variable llamada "nombre_completo", el nombre y el apellido con un espacio entre medio. 
# Puedes usar libremente la forma de concatenación que quieras.
nombre = "Sabina "
apellido = "Fabrega"
nombre_completo = nombre + apellido
print(f"Nombre completo: {nombre_completo}")

#consigna 13
#Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 20
edad += 5
edad -= 10
print(f"Edad: {edad}")

#consigna 14
#Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.
altura = 1.67
altura *= 4
altura /= 3
print(f"Altura: {altura}")

#consigna 15
#Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas con algún método o función de Python.
nombre_completo = "SABINA FABREGA"
print(f"Nombre completo en minúsculas: {nombre_completo.lower()}")

#consigna 16
#Por último, con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas excepto la primera letra.
nombre_completo = nombre_completo.title()
print(f"Nombre completo: {nombre_completo}")

