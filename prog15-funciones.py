def pares(n):
    lista_pares = []

    for i in range(1, n + 1): # [1, n]
        lista_pares.append(2 * i)
    
    return lista_pares

print pares(10)

print pares(20)