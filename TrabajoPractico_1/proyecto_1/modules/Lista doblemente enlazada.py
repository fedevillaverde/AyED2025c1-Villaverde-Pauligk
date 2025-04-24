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
        return self.__tamano
    
    def insertar(self,item,posicion):

        if posicion == 1:
            self.agregar_al_inicio(item)
        elif type(posicion)!=int or posicion > self.__tamano or posicion < 1:
            raise ValueError("La posicion ingresada no es valida")
        contador = 1
        nuevo=Nodo(item)
        actual=self.__cabeza
        while contador < posicion:
            contador += 1
            actual=actual.siguiente
        previo=actual.anterior
        nuevo.siguiente=actual
        nuevo.anterior=previo
        previo.siguiente=nuevo
        actual.anterior=nuevo
        self.__tamano+=1

    def extraer(self, posicion = None):
        if self.esta_vacia():
            return None
        if posicion == None:
            nodo = self.__cola
            if self.__cabeza == self.__cola:  # solo un nodo
                self.__cabeza = self.__cola = None
            else:
                self.__cola = nodo.anterior
                self.__cola.siguiente = None
            self.__tamano -= 1
            return nodo.dato
        if type(posicion)!=int or posicion > self.__tamano or posicion < 1:
            raise ValueError("La posicion ingresada no es valida")
        
       
        else:
            contador = 1
            actual = self.__cabeza
            while contador <= posicion:
                contador += 1
                actual=actual.siguiente
            previo = actual.anterior
            posterior = actual.siguiente

            previo.siguiente = posterior
            posterior.anterior = previo

            self.tamano -=1
            return


        
    def copiar(self):
        copia = ListaDobleEnlazada()

        actual = self.__cabeza
        contador = 1
        while contador <= self.tamano:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
            contador  += 1

        return copia
    
    def invertir (self):
        cola = self.__cola
        contador = 1
        while contador <= self.tamano:
            self.agregar_al_inicio(cola.dato)
            cola = cola.anterior
            self.extraer()
            contador += 1
    



            
            
        
                
                
            