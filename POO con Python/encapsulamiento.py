class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido: puede ser accedido desde fuera de la clase, pero se considera convencionalmente como protegido
        self._edad = edad      # Atributo protegido: lo mismo que el anterior

    def get_nombre(self):     # Método público para obtener el nombre
        return self._nombre

    def set_nombre(self, new_nombre):  # Método público para establecer el nombre
        self._nombre = new_nombre

# Creación de un objeto de la clase Persona
dalto = Persona("Lucas", 21)

# Obteniendo el nombre del objeto "dalto" y almacenándolo en la variable "nombre"
nombre = dalto.get_nombre()
print(nombre)  # Imprime: Lucas

# Cambiando el nombre del objeto "dalto" a "Pepito"
dalto.set_nombre("Pepito")

# Obteniendo el nuevo nombre del objeto "dalto" y almacenándolo en la variable "nombre"
nombre = dalto.get_nombre()
print(nombre)  # Imprime: Pepito
