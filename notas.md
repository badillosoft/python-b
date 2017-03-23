# Notas de Python

Instructor: Alan Badillo Salas [badillo.soft@hotmail.com](badillo.soft@hotmail.com)

## 1. Fundamentos

Un programa en `python` consite de variables, funciones, clases y módulos los cuales
mediante estructuras de control nos permiten resolver problemas computacionales.

Es recomendable seguir los siguientes puntos para resolver un problema:

* Plantear el problema de forma que logremos identificar la entrada y salida del programa.

* Idear un método conceptual de como resolveríamos el problema si fueramos una computadora.

* Plantear el algoritmo que soluciona el problema de tal forma que quede como una lista de pasos
que logremos entender y seguir hasta alcanzar la solución y creamos que es posible de implementar.

* Codificar cada uno de los pasos mediante python tomando en cuenta que las repeticiones o ciclos
del algoritmo y las decisiones se llevarán a cabo mediante las estructuras de control
(`for`, `while`, `if`).

### 1.1 Variables

Las variables son espacios de memoria nombrados asociados a un tipo para guardar datos en nuestro
programa, por ejemplo, valores temporales para realizar operaciones o incluso arreglos de datos
para procesarlos.

> Distintos tipos de variables y métodos útiles

~~~py
# declarar una variable que guarde un numero
a = 123

# crear otra variable utilizando el valor de a guardado
b = a ** 2 # x ** y : es el operador exponencial x^y

# imprimir los valores de las variables
print a, b
~~~

Las variables pueden almacenar números enteros, flotantes, cadenas de caracteres, booleanos, nulos,
arreglos de otras variables o valores, tuplas de datos, diccionarios y expresiones lamda.

> Imprime dos números flotantes con formato

~~~py
# 1 / 3 devuelve 0 porque la division entre numeros enteros es entera
a = 1 / 3.0
b = 2 / float(a)

# mediante la interpolacion de cadenas podemos dar formato a numeros con decimales
print "A = %.2f | B = %.8f" % (a, b)
~~~

### 1.2 Funciones

Una función es un fragmento de código que toma parametros de entrada y opcionalmente devuelve
una salida, ejecutando líneas de código cuando es llamada. Las funciones abstraen la funcionalidad
de un proceso altamente repetible para ahorrar código. Otra forma de nombrar a las funciones es 
mediante la palabra `rutina`.

> Define una función saludar que muestra un mensaje formateado usando los parámetros

~~~py
# ejemplo de la funcion nombre que recibe dos parametros y devuelve None
def saludar(nombre, apellido):
  # Ponemos todo el codigo
  return "hola: %s %s" % (nombre, apellido)
  
print saludar("ash", "ketchup")
~~~

### 1.3 Arreglos

Un arreglo es un conjunto de datos el cual se accede mediante una variable y los `[]` indicando 
el índice empezando siempre por el índice 0.

> Varios arreglos con distintos datos

~~~py
# crea un arreglo de numeros explicitamente
a = [1, 3, 5, 7, 9]

# imprime el arreglo
print a

# agrega el elemento 11 al final del arreglo
a.append(11)

print a

# elimina y devuelve el elemento de la posicion 0 del arreglo
print a.pop(0)

print a

# inserta el elemento 6 en el indice 3, es decir, la posicion 4 real
a.insert(3, 6)

print a

# agrega los elementos de lista
a.fromlist([2, 4, 6, 8, 10])

print a

# elimina el elemento con indice 1
a.remove(1)

print a

# cuenta el numero de elementos 6 en el arreglo
print a.count(6)
~~~

### 1.4 Condicional _if_

Una condicional es una estructura que nos permite ejecutar un bloque de código
sólo si se cumple una condición booleana

> Imprimir si la variable x es mayor o igual a 32

~~~py
# raw_input devuelve una cadena de texto con lo que ingrese el usuario desde 
# la entrada estandar y int(...) convierte a la cadena ... en un entero (si se puede)
x = int(raw_input("Dame x: "))

if x >= 32:
  print "x es mayor o igual a 32"
~~~

Opcionalmente las condicionales pueden contener un bloque negativo en caso de que la
condición no se cumpla.

> Determinar si la variable y es menor a 8 y mostrar si lo es o no lo es

~~~py
y = int(raw_input("Dame y: "))

if y < 8:
  print "y es menor a 8"
else:
  print "y no es menor a 8 (y >= 8)"
~~~

Finalmente podemos anidar varias condiciones para el caso en que necesitemos ejecutar sólo
una condición que se cumpla y las demás no.

> Determinar en que etapa de la vida se encuentra según la edad

~~~py
edad = int(raw_input("Dame tu edad: "))

if edad <= 11:
  print "Eres un niño"
elif edad < 18:
  print "Eres un adolescente"
elif edad < 60:
  print "Eres un adulto"
elif edad < 120:
  print "Eres chido"
else:
  print "La edad es falsa"
~~~

### 1.5 Ciclo _for-in_

Un ciclo iterador consiste en recorrer un elemento iterable, generalmente una lista y
asiganar el valor iterado en una variable llamada `elemento iterado`.

> Imprimir los números de 1 a 100

~~~py
for i in range(1, 101):
  print i
~~~

> Recorrer los elementos de una lista

~~~py
a = [1, 3, 5, 7, 9, 11]

for x in a:
  print x
  
for i in range(0, len(a)):
  print a[i]
~~~

### 1.6 Ciclo _while_

Un ciclo repetidor consiste en repetir un bloque de código mientras una condición booleana se cumpla.

> Solicitar al usuario un número hasta que sea 4

~~~py
n = 0

while n != 4:
  n = int(raw_input("Dame un numero: "))
  
while True:
  n = int(raw_input("Dame un numero: "))
  
  if n == 4:
    break
~~~

## 1. Ejemplos

> Hacer función que convierta de grados a radianes

~~~py
import math

def deg_to_rad(d):
  return d * math.pi / 180.0
~~~

> Hacer una función que cuente el número de palabras en una cadena

~~~py
s = "hola esta es una cadena de prueba para contar el numero de palabras"

# creamos un arreglo que guarde las cadenas separadas por espacio
aux = s.split(" ")

print aux

# el numero de cadenas en el arreglo determina el numero de palabras en la cadena
palabras = len(aux)

print "El numero de palabras es %d" % palabras
~~~

> Copiar una cadena en otra vacia

~~~py
s = "hola mundo"

r = ""

for i in range(0, len(s)):
  r += s[i]
  
r = ""

for c in s:
  r += c
~~~

> Quitar los espacios multiples en una cadena para que quede una cadena con a lo mas
un espacio de separación en palabras. Ejemplo: `hola       mundo` => `hola mundo`.

~~~py
s = "hola                                   mundo            :)"

r = ""

hay_doble_espacio = False

for c in s:
  if c != " ":
    hay_doble_espacio = False
  elif c == " ":
    if hay_doble_espacio:
      continue
    hay_doble_espacio = True
    
  r += c
  
print r
~~~

> Quitar los espacios de una cadena

~~~py
s = "h o l    a        m  un  d  o         : )    "

r = ""

for c in s:
  if c != " ":
    r += c
    
r = ""

for c in s:
  if c == " ":
    continue
 
  r += c
  
print r
~~~

> Comprobar si una cadena es un palindromo

~~~py
s = "anitalavalatina"

n = len(s)

es_palindromo = True

for i in range(0, n):
  if s[i] != s[n - 1 - i]:
    es_palindromo = False
    break
    
# a = valor_v if condicion else valor_f
# max = x if x > y else y
print ("Es palindromo" if es_palindromo else "No es palindromo")
~~~
