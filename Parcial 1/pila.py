
class Pila(object):
    
    def __init__(self):
        self.__elementos = []

    def apilar(self, dato):
        self.__elementos.append(dato)

    def desapilar(self):
        return self.__elementos.pop()
    
    def pila_vacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)

    def elemento_cima(self):
        return self.__elementos[-1]
    
    def barrido_pila(self):
        aux = Pila()

        while not self.pila_vacia():
            num = self.desapilar()
            print(num)
            aux.apilar(num)

        while not aux.pila_vacia():
            self.apilar(aux.desapilar())
