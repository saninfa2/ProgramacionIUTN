#Clase motocicleta con sus atributos inicializados: estado y motor
#Todas las motocicletas son nuevas y todas están apagadas
class motocicleta:
    estado = "nuevo"
    motor = False
    
    #Metodo constructor con sus respectivos atributos
    def __init__(self, color, matricula, combustible_litros, numero_ruedas = 2, marca="", modelo="", fecha_fabricacion="", velocidad_punta=0, peso=0):
        self.color = color
        self.marca = matricula
        self.combustible_litros = combustible_litros
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
    
    #Método arrancar que "enciende" el motor si está apagado o avisa que se encuentra encendido
    def arrancar(self):
        if self.motor:
            print("El motor ya está encendido")
        else: 
            self.motor = True
            print("El motor se ha encendido")
            
    #Método detener que "detiene" el motor si está prendido o avisa que está apagado     
    def detener(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido")
        else: 
            print("El motor ya está detenido")
        
    #Método para obtener el precio de una moto
    def obtener_precio(sefl):
        return sefl.precio


motocicleta1 = motocicleta(color= "rojo", matricula = "abc-123", combustible_litros= 10, marca="motorola", modelo= "MT-A31")
motocicleta2 = motocicleta(color= "gris", matricula = "abc-321", combustible_litros= 10, marca="motorola", modelo= "MT-A32")


# Prueba los métodos de arranque y detención
motocicleta1.arrancar()
motocicleta1.detener()

# Añade un precio desde fuera de la clase
motocicleta1.precio = 12000  

# Imprime el precio desde fuera de la clase
print(f"El precio de la motocicleta {motocicleta1.marca} {motocicleta1.modelo} es de ${motocicleta1.obtener_precio()}.")

    
        