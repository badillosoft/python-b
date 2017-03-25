# Una funcion es un conjunto de sentencias, es decir,
# un bloque de instrucciones que puede ser llamado
# muchas veces, repitiendo la ejecucion del bloque
# y opcionalmente recibe parametros de entrada
# y opcionalmente devuelve un valor de salida

# Sintaxis
def suma(a, b):
    return a + b

# Llamada a la funcion
c = suma(1, 8)

print "La suma de 1 y 8 es:", c

print "La suma de 4 y 7 es:", suma(4, 7)