# Tuplas son listas fijas que no pueden agregar
# quitar o modificar valores.

# Propiedades:
# * Pueden ser iteradas en un ciclo for-in
# * Empaquetan exactamente tantos datos como
# se definan en su creacion
# * Las tuplas deben contener al menos 2 elementos
# * Las tuplas se desempaquetan en exactamente
# tantas variables como datos haya empaquetado

p = (-1, 8, 4)

x, y, z = p

print p
print x, y, z

x, y, z = p
p = (x / 2., y + 1, z ** 2)

print p