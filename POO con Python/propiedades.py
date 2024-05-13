# Definición de la clase Persona
class Persona:
    # Constructor de la clase con atributos privados __nombre y _edad
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado (__nombre)
        self._edad = edad       # Atributo protegido (_edad)

    # Decorador @property para obtener el nombre (__nombre)
    @property
    def nombre(self):
        return self.__nombre

    # Decorador @nombre.setter para modificar el nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    # Decorador @nombre.deleter para eliminar el nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre

# Creación de un objeto de la clase Persona con nombre "Lucas" y edad 21
dalto = Persona("Lucas", 21)

# Obtener el nombre del objeto dalto
nombre = dalto.nombre
print(nombre)  # Salida: Lucas

# Modificar el nombre del objeto dalto a "Pepe"
dalto.nombre = "Pepe"
# Obtener el nuevo nombre del objeto dalto
nombre_modificado = dalto.nombre
print(nombre_modificado)  # Salida: Pepe

# Eliminar el nombre del objeto dalto
del dalto.nombre
# Tras eliminar el nombre, si intentamos acceder, obtendremos un AttributeError
# nombre = dalto.nombre  # Descomentar esta línea generará un AttributeError

print("¿Qué estás haciendo?")  # Salida: ¿Qué estás haciendo?
