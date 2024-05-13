# Lógica de nuestro auto
# Definición de la clase Auto
class Auto():
  def __init__(self):
    self._estado = "apagado"
    
  def encender(self):
    self._estado = "encendido"
    print("El auto está encendido")
    
  def conducir(self):
    if self._estado == "apagado":
      self.encender()
    print("Conduciendo el auto")
    
# Instanciamos la clase auto    
mi_auto = Auto()
# Aplicamos el método conducir, pero por dentro se aplica el método enceder, lo cual nosotros no tocamos, pero que la lógica del programa sí.

# Aplicamos el método conducir
mi_auto.conducir()  
    