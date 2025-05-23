from modules.NodoArbol import NodoArbol
class ArbolAVL:
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
    
    def actualizarEquilibrio(self,nodito: NodoArbol):
        if nodito.factorEquilibrio > 1 or nodito.factorEquilibrio < -1:
            self.reequilibrar(nodito)
            return
        if nodito.padre != None:
            if nodito.esHijoIzquierdo():
                nodito.padre.factorEquilibrio += 1
            elif nodito.esHijoDerecho():
                nodito.padre.factorEquilibrio -= 1
        if nodito.padre.factorEquilibrio != 0:
            self.actualizarEquilibrio(nodito.padre)
        
    def rotarIzquierda(self, pivote:NodoArbol):
        nuevaRaiz= pivote.hijoIzquierdo
        pivote.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = pivote
        nuevaRaiz.padre = pivote.padre
        if pivote.esRaiz():
            self.__raiz = nuevaRaiz
        else:
            if pivote.esHijoIzquierdo():
                pivote.padre.hijoIzquierdo = nuevaRaiz
            else:
                pivote.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = pivote
        pivote.padre = nuevaRaiz
        pivote.factorEquilibrio = pivote.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio , 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 +max(pivote.factorEquilibrio, 0)
        
    def rotarDerecha(self, pivote: NodoArbol):
        nuevaRaiz = pivote.hijoIzquierdo
        pivote.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
             nuevaRaiz.hijoDerecho.pandre = pivote
        nuevaRaiz.padre = pivote.padre
        if pivote.esRaiz():
            self.__raiz = nuevaRaiz
        else:
            if pivote.esHijoIzquierdo():
                pivote.padre.hijoIzquierdo = nuevaRaiz
            else:
                pivote.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoDerecho = pivote
        pivote.padre = nuevaRaiz
        pivote.factorEquilibrio = pivote.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio , 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 +max(pivote.factorEquilibrio, 0)
        
    def reequilibrar (self, nodito: NodoArbol):
        if nodito.factorEquilibrio < 0:
            if nodito.hijoDerecho.factorEquilibrio>0:
                self.rotarDerecha(nodito.hijoDerecho)
                self.rotarIzquierda(nodito)
                
            else:
                self.rotarIzquierda(nodito)
        elif nodito.factorEquilibrio > 0:
            if nodito.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodito.hijoIzquierdo)
                self.rotarDerecha(nodito)
            else:
                self.rotarDerecha(nodito)
                
    
        
            
            
            