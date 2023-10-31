#PRIMERA PARTE
#clase padre
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas,velocidad, cilindrada)
        self.carga = carga
        
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
#SEGUNDA PARTE
class Animal():
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def talk(self):
        print("El animal hace un sonido genérico")
        
    def information(self):
        print(f"Soy {self.nombre}, tengo {self.edad} y soy un {self.genero}")

class Cat(Animal):
    
    def talk(self):
        print("Miau")
        
   
        
class Bird(Animal):
    def __init__(self, nombre, edad, genero, especie):
        super().__init__(nombre, edad, genero)
        self.especie = especie
               
    def talk(self):
        print("Pio pio")
        
    def information(self):
        print(f"Soy {self.nombre}, tengo {self.edad}, soy un {self.genero} y un {self.especie}")
        
class Dog(Animal):
    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, edad, genero)
        self.raza = raza
        
    #Metodo talk sobreescrito 
    def talk(self):
        print("Guau")
        
    def information(self):
        print(f"Soy {self.nombre}, tengo {self.edad}, soy un {self.raza}, {self.genero}")
    
    
dog1 = Dog("Joji", 5, "Macho", "Corgi")
dog1.information()

dog1.talk()