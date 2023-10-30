#Ejercicio 1

#Creamos la clase persona
class Persona:
    
    #Constructor 
    def __init__(self, nombre="", edad="", dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    #Getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if edad.isnumeric():
            self.edad = int(edad)
        else:
            print("La edad debe ser un número válido.")

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if len(dni) == 9 and dni[:8].isnumeric() and dni[8].isalpha():
            self.dni = dni
        else:
            print("El DNI debe tener 8 dígitos numéricos y una letra.")

    #Metodo mostrar, muestra los datos de objetos instanciados
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    #Metodo mayor de edad, evalua si los objetos instanciados tienen más de 18 años
    def esMayorDeEdad(self):
        return self.edad >= 18

#Ejemplo de uso
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad("25")
persona1.set_dni("12345678A")

persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

#Ejercicip 2
#Clase cuenta
class Cuenta:
    #Constructor con atributos titular y cantidad
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Se establecerá en 0.")
            self.cantidad = 0.0
        else:
            self.cantidad = cantidad

    #Getters y setters
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    #Metodo mostrar: muestra los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad: {self.cantidad:.2f} dolares")

    #Metodo ingresar: se ingresa saldo a la cuenta, siempre y cuando el monto no sea negativo
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar no puede ser negativa.")

    #Metodo retirar: se retira una cantidad de saldo siempre y cuando no supere el monto existente en la cuenta
    def retirar(self, cantidad):
        if cantidad >= 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar no puede ser negativa.")

# Clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

# Ejemplo de uso
titular = Persona("Juan Pérez")
cuenta = Cuenta(titular, 100.0)

cuenta.mostrar()
cuenta.ingresar(50.0)
cuenta.retirar(30.0)

cuenta.mostrar()

#Ejercicio 3
#Clase triángulo
class Triangulo:
    
    #Constructor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    #Metodo que te devuelve el lado más largo de un triángulo
    def determinar_lado_mas_largo(self):
        lados = [self.lado1, self.lado2, self.lado3]
        return max(lados)

    #Método que devuelve el tipo de triángulo
    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)
lado_mas_largo = triangulo.determinar_lado_mas_largo()
tipo_triangulo = triangulo.determinar_tipo()

print(f"El lado más largo del triángulo es {lado_mas_largo}")
print(f"El triángulo es de tipo {tipo_triangulo}")

#Ejercicio 4
#Clase contacto
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

#Clase agenda
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto agregado con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre_buscar):
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre == nombre_buscar:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                encontrado = True
                break
        if not encontrado:
            print("El contacto no se encontró en la agenda.")

    def editar_contacto(self, nombre_buscar, nuevo_nombre, nuevo_telefono, nuevo_email):
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre == nombre_buscar:
                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("El contacto no se encontró en la agenda.")

    def menu(self):
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.agregar_contacto(nombre, telefono, email)

            elif opcion == "2":
                self.listar_contactos()

            elif opcion == "3":
                nombre_buscar = input("Nombre a buscar: ")
                self.buscar_contacto(nombre_buscar)

            elif opcion == "4":
                nombre_buscar = input("Nombre a editar: ")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre_buscar, nuevo_nombre, nuevo_telefono, nuevo_email)

            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

# Ejemplo de uso
mi_agenda = Agenda()
mi_agenda.menu()

