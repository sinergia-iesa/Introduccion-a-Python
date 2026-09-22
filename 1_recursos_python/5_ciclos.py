# ============================================
# CICLOS
# Repiten instrucciones varias veces.
# ============================================

# --- while: se repite MIENTRAS la condición sea verdadera ---
intento = 1
while intento <= 3:
    print("Intento número", intento)
    intento += 1     # sin esto, el ciclo nunca terminaría

# --- for con range(): se repite un número definido de veces ---
for numero in range(1, 6):     # del 1 al 5
    print("Contando:", numero)
