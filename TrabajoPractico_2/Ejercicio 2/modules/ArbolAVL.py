class ArbolAvl:
    def __init__(self):
        self.__raiz=None
        self.__tamano=0
        
    def devolver_tamano(self):
        return self.__tamano
    
    def __len__(self):
        return self.__tamano
    
    def __iter__(self):
        return self.__raiz.__iter__()
    
    