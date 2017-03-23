a = 1
b = 3
c = 8
d = 5

x = float(raw_input("Dame x: "))
y = float(raw_input("Dame y: "))

if x >= a and x <= c and y >= b and y <= d:
    print "Dentro"
else:
    print "Afuera"

if x >= a and x <= c:
    if y >= b and y <= d:
        print "Dentro"
    else:
        print "Afuera"
else:
    print "Afuera"

PX = x >= a and x <= c
PY = y >= b and y <= d

if PX and PY:
    print "Adentro"
else:
    print "Afuera"