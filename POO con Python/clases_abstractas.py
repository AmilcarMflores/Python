# La clase ABC es una clase base proporcionada por el módulo abc que se utiliza para definir clases abstractas
# El decorador abstractclassmethod es una función que se utiliza para marcar métodos como abstractos dentro de una clase abstracta.
from abc import ABC, abstractclassmethod

# Definición de la clase abstracta Persona
class Persona(ABC):
    # Constructor abstracto de la clase Persona
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    # Método abstracto que debe ser implementado por las subclases
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    # Método concreto de la clase Persona
    def presentarse(self):
        print(f'Hola, me llamo: {self.nombre} y tengo {self.edad} años')

# Definición de la subclase Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    # Implementación del método hacer_actividad para Estudiante
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')

# Definición de la subclase Trabajador
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    # Implementación del método hacer_actividad para Trabajador
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en el rubro de: {self.actividad}')

# Creación de instancias y uso de las clases
pedrito = Estudiante("Pedrito", 25, "No binario", "programación")
dalto = Trabajador("Lucas", 21, "Masculino", "programación")

# Métodos de instancia
dalto.presentarse()
dalto.hacer_actividad()

pedrito.presentarse()
pedrito.hacer_actividad()
