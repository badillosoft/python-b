def ordenar(A):
    B = []

    while len(A) > 0:
        m = min(A)
        
        i = A.index(m)

        A.pop(i)
        
        B.append(m)

        print m, A, B

    return B

print ordenar([3, 5, 8, 1, 7, 2])