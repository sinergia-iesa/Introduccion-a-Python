---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">1</div>

# Variables

<div class="prep-subtitle">Guardar información en la memoria</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Variables</div>

# Crear una variable

- Una variable es como una **"caja" con nombre** que guarda un dato
- En Python no hay que indicar el tipo: **se detecta solo**
- El nombre va a la izquierda, el valor a la derecha del `=`

::right::

```python
nombre = "Camila"       # una caja llamada "nombre" que guarda texto
edad = 20                # una caja llamada "edad" que guarda un número
precio_cafe = 1500       # otra variable, con otro dato

print(nombre)
print(edad)
print(precio_cafe)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Variables</div>

# Reemplazar el valor

- El valor de una variable **puede cambiar** en cualquier momento
- Solo hay que volver a asignarlo con `=`
- El nuevo valor reemplaza al anterior

::right::

```python
precio_cafe = 1500
precio_cafe = 1600
print(precio_cafe)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Variables</div>

# Pedir datos a quien usa el programa

- `input()` muestra un mensaje y **espera** lo que la persona escriba
- OJO: `input()` **siempre** devuelve texto

::right::

```python
nombre_usuario = input("¿Cómo te llamás? ")
print("Hola,", nombre_usuario)
```

---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">2</div>

# Tipos de datos

<div class="prep-subtitle">Qué clase de información guarda cada variable</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Tipos de datos</div>

# Los 4 tipos básicos

- `str` &rarr; texto
- `int` &rarr; número entero
- `float` &rarr; número con decimales
- `bool` &rarr; verdadero o falso

::right::

```python
nombre = "Andrés"        # str
edad = 20                 # int
altura = 1.75              # float
esta_activo = True          # bool
dinero = 5000.50           # float, el dinero casi siempre lleva decimales

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(esta_activo))
print(type(dinero))
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Tipos de datos</div>

# Convertir entre tipos

- Se usa `tipo(variable)`
- Muy útil cuando un dato llega como texto y se necesita como número

::right::

```python
edad_texto = "20"
edad_numero = int(edad_texto)      # de texto a número entero
print(edad_numero + 1)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Tipos de datos</div>

# input() siempre da texto

- Si se necesita un número, **hay que convertirlo**
- Si no, Python no va a poder hacer cálculos con ese dato

::right::

```python
precio_texto = input("Precio del producto: ")
precio = float(precio_texto)
print(precio * 2)
```

---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">3</div>

# Operadores

<div class="prep-subtitle">Cálculos y comparaciones</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Operadores</div>

# Aritméticos

- `*` da el resultado de una multiplicación
- `/` da el cociente de una división
- `%` da el **resto** de una división

::right::

```python
precio = 1000
cantidad = 3
total = precio * cantidad
print(total)

mitad = 8 / 2
print(mitad)

resto = 9 % 4
print(resto)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Operadores</div>

# De comparación

- El resultado siempre es `True` o `False`
- Son: `>`, `<`, `>=`, `<=`, `==`, `!=`

::right::

```python
edad = 17
es_mayor_de_edad = edad >= 18
print(es_mayor_de_edad)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Operadores</div>

# Lógicos

- `and`, `or`, `not`
- En Python son **palabras**, no símbolos

::right::

```python
tiene_entrada = True
tiene_identificacion = False
puede_entrar = tiene_entrada and tiene_identificacion
print(puede_entrar)
```

---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">4</div>

# Condicionales

<div class="prep-subtitle">El programa decide qué hacer</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Condicionales</div>

# if / else

- `if` ejecuta un bloque **si la condición es verdadera**
- `else` cubre el resto de los casos
- OJO: en Python la **sangría** (los espacios al inicio de la línea) es la sintaxis

::right::

```python
edad = int(input("¿Cuántos años tenés? "))

if edad >= 18:
    print("Puede votar")
else:
    print("Todavía no puede votar")
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Condicionales</div>

# Más de dos caminos: elif

- Cuando hay más de dos casos posibles, se agrega `elif`
- Python revisa las condiciones **en orden**, de arriba hacia abajo

::right::

```python
saldo = 5000
monto_a_pagar = 7000

if saldo >= monto_a_pagar:
    print("Pago aprobado")
elif saldo > 0:
    print("Saldo insuficiente")
else:
    print("Cuenta sin fondos")
```

---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">5</div>

# Ciclos

<div class="prep-subtitle">Repetir instrucciones</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Ciclos</div>

# while

- Se repite **mientras** la condición sea verdadera
- Hay que actualizar la variable dentro del ciclo, o nunca termina

::right::

```python
intento = 1
while intento <= 3:
    print("Intento número", intento)
    intento += 1     # sin esto, el ciclo nunca terminaría
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Ciclos</div>

# for con range()

- Se repite un **número definido** de veces
- `range(1, 6)` genera del 1 al 5 (el último número no se incluye)

::right::

```python
for numero in range(1, 6):     # del 1 al 5
    print("Contando:", numero)
```

---
layout: center
class: prep-ambiente prep-divider text-center
---

<div class="prep-step-badge mx-auto">6</div>

# Listas

<div class="prep-subtitle">Guardar varios datos juntos</div>

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Listas</div>

# Crear y acceder

- Una lista guarda **varios datos juntos**, en orden
- El primer elemento siempre está en la **posición 0**

::right::

```python
frutas = ["manzana", "pera", "uva"]
print(frutas)
print(frutas[0])       # "manzana", el primer elemento
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Listas</div>

# Agregar y recorrer

- `.append()` agrega un elemento **al final**
- `for` recorre la lista elemento por elemento

::right::

```python
frutas.append("banano")    # agrega un elemento al final
print(frutas)

for fruta in frutas:
    print(fruta)
```

---
layout: two-cols
layoutClass: gap-10 items-center
class: prep-ambiente
---

<div class="prep-eyebrow">Listas</div>

# Ejemplo integrador

- Junta todo lo visto: **variable + tipo + ciclo + lista**
- Así se ve un programa real, aunque sea chiquito

::right::

```python
notas = [85, 90, 70, 60]   # arreglo de notas, hay en total 4
suma = 0                    # suma inicial en 0

for nota in notas:          # por cada nota en la lista de notas
    suma += nota             # a la suma se le suma la nota actual

promedio = suma / len(notas)
print("Promedio:", promedio)
```

---
layout: center
class: prep-ambiente prep-divider text-center
hideInToc: true
---

# ¡A programar!

<div class="prep-subtitle">Variables · Tipos de datos · Operadores · Condicionales · Ciclos · Listas</div>
