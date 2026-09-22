# ============================================
# VARIABLES
# Una variable es como una "caja" con nombre que
# guarda un dato.
# ============================================

nombre = "Camila"       # una caja llamada "nombre" que guarda texto
edad = 20                # una caja llamada "edad" que guarda un número
precio_cafe = 1500       # otra variable, con otro dato

print(nombre)
print(edad)
print(precio_cafe)

# Una variable se puede reemplazar en cualquier momento:
precio_cafe = 1600
print(precio_cafe)

# input() sirve para pedirle un dato a la persona que usa el programa.
# OJO: siempre devuelve texto, aunque la persona escriba un número
# (eso se resuelve en el ejemplo de tipos de datos).
nombre_usuario = input("¿Cómo te llamas? ")
print("Hola,", nombre_usuario)
