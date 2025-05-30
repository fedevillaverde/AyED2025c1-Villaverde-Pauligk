class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = 0
        self.predecesor = None
    
    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion
        
    def __str__(self):
        return str(self.id) + 'conectadoA' + str([x.id for x in self.conectadoA])
    
    def obtenerConexiones (self):
        return self.conectadoA.keys()
    
    def obtenerId(self):
        return self.id
    
    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]
    
    def asignarDistancia(self,nuevita_distancia):
        self.distancia = nuevita_distancia
    
    def obtenerDistancia(self):
        return self.distancia
    
    def asignarPredecesor(self,nuevito_papa):
        self.predecesor = nuevito_papa
        
    def obtenerPredecesor(self):
        return self.predecesor
    

    