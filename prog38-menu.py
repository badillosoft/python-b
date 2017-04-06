import time

def menu(nombre, opciones): # MOD
    print "\x1bc", nombre # MOD

    for i in range(0, len(opciones)):
        print "%d. %s" %(i + 1, opciones[i])

    print

    try:
        r = int(raw_input("> "))
    except:
        r = 0

    if r <= 0 or r > len(opciones):
        print "La opcion no esta en el menu"
        time.sleep(1)
        return menu(nombre, opciones) # MOD

    return r

def menu_clientes():
    opc = menu("Clientes", [
        "Ver todos",
        "Buscar",
        "Actualizar",
        "Eliminar",
        "Regresar"
    ])

    if opc == 5:
        menu_principal()

def menu_principal():
    opc = menu("Inicio", ["Clientes", "Facturas", "Salir"])

    if opc == 1:
        menu_clientes()
    elif opc == 3:
        print "Hasta luego"

menu_principal()