vector_fila = [1, 2, 3, 4] # vector fila

vector_columna = [
    [1],
    [2],
    [3],
    [4]
]

mat_2_2 = [
    [1, 2],
    [3, 4]
]

def matriz(n, m):
    mat = []

    for i in range(0, n):
        vector = [0 for j in range(0, m)]
        mat.append(vector)

    #n = len(mat)
    #m = len(mat[0])

    return mat

def print_matriz(mat):
    print "+", "- " * (len(mat[0]) - 2), "- +"
    for vector in mat:
        print "|",
        for x in vector:
            print x,
        print "|"
    print "+", "- " * (len(mat[0]) - 2), "- +"
    

mat = matriz(5, 10)

print_matriz(mat)