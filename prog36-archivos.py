import random

def password(n):
    alfabeto = list("0123456789abcdefABCDEF")

    p = ""

    for i in range(0, n):
        p += random.choice(alfabeto)

    return p

f = open("passwords.txt", "w")

for i in range(0, 100000):
    f.write(password(12))
    f.write(" ")

f.close()