
# ejercicio 1:

# A 


# def barridoRecursivo(vector):
#     if(len(vector)>0):
#         return   print(vector[-1])
#     else:
#         return barridoRecursivo(vector[1:])


# lista = ['yoda','luke','leila','obiwan']

# barridoRecursivo(lista)




# Ejercicio 2:

from cola import Cola
from pila import Pila

# class notificacion(object):
#         def __init__(self,hora,aplicacion,mensaje):
#             self.hora = hora
#             self.aplicacion = aplicacion
#             self.mensaje = mensaje

#         def __str__(self):
#             return self.hora+' - '+self.aplicacion+' - '+self.mensaje



# cola_notificacion = Cola()
# cola_twit = Cola()
# pila_aux = Pila()


# lista_notificaicones = [
                        
#                         notificacion('23:40','whatsapp','que haces?'),
#                         notificacion('12:00','twitter','python es lo mejor'),
#                         notificacion('5:00','instagram','que tul?'),
#                         notificacion('11:32','facebook','hola'),
#                         notificacion('2:00','twitter','lo mejor de python'),
#                         notificacion('4:40','facebook','adios'),
#                         notificacion('3:50','instagram','que suerte'),
# ]


# for i in lista_notificaicones:
#     cola_notificacion.arribo(i)

# # A:

# cantida_elementos = 0
# while cantida_elementos < cola_notificacion.tamanio():
#         cola_notificacion.mover_final()
#         x = cola_notificacion.en_frente()
#         if x.aplicacion == 'facebook':
#                 cola_notificacion.atencion()     
#         cantida_elementos += 1

# cola_notificacion.barrido_cola()

# print()

# # B:

# cantida_elementos = 0
# while cantida_elementos < cola_notificacion.tamanio():
#         x = cola_notificacion.mover_final()
#         if x.aplicacion == 'twitter' and 'python' in x.mensaje :
#                      cola_twit.arribo(x)
#         cantida_elementos += 1


# cola_twit.barrido_cola()

# print()
# # C:

# cantida_elementos = 0
# while cantida_elementos < cola_notificacion.tamanio():
#         x = cola_notificacion.mover_final()
#         if x.aplicacion == 'instagram':
#                      pila_aux.apilar(x)
#         cantida_elementos += 1

# pila_aux.barrido_pila()




# Ejercico 3:

from lista import Lista


lista_personajes = Lista()
lista_aux = Lista()

lista = ['gamora','thor','antman','iron man','sacalet witch','capitan america']


for i in lista:
    lista_personajes.insertar(i)

# A:
if lista_personajes.busqueda('thor'):
    print(lista_personajes.busqueda('thor'))

print()

# B:
lista_personajes.modificar_elemento(4,'scarlet witch')
lista_personajes.barrido()

print()
# C:

lista_secundaria = ['hulk','black widow','rocket','loki']

for i in lista_secundaria:
    lista_personajes.insertar(i)

lista_personajes.barrido()

print()
# D:


# E:

print(lista_personajes.obtener_elemento(7))
print()
# F:

for i in range(lista_personajes.tamanio()):
    heroe = lista_personajes.obtener_elemento(i)

    if heroe[0] in ["c", "s"]:
        lista_aux.insertar(heroe)
lista_aux.barrido()


# G:
print()
print()
list_personajes_2 = Lista()


personajes_marvel = [
    {"nombre" : "iron man", "año" : 1998,'tipo': True },
    {"nombre" : "scarlet witch", "año" : 1960,'tipo': True  },
    {"nombre" : "hulk", "año" : 1970,'tipo': True  },
    {"nombre" : "capitan america", "año" : 1955,'tipo': True  },
    {"nombre" : "craneo rojo", "año" : 1955,'tipo': False  },
    {"nombre" : "rhino", "año" : 1980,'tipo': False  },
    {"nombre" : "thanos", "año" : 1919,'tipo': False }
]


for i in personajes_marvel:
    list_personajes_2.insertar(i, 'nombre')

list_personajes_2.barrido()

print()

list_personajes_2.ordenar('año')

list_personajes_2.barrido()