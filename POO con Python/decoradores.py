def decorador(funcion):
  def funcion_modificada():
    print("Antes de llamar a la función")
    funcion()
    print("Después de llamar a la función")
  return funcion_modificada

# def saludo():
#   print("Hola Dalto")
  
# saludo_modificado = decorador(saludo)
# saludo_modificado()

# Decoración de la función "saludo" con el decorador "@decorador"
@decorador
def saludo():
  print("Hola Dalto")

# Llamada a la función decorada "saludo"
saludo()

# Adicionales:
# decoradores de clases
# decoradores múltiples