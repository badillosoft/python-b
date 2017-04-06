import facli

clientes = [
    {
        "nombre": "Ana B.",
        "email": "ana@correo.com",
        "direccion": "Av. Boulevard 123 Edif. A 12",
        "telefonos": "5512345678"
    }
]

def ver_clientes():
    pos = 1
    for cliente in clientes:
        print pos, cliente["nombre"], cliente["email"]
        pos += 1

def agregar_cliente():
    nombre = raw_input("Nombre completo: ")
    email = raw_input("Correo: ")

    clientes.append({
        "nombre": nombre,
        "email": email
    })


facli.ver_clientes = ver_clientes
facli.agregar_cliente = agregar_cliente

facli.menu_principal()