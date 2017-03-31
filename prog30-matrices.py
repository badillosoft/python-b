# Opcion 1:
#   Tomar 1 hora extra la siguiente semana
#   6 a 9 o 7 a 10

# Opcion 2:
#   Pausar el curso y reanudar el 17 de abril

# Opcion 3:
#   5 horas de video explicando los conceptos vistos
#   youtube: Variable, For-In, While, IF, Ejercicios

# Crear una matriz de 3x4
# poner -1 en las columnas pares
# port 1 en las columnas impares

mat = []

# 1. Recorrer las filas
for filas in range(0, 3):
    # 2. Para cada fila crear un vector
    vector = []

    # 3. Recorrer las columnas
    for columna in range(0, 4):
        # 4. Llenar el vector para cada columna
        if columna % 2 == 0:
            vector.append(-1)
        else:
            vector.append(1)
    
    # 5. Agregar el vector a la matriz
    mat.append(vector)

print mat