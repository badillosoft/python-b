def prim_ult(lista):
    p = lista[0]
    u = lista[-1]

    return (p, u)

p1, u1 = prim_ult([1, 2, 3, 4, 5, 6])
print p1, u1

p2, u2 = prim_ult([4, 3, 2, 1])
print p2, u2