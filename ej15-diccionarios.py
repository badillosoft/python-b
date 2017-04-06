# Crear un diccionario llamado punto, que en la clave
# "x" contenga 10 y en la clave "y" contenga 13

punto = {
    "x": 10,
    "y": 13
}

# Crear una lista de 10 diccionarios donde cada diccionario
# contenga las claves "x" y "y".
# Para el i-esimo diccionario la clave "x" valdra i ** 2
# para el i-esimo diccionario la clave "y" valdra 2 * i + 1
# Hint: Utilizar i en el rango de [1, 10]

puntos = []

for i in range(1, 11):
    p = {
        "x": i ** 2,
        "y": 2 * i + 1
    }
    
    puntos.append(p)

print puntos