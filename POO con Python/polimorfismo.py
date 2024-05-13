class Gato():
  def sonido(self):
    return "Miau"
  
class Perro():
  def sonido(self):
    return "Guau"
  
gato = Gato()
perro = Perro()

# Polimorfismo de método
# print(perro.sonido())  

# Otra forma
def hacer_sonido(animal):
  print(animal.sonido())

hacer_sonido(perro)

#-------------------------------------------------------------------
# Aunque Python es de tipado dinámico y sigue la filosofía de su camina como pato y actúa como pato entonces es un pato, entonces la anterior forma que hicimos es válida

# Polimorfismo de herencia:
# class Animal():
#   def sonido(self):
#     pass
  
# class Gato(Animal):
#   def sonido(self):
#     return "Miau"
  
# class Perro(Animal):
#   def sonido(self):
#     return "Guau"
  
# def hacer_sonido(animal):
#   print(animal.sonido())
  
# gato = Gato()
# perro = Perro()

# print(gato.sonido())

#------------------------------------------------------
# # También hay polimorfismo en los tipos de datos:
# num1 = 3
# num2 = 4.4

# # Cohersión automática: Python internamente realiza la operación aunque sean diferentes tipos de datos.
# resultado = num1 + num2 

# print(resultado)
# print(type(resultado))

#----------------------------------------------------------
# Polimorfismo en el for
# def recorrer(elemento):
#   for item in elemento:
#     print(f'El elemento actual es: {item}')
    
# lista = [1,2,3,4]
# lista2 = ["maquina","como","andas"]

# recorrer(lista)
# recorrer(lista2)

# Adicionales para profundizar:
# Duck typing

# Enlaces dinámicos
# Enlaces estáticos

# Tipo real
# Tipo declarado