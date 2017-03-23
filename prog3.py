a = int(raw_input("Dame a: "))
b = int(raw_input("Dame b: "))
c = int(raw_input("Dame c: "))

print a, b, c

if a < b:
    # a < b
    if c < a:
        # c < a < b
        print c, a, b
    else:
        # a < c
        if b < c:
            # a < b < c:
            print a, b, c
        else:
            # a < c < b
            print a, c, b
else:
    # b < a
    if c < b:
        # c < b < a
        print c, b, a
    else:
        # b < a, b < c ? c < a o a < c
        if c < a:
            # b < c < a
            print b, c, a
        else:
            # b < a < c
            print b, a, c