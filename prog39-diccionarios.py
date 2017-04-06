# Diccionarios

# Un diccionario es una coleccion de datos como las listas
# pero en lugar de guardar valores con indice
# guardamos los valores bajo una clave

# Ejemplo 1:

frutas = { "manzana": "rojo", "platano": "amarillo" }

print frutas["platano"]
print frutas["manzana"]

# Ejemplo 2:

persona = {
    "nombre": "Pepe Perez",
    "edad": 34,
    "sexo": "Hombre",
    "peso": 78.5
}

print persona["nombre"], persona["sexo"]

print "manzana" in persona, "peso" in persona