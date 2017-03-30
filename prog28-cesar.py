import sys

# l = [2, 4, 6, 8, 9, 11, 13, 15, 16] 
# print l[1:-1] # [4, 6, 8, 9, 11, 13, 15]
# print l[2:6] # [6, 8, 9, 11]
# print l[::-1] # [16, 15, 13, 11, 9, 8, 6, 4, 2]

texto = " ".join(sys.argv[1:-1])
k = int(sys.argv[-1])

alfa = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

def cesar(alfa, palabra, k):
    cpalabra = ""

    for c in palabra:
        i = alfa.index(c)

        cpalabra += alfa[(i + k) % len(alfa)]
        # cpalabra = cpalabra + alfa[(i + k) % len(alfa)]

    return cpalabra

print cesar(alfa,texto, k)