from modules.vertice import Vertice
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
    
    def agregarVertice (self,clavecita):
        self.numVertices = self.numVertices +1
        nuevito_vertice = Vertice(clavecita)
        self.listaVertices[clavecita] = nuevito_vertice
        return nuevito_vertice
    
    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.listaVertices
    
    def agregarArista(self,desde,hacia,costo = 0):
        if desde not in self.listaVertices:
            nuevito_vertice = self.agregarVertice(desde)
        if hacia not in self.listaVertices:
            nuevito_vertice = self.agregarVertice(hacia)
        self.listaVertices[desde].agregarVecino(self.listaVertices[hacia],costo)
    
    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __getitem__(self, clave):
        return self.listaVertices[clave] if clave in self.listaVertices else None
             
        