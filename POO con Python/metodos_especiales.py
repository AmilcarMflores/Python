# Definición de la clase Persona
class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicialización del atributo nombre
        self.edad = edad      # Inicialización del atributo edad
    
    # Método especial para representar el objeto como una cadena legible
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    # Método especial para representar el objeto de manera oficial
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    # Método especial para sobrecargar el operador de suma (+)
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad  # Suma de las edades
        # Creación de una nueva instancia de Persona con la suma de nombres y edades
        return Persona(self.nombre + otro.nombre, nuevo_valor)

# Creación de instancias de la clase Persona
dalto = Persona("Lucas", 21)
pedro = Persona("Pedro", 30)

# Uso del operador de suma (+) sobrecargado para crear una nueva persona
nueva_persona = dalto + pedro

# Impresión de los atributos de la nueva persona
print(nueva_persona.nombre)  # Salida: LucasPedro
print(nueva_persona.edad)    # Salida: 51
