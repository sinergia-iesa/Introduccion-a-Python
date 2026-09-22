# ============================================
# LISTAS
# Guardan varios datos juntos, en orden.
# El primer elemento siempre está en la posición 0.
# ============================================

frutas = ["manzana", "pera", "uva"]
print(frutas)
print(frutas[0])       # "manzana", el primer elemento

frutas.append("banano")    # agrega un elemento al final
print(frutas)

for fruta in frutas:
    print(fruta)

# =====================================================
# Ejemplo uniendo todo: variable + tipo + ciclo + lista

notas = [85, 90, 70, 60] # arreglo de notas, hay en total 4

suma = 0 # suma inicial en 0

for nota in notas: # por cada nota en la lista de notas
    suma += nota # a la suma se le suma la nota actual en ese orden

promedio = suma / len(notas) #
print("Promedio:", promedio)
