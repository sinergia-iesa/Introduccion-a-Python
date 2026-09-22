# ============================================
# CONDICIONALES (if)
# El programa decide qué hacer según si algo es
# verdadero o falso.
# OJO: en Python la sangría (los espacios al inicio
# de la línea) SÍ importa.
# ============================================

edad = int(input("¿Cuántos años tenés? "))

if edad >= 18: # OJO que es mayor o igual a 18

    print("Puede votar") # caso mayor o igual a 18

else:
    print("Todavía no puede votar") # caso menor a 18

# Con más de dos caminos se usa elif:
saldo = 5000
monto_a_pagar = 7000

if saldo >= monto_a_pagar:
    print("Pago aprobado")
elif saldo > 0:
    print("Saldo insuficiente")
else:
    print("Cuenta sin fondos")
