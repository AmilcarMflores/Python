#Comentarios:
# separado_por_guiones_bajos --> Snake case
# primerLetraEnMinusculaElRestoEnMayuscula --> Camel Case
# PrimerLetraEnMinusculaElRestoEnMayuscula --> Pascal Case

# La recomendación es usar pascal case
# Crear clases y atributos: Se puede usar la misma forma de la POO en Java, pero en Python hay una forma más interesante:

# # En la forma tradicional (Java):
# class  Celular():
#   #Atributos estáticos
#   marca = "Samsung"
#   modelo = "S23"
#   camara = "48MP"

# #Instanciamos objetos  
# celular1 = Celular()
# celular2 = Celular()
# celular3 = Celular()
# celular4 = Celular()

# print(celular3)

# En Python:
class Celular:
  # Esta función se ejecuta automáticamente
  # Es un método 'constructor'
  # self --> uno mismo
  def __init__(self, marca, modelo, camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara
  
  # En un método siempre tenemos que mandar self para autoreferenciar así mismo
  def llamar(self):
    print(f'Estás haciendo un llamado desde un: {self.modelo}')
    
  def cortar(self):
    print(f'Cortaste la llamada desde un: {self.modelo}')
  
celular1 = Celular("Samsung", "s23", "48mp")
celular2 = Celular("Apple", "Iphone 15 pro", "96mp")

#print(celular2.marca)

celular1.llamar()

