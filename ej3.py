x = float(raw_input("Dame x: "))
y = float(raw_input("Dame y: "))

if x >= 0 and y >= 0:
    print "I"

if x < 0 and y >= 0:
    print "II"

if x < 0 and y < 0:
    print "III"

if x >= 0 and y < 0:
    print "IV"

if x >= 0:
    if y >= 0:
        print "I"
    else:
        print "IV"
else:
    if y >= 0:
        print "II"
    else:
        print "III"