# Una cadena de ADN puede ser codificada mediante sus
# bases nitrogenadas A (adenina) G (guanina)
# C (citosina) T (tiamina)
# Por ejemplo: AGCTCATCAGCTACGTTGCGA

# Un gen se expresa como una subcadena codificada, y el ADN
# posee dicho gen en su informacion si contiene dicha subcadena
# Por ejemplo: TCATC

# Se requiere un programa que dada una subcadena con los
# simbolos codificados A, C, G, T para un gen dada, diga
# si una cadena de ADN codificada posee dicha subcadena
# Ejemplo: AGCTCATCAGCTACGTTGCGA contine TCATC
# Ejemplo: AGCTCATCAGCTACGTTGCGA no contine AACC

def contiene(adn, gen):
    n = len(gen)
    m = len(adn)
    a = 0 # posicion inicial donde empiezo a comparar
    while a < m - n:
        # 1. Comparar los siguientes n caracteres
        # de adn empezando en a
        encontrado = True
        for i in range(0, n):
            if adn[a + i] != gen[i]:
                encontrado = False
        if encontrado:
            return (True, a)
        
        a += 1
    return False

print contiene("AGCTCATCAGCTACGTTGCGA", "CCTAC")