# Crear un diccionario con los datos que describan una mascota

# Crear una lista de diccionarios con al menos 3 mascotas

# Recuperar de la lista de mascotas el valor de una clave,
# por ejemplo, nombre

# Modificar la tercer mascota en una clave, por ejemplo,
# en la clave raza

# Crear un diccionario con las claves "color" y "hexadecimal"
# que contenga en "color" una tupla de 3 numeros enteros
# con valores entre 0 y 255. Utilizar la siguiente funcion
# llamada rgb_hex(r, g, b) y devuelve una cadena de 7 caracteres
# con los valores en hexadecimal del color dato.
# Usar dicha funcion para asignar el valor de la clave
# hexadecimal.

# Ejemplo: d = { "color": (255, 0, 0) }
# d["hexadecimal"] = rgb_hex(255, 0, 0)
# print d # { "color": (255, 0, 0), "hexadecimal": "#FF0000" }

def rgb_hex(r, g, b):
    rx = "%x" % r
    gx = "%x" % g
    bx = "%x" % b

    if len(rx) == 1:
        rx = "0" + rx

    if len(gx) == 1:
        gx = "0" + gx

    if len(bx) == 1:
        bx = "0" + bx

    return "#" + rx + gx + bx

print rgb_hex(255, 0, 0)