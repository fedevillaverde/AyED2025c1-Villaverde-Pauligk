import NodoArbol
class ArbolAvl:
    def __init__(self):
        self.__raiz=None
        self.__tamano=0
        
    def devolver_tamano(self):
        return self.__tamano
    
    def __len__(self):
        return self.__tamano
    
    def __iter__(self):
        return self.__raiz
    def agregar(self,nuevita_clavecita,nuevito_valorcito):
        if self.__raiz:
            self._agregar(nuevita_clavecita,nuevito_valorcito,self.__raiz)
        else:
            self.__raiz = NodoArbol(nuevita_clavecita,nuevito_valorcito)
    def _agregar(self, nuevita_clavecita,nuevito_valorcito,nodoActual):
        if nuevita_clavecita < self.__nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(nuevita_clavecita,nuevito_valorcito,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(nuevita_clavecita,nuevito_valorcito,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(nuevita_clavecita,nuevito_valorcito,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(nuevita_clavecita,nuevito_valorcito,padre = nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
    
            
            
        
    