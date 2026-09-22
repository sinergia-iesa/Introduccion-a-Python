# ============================================
# OPERADORES
# Sirven para hacer cálculos y comparaciones.
# ============================================

# --- Aritméticos ---
precio = 1000
cantidad = 3
total = precio * cantidad  # * da el resultado de una multiplicación
print(total)

mitad = 8 / 2     # / da el cociente de una división
print(mitad)

resto = 9 % 4    # % da el resto de una división
print(resto)

# --- Comparación (el resultado siempre es True o False) ---
edad = 17
es_mayor_de_edad = edad >= 18  # son: ">" y "<" , si se le pone "=" , es menor o mayor igual
print(es_mayor_de_edad)

# --- Lógicos (and, or, not; en Python son palabras, no símbolos) ---
tiene_entrada = True
tiene_identificacion = False
puede_entrar = tiene_entrada and tiene_identificacion
print(puede_entrar)
