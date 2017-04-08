import os

directorio = os.getcwd()

print directorio

# Crear una carpeta en el directorio actual

# os.system("mkdir hola")

try:
    os.mkdir("hola")
    print "La carpeta 'hola' fue creada"
except:
    print "El directorio 'hola' ya existe"