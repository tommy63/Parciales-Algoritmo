from grafo import Grafo


# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:


# 6. debe utilizar un grafo no dirigido.
grafoConexion = Grafo(dirigido=False)


# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook,
# servidor, router, switch, impresora;


conexion = [
    {'nombre': 'manjaro', 'tipo': 'pc'},
    {'nombre': 'parrot', 'tipo': 'pc'},
    {'nombre':'fedora','tipo':'pc'},
    {'nombre':'mint','tipo':'pc'},
    {'nombre':'ubuntu','tipo':'pc'},
    {'nombre':'red hat','tipo':'notbook'},
    {'nombre':'debian','tipo':'notbook'},
    {'nombre':'arch','tipo':'notbook'},
    {'nombre':'impresora','tipo':'impresora'},
    {'nombre':'guarani','tipo':'servidor'},
    {'nombre':'mongoDB','tipo':'servidor'},
    {'nombre':'switch1','tipo':'switch'},
    {'nombre':'switch2','tipo':'switch'},
    {'nombre':'router1','tipo':'router'},
    {'nombre':'router2','tipo':'router'},
    {'nombre':'router3','tipo':'router'},
]

for con in conexion:
    grafoConexion.insertar_vertice(con["nombre"], data=con)

grafoConexion.insertar_arista(40,'manjaro','switch2')
grafoConexion.insertar_arista(12,'parrot','switch2')
grafoConexion.insertar_arista(2,'mongoDB','switch2')
grafoConexion.insertar_arista(56,'arch','switch2')
grafoConexion.insertar_arista(3,'fedora','switch2')
grafoConexion.insertar_arista(61,'router3','switch2')
grafoConexion.insertar_arista(43,'router1','router3')
grafoConexion.insertar_arista(50,'router2','router3')
grafoConexion.insertar_arista(37,'router2','router1')
grafoConexion.insertar_arista(9,'router2','guarani')
grafoConexion.insertar_arista(25,'router2','red hat')
grafoConexion.insertar_arista(29,'router1','switch1')
grafoConexion.insertar_arista(17,'switch1','debian')
grafoConexion.insertar_arista(18,'switch1','ubuntu')
grafoConexion.insertar_arista(22,'switch1','impresora')
grafoConexion.insertar_arista(80,'switch1','mint')


# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;

# ver_origen1 = grafoConexion.buscar_vertice('red hat')
# grafoConexion.barrido_amplitud(ver_origen1)
# grafoConexion.barrido_profundidad(ver_origen1)

# ver_origen2 = grafoConexion.buscar_vertice('debian')
# grafoConexion.barrido_amplitud(ver_origen2)
# grafoConexion.barrido_profundidad(ver_origen2)

# ver_origen3 = grafoConexion.buscar_vertice('arch')
# grafoConexion.barrido_amplitud(ver_origen3)
# grafoConexion.barrido_profundidad(ver_origen3)


# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;

# def camino_pc(origen, destino):

#     ver_origen = grafoConexion.buscar_vertice(origen)
#     ver_destino = grafoConexion.buscar_vertice(destino)
#     costo = None
    
#     if ver_origen != -1 and ver_destino != -1:
#         camino = grafoConexion.dijkstra(ver_origen)
        
#         while(not camino.pila_vacia()):
#             dato = camino.desapilar()
#             if(dato[1][0] == destino):
#                 if(costo is None):
#                     costo = dato[0]
#                 print('el camino mas corto desde: ', origen,'hasta: ',destino)
                        
#         print('costo total: ', costo)

# camino_pc('debian','mongoDB')
# camino_pc('red hat','mongoDB')


# 4. encontrar el árbol de expansión mínima;

# print(grafoConexion.prim(0))

# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;

# grafoConexion.barrido_profundidad(0)
# print()
# grafoConexion.eliminar_vertice('impresora')
# print()
# grafoConexion.barrido_profundidad(0)



