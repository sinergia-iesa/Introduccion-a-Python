# ============================================
# TIPOS DE DATOS
# Cada variable guarda información a conveniencia.
# En Python los básicos son: str, int, float, bool.
# ============================================

nombre = "Andrés"        # str   -> texto
edad = 20                 # int   -> número entero
altura = 1.75              # float -> número con decimales
esta_activo = True          # bool  -> verdadero o falso
dinero = 5000.50           # float -> el dinero casi siempre lleva decimales

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(esta_activo))
print(type(dinero))

# Convertir entre tipos, se le pone "= tipo(variable)"
edad_texto = "20"
edad_numero = int(edad_texto)      # de texto a número entero
print(edad_numero + 1)

# input() siempre da texto, por eso hay que convertirlo si es un número:
precio_texto = input("Precio del producto: ")
precio = float(precio_texto)
print(precio * 2)
