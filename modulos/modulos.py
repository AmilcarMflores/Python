# Importando un módulo y asignándole el nombre "m_saludar"
# # Namespace --> modulo_saludar
# # as -- > asignar (en estes caso m_saludar para el modulo_saludar)
import modulo_saludar as m_saludar


saludo = m_saludar.saludar("Lucas")
print(saludo)

# print(type(m_saludar))
#------------------------------
# solo importamos la función:
# from modulo_saludar import saludar, saludar_raro as saludar_como_coscu

# saludo = saludar("Lucas")
# saludo_raro = saludar_como_coscu("Frank")

# print(saludo)
# print(saludo_raro)

# Para ver las propiedades y métodos de el namespace
# print(dir(m_saludar))

# Accedemos al nombre de este módulo
print(__name__)

# Accedemos al nombre del módulo llamado
print(m_saludar.__name__)