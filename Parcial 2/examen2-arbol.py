from arbol_binario import Arbol

# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:



# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);

Dinosaurios = [
    {'nombre' : 'estegosaurrio', 'codigo' : 792, 'ubicacion' : '6B'},
    {'nombre' : 't-rex', 'codigo' : 23424, 'ubicacion' : '7A'},
    {'nombre' : 't-rex', 'codigo' : 44422, 'ubicacion' : '7A'},
    {'nombre' : 't-rex', 'codigo' : 22323, 'ubicacion' : '7A'},
    {'nombre' : 'raptor', 'codigo' : 26789, 'ubicacion' : '4C'},
    {'nombre' : 'raptor', 'codigo' : 11119, 'ubicacion' : '7C'},
    {'nombre' : 'diplodocus', 'codigo' : 89324, 'ubicacion' : '7D'},
    {'nombre' : 'diplodocus', 'codigo' : 22211, 'ubicacion' : '7D'},
    {'nombre' : 'diplodocus', 'codigo' : 32132, 'ubicacion' : '7D'},
    {'nombre' : 'sgimoloch', 'codigo' : 33342, 'ubicacion' : '9D'},
]

arbolNombre = Arbol()

arbolCodigo = Arbol()


# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;

for nom in Dinosaurios:
    arbolNombre.insertar_nodo(nom['nombre'],nom)

for cod in Dinosaurios:
    arbolCodigo.insertar_nodo(cod['codigo'],cod)

# 3. realizar un barrido en orden del árbol ordenado por nombre;    

# arbolNombre.inorden()

# 4. mostrar toda la información del dinosaurio 792;

# pos = arbolCodigo.busqueda(792)
# print(pos.datos)

# 5. mostrar toda la información de todos los T-Rex que hay en la isla;

# def contar_dinosaurio(arbol : Arbol):
#     if (arbol.info is not None):
#         if (arbol.izq is not None):
#             contar_dinosaurio(arbol.izq)
#         if arbol.datos['nombre'] == 't-rex':
#             print(arbol.datos)
#         if (arbol.der is not None):
#             contar_dinosaurio(arbol.der)

# contar_dinosaurio(arbolNombre)


# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;


# def remplazar_proximidad(arbol : Arbol, clave, remplazar):
#         if(arbol.info is not None):
#             if(arbol.izq is not None):
#                 remplazar_proximidad(arbol.izq,clave, remplazar)
#             if(arbol.info[0:len(clave)] == clave):
#                 arbol.info = remplazar
#                 arbol.datos['nombre'] = remplazar
#             if(arbol.der is not None):
#                 remplazar_proximidad(arbol.der, clave, remplazar)

# remplazar_proximidad(arbolNombre,'sgimoloch', 'stygimoloch')
# remplazar_proximidad(arbolCodigo,'sgimoloch', 'stygimoloch')

# arbolNombre.inorden()
# print()
# arbolCodigo.inorden()

# 7. mostrar la ubicación de todos los Raptores que hay en la isla;

# def mostrar_dinosaurio(arbol : Arbol):
#     if (arbol.info is not None):
#         if (arbol.izq is not None):
#             mostrar_dinosaurio(arbol.izq)
#         if arbol.datos['nombre'] == 'raptor':
#             print('raptor')
#             print(arbol.datos['ubicacion'])
#         if (arbol.der is not None):
#             mostrar_dinosaurio(arbol.der)

# mostrar_dinosaurio(arbolNombre)

# 8. contar cuantos Diplodocus hay en el parque;

# print(arbolNombre.contar_ocurrencias('diplodocus'))


# 9. debe cargar al menos 15 elementos.

Dinosaurios2 = [
    {'nombre' : 'estegosaurrio', 'codigo' : 10202, 'ubicacion' : '6B'},
    {'nombre' : 't-rex', 'codigo' : 99999, 'ubicacion' : '7A'},
    {'nombre' : 't-rex', 'codigo' : 29251, 'ubicacion' : '7A'},
    {'nombre' : 't-rex', 'codigo' : 19261, 'ubicacion' : '7A'},
    {'nombre' : 'raptor', 'codigo' : 19082, 'ubicacion' : '4C'},
    {'nombre' : 'raptor', 'codigo' : 12877, 'ubicacion' : '7C'},
    {'nombre' : 'diplodocus', 'codigo' : 76589, 'ubicacion' : '7D'},
    {'nombre' : 'diplodocus', 'codigo' : 98567, 'ubicacion' : '7D'},
    {'nombre' : 'diplodocus', 'codigo' : 12347, 'ubicacion' : '7D'},
    {'nombre' : 'sgimoloch', 'codigo' : 10101, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 12300, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 43200, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 12220, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 12222, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 11100, 'ubicacion' : '9D'},
    {'nombre' : 'sgimoloch', 'codigo' : 12300, 'ubicacion' : '9D'},
]

for nom in Dinosaurios2:
    arbolNombre.insertar_nodo(nom['nombre'],nom)

for cod in Dinosaurios2:
    arbolCodigo.insertar_nodo(cod['codigo'],cod)
