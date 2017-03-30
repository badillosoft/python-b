alfa = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

def cesar(alfa, palabra, k):
    cpalabra = ""

    for c in palabra:
        i = alfa.index(c)

        cpalabra += alfa[(i + k) % len(alfa)]
        # cpalabra = cpalabra + alfa[(i + k) % len(alfa)]

    return cpalabra

print cesar(alfa, "HOLA MUNDO", 14)
print cesar(alfa, "VBZON HARB", -14)