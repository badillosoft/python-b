# Condicionales en cascada

masa = float(raw_input("Dame el peso: "))
estatura = float(raw_input("Dame la estatura: "))

# Prioridad peradores
# Izquierda a derecha
# ()
# **
# * /
# + - %

IMC = masa / (estatura ** 2)

print "IMC:", IMC

if IMC < 18.5:
    print "Bajo de peso"
elif IMC >= 18.5 and IMC < 25:
    print "Peso normal"
elif IMC < 30:
    print "Sobrepeso"
else:
    print "Obesidad"

