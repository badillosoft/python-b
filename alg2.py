def ult2(L, x):
    for s in range(1, len(L)):
        if x <= L[s]:
            return (s - 1, s)
    return (s - 1, s)

L = [1, 5, 8, 20]

print ult2(L, -1) == (0, 1)
print ult2(L, 3) == (0, 1)
print ult2(L, 6) == (1, 2)
print ult2(L, 8) == (1, 2)
print ult2(L, 15) == (2, 3)
print ult2(L, 20) == (2, 3)
print ult2(L, 50) == (2, 3)