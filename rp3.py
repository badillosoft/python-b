def min_max(A):
    m = A[0]
    M = A[0]

    for x in A:
        if x < m:
            m = x

        if x > M:
            M = x

    return (m, M)

print min_max([8, 5, 1, 2, 7, 3, 5, 8, 6, 3])
print min_max([2, -100, 9, 20, 5])
print min_max(range(100, 200))