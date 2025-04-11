from modules.Nodos import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza=None
        self.__cola=None
        self.__tamano=0
        
    def esta_vacia(self):
       return (self.__cabeza==None and self.__cola==None)
   
    def agregar_al_inicio(self,item):
        temp=Nodo(item)
        if self.__cabeza is None and self.__cola is None:
            self.__cabeza=temp
            self.__cola=temp
            self.__tamano+=1
        else:
            temp.siguiente=self.__cabeza
            self.__cabeza.anterior=temp
            self.__cabeza=temp
            self.__tamano+=1
    
    def agregar_al_final(self,item):
        temp=Nodo(item)
        if self.__cola is None and self.__cabeza is None:
            self.__cola=temp
            self.__cabeza=temp
            self.__tamano += 1  
        else:
            temp.anterior=self.__cola
            self.__cola.siguiente=temp
            self.__cola=temp
            self.__tamano += 1
            
    @property
    def tamano(self):
        return self.__tamano
        
    def __len__(self):
        return self.tamano
    
    def insertar(self,item,posicion):
        if type(posicion)!=int or posicion > self.__tamano or posicion < 1:
            raise ValueError("La posicion ingresada no es valida")
        contador = 1
        nuevo=Nodo(item)
        actual=self.__cabeza
        while contador != posicion:
            contador += 1
            actual=actual.siguiente
        previo=actual.anterior
        nuevo.siguiente=actual
        nuevo.anterior=previo
        previo.siguiente=nuevo
        actual.anterior=nuevo
        self.__tamano+=1
    
        
                
                
            