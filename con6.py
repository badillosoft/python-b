s = 1

a = [s]

for i in range(0, 102):
    if i % 2 == 0:
        s = s + 4
    else:
        s = s - 1
    
    a.append(s)

print "100:", a[100]
print "101:", a[101]