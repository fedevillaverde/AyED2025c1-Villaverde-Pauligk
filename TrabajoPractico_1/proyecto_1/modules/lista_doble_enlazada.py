from modules.Nodos import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza=None
        self.__cola=None
        self.__tamano=0
    @property
    def cabeza(self):
        return self.__cabeza
    @cabeza.setter
    def cabeza(self,nuevita_cabecita):
        self.__cabeza=nuevita_cabecita
        
    @property
    def cola(self):
        return self.__cola
    @cola.setter
    def cola(self,nuevita_colita):
        self.__cola=nuevita_colita
        
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
    
    def insertar(self,item,posicion=-1):
        if posicion==0:
            self.agregar_al_inicio(item)

            
        elif posicion == -1:
            self.agregar_al_final(item)
           
            return 
        elif type(posicion)!=int or posicion > self.__tamano or posicion < 0:
            raise ValueError("La posicion ingresada no es valida")
        else:
            contador = 0
            nuevo=Nodo(item)
            actual=self.__cabeza
            while contador < posicion:
                contador += 1
                actual=actual.siguiente
            izq=actual.anterior
            nuevo.anterior=izq
            izq.siguiente=nuevo
            der=actual
            nuevo.siguiente=der
            der.anterior=nuevo
            
            
            self.__tamano+=1

    def extraer(self, posicion = None):
        if posicion == 0:
            temp = self.__cabeza
            if self.__cabeza == self.__cola:  # solo un nodo
                self.__cabeza = self.__cola = None
            else:
                self.__cabeza = self.__cabeza.siguiente
                self.__cabeza.anterior = None
            self.__tamano -= 1
            return temp.dato
        if self.esta_vacia():
            raise ValueError("La lista está vacía")
        if posicion == None or posicion==-1 or posicion == self.__tamano -1:
            nodo = self.__cola
            if self.__cabeza == self.__cola:  # solo un nodo
                self.__cabeza = self.__cola = None
            else:
                self.__cola = nodo.anterior
                self.__cola.siguiente = None
            self.__tamano -= 1
            return nodo.dato
        if type(posicion)!=int or posicion > self.__tamano or posicion < 0:
            raise ValueError("La posicion ingresada no es valida")
        else:
            contador = 0
            actual = self.__cabeza
            while contador < posicion:
                contador += 1
                actual=actual.siguiente
            previo = actual.anterior
            posterior = actual.siguiente

            previo.siguiente = posterior
            posterior.anterior = previo

            self.__tamano -=1
            return actual.dato


        
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
        datos = []
        actual = self.__cola
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.anterior

        while self.__cabeza is not None:
            self.extraer()  # suponiendo que esto elimina de la cabeza o cola

        for dato in datos:
            self.agregar_al_final(dato)  # o al inicio, según el orden que querés
        
            

        
    
    # def concatenar(self, lista):
    #     if self.esta_vacia() and lista.esta_vacia():
    #         return None
        
    #     elif self.esta_vacia() and not lista.esta_vacia():
    #         self.__cabeza = lista.__cabeza
    #         self.__cola = lista.__cola
    #         self.__tamano = lista.tamano
    #         self.__cabeza.anterior = None

    #         return self
    #     elif not self.esta_vacia() and lista.esta_vacia():
    #         return self
    #     else:
    #         self.__cola.siguiente = lista.__cabeza
    #         lista.__cabeza.anterior = self.__cola
    #         self.__cola = lista.__cola
    #         self.__tamano += lista.tamano
    #         return self

    def concatenar(self, lista):
        if self.esta_vacia() and lista.esta_vacia():
            return None
        lista_copia = lista.copiar()  # Asumimos que tenemos un método copiar()
        if self.esta_vacia():
            self.__cabeza = lista_copia.__cabeza
            self.__cola = lista_copia.__cola
            self.__tamano = lista_copia.__tamano
            return self
        elif lista.esta_vacia():
            return self
        else:
            self.__cola.siguiente = lista_copia.__cabeza
            lista_copia.__cabeza.anterior = self.__cola
            self.__cola = lista_copia.__cola
            self.__tamano += lista_copia.__tamano
            return self
    
    def __add__(self, lista):
        if type(lista)==ListaDobleEnlazada:
            nueva_lista=ListaDobleEnlazada()
            nueva_lista.concatenar(self)
            nueva_lista.concatenar(lista)
            return nueva_lista
        else:
            raise TypeError("La lista debe ser una lista doblemente enlazada :c")
        
        
    def __iter__(self):
        actual=self.__cabeza
        while actual is not None:
            yield actual.dato
            actual=actual.siguiente
    # def __str__(self):
        
    
    
        
            
        
        
if __name__=='__main__':
    l1=ListaDobleEnlazada()
    l2=ListaDobleEnlazada()
    l3=ListaDobleEnlazada()
    for i in range(10):
        l1.agregar_al_final(i)
        l2.agregar_al_final(i)
    for l in l1:
        print(l)
    len(l1)
    
    for l in l1:
        print(l)
    l1.invertir()
    print("invertida?") 
    for l in l1:
        print(l)
    print('-----------------------------')
    
    
    
            
    



            
            
        
                
                
              