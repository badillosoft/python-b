def foo(a, b):
    c = 123

    print "a:", a
    print "b:", b
    print "c:", c

    return a + b + c

    # c no se imprime
    print c # La funcion ya se regreso

foo(1, 5)

print a, b, c # a, b, c no existen
# fuera de la funcion