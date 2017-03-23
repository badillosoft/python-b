# edad en [1, 5)
edad = int(raw_input("Dame edad: "))

if edad >= 1 and edad < 5:
    print "edad en [1, 5)"

# x en (-2, 6)
x = int(raw_input("Dame x: "))

if x > -2 and x < 6:
    print "x en (-2, 6)"

# y no en (-8, 17]
y = int(raw_input("Dame y: "))

if y <= -8 or y > 17:
    print "y no en (-8, 17]"

if not (y > -8 and y <= 17):
    print "y no en (-8, 17]"