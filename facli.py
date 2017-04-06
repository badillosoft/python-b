import time

def menu(nombre, opciones):
    print "\x1bc", nombre

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
        return menu(nombre, opciones)

    return r

def menu_clientes():
    
    opc = menu("Clientes", [
        "Ver todos",
        "Buscar",
        "Agregar",
        "Actualizar",
        "Eliminar",
        "Regresar"
    ])

    if opc == 1:
        ver_clientes()
    elif opc == 2:
        buscar_cliente()
    elif opc == 3:
        agregar_cliente()
    elif opc == 4:
        actualizar_cliente()
    elif opc == 5:
        eliminar_cliente()
    elif opc == 6:
        menu_principal()
        return

    raw_input()
    menu_clientes()

def menu_principal():
    opc = menu("Inicio", ["Clientes", "Facturas", "Salir"])

    if opc == 1:
        menu_clientes()
    elif opc == 3:
        print "Hasta luego"