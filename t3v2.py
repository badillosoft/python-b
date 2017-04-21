def contiene(adn, gen):
    n = len(gen)
    m = len(adn)
    b = m - n # el ultimo indice que contine n carecteres
    encontrados = []
    for i in range(0, b + 1):
        sub = ""
        # llena sub con los siguientes n carecteres
        # de adn partiendo de la posicion i
        for j in range(0, n):
            sub += adn[i + j]
        print sub, sub == gen
        if sub == gen:
            encontrados.append(i)
    return encontrados

print contiene("ACCTGCGTAGTGCGTAGC", "TCG")

print contiene("la leche lala contiene lactosa", "a")