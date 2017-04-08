ana = {
    "nombre": "Ana B.",
    "sexo": "Mujer",
    "correo": "ana@gmail.com",
    "telefonos": ["1234567890", "0987654321", "(044)"],
    "direccion": {
        "calle": "Av. ABC",
        "ext": 501,
        "int": 7,
        "colonia": "Juarez",
        "municipio": "CDMX",
        "estado": "CDMX"
    }
}

pepe = {
    "nombre": "Pepe P.",
    "sexo": "Hobre",
    "correo": "pepe@hotmail.com",
    "telefonos": [],
    "direccion": {
        "calle": "Av. DEF",
        "ext": 1231,
        "int": 23,
        "colonia": "Obrera",
        "municipio": "Tulancingo",
        "estado": "Hidalgo"
    }
}

personas = [ana, pepe, "Hola mundo"]

print personas[0]["direccion"]["colonia"]