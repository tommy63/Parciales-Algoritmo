

class Cola(object):

    def __init__(self):
        self.__elementos = []
    
    def arribo(self, dato):
        self.__elementos.append(dato)
    
    def atencion(self):
        return self.__elementos.pop(0)
    
    def cola_vacia(self):
        return len(self.__elementos) == 0
    
    def en_frente(self):
        return self.__elementos[0]
    
    def mover_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato
    
    def tamanio(self):
        return len(self.__elementos)
    
    def barrido_cola(self):
        aux = Cola()

        while not self.cola_vacia():
            num = self.atencion()
            print(num)
            aux.arribo(num)

        while not aux.cola_vacia():
            self.arribo(aux.atencion())
