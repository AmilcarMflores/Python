class Persona:
  def __init__(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad
    
  def hablar(self):
    print("Hola, estoy hablando un poco")
    
class Artista:
  def __init__(self,habilidad):
    self.habilidad = habilidad
    
  def mostrar_habilidad(self):
    return f'Mi habilidad es: {self.habilidad}'
  
class EmpleadoArtista(Persona,Artista):
  def __init__(self,nombre,edad,nacionalidad,habilidad,empresa,salario):
    # Si heredamos varias clases, podemos hacerlo de la siguiente manera:
    Persona.__init__(self,nombre,edad,nacionalidad)
    Artista.__init__(self,habilidad)
    self.salario = salario
    self.empresa = empresa
    
  def presentarse(self):
    # Si heredamos un método, mejor es comenzar con super().
    print(f'Hola, soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')
    
  
roberto = EmpleadoArtista("Roberto",43,"argentino","Cantar","Google", 10000)

# roberto.presentarse()
    
    
# ¿Cómo sabemos si es una clase y la otra subclase?
# EmpleadoArtista es una subclase de Artista (?)
herencia = issubclass(EmpleadoArtista, Artista)
# print(herencia)

# Roberto es una objeto de EmpleadoArtista (?)
# También Roberto será un objeto de la clase Artista y Persona porque está heredando. 
intancia = isinstance(roberto,Persona)
print(intancia)
