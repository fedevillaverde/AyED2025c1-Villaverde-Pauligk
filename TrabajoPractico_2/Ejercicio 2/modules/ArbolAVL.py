from modules.NodoArbol import NodoArbol
class ArbolAVL:
    def __init__(self):
        self.__raiz=None
        self.__tamano=0
        
    def devolver_tamano(self):
        return self.__tamano
    
    def __len__(self):
        return self.__tamano


    #Si está vacío el árbol, lo asigna a la raíz. Sino, llama a "_agregar()" 
    def agregar(self,nuevita_clavecita,nuevito_valorcito=None):
        if self.__raiz:
            self._agregar(nuevita_clavecita,nuevito_valorcito,self.__raiz)
        else:
            self.__raiz = NodoArbol(nuevita_clavecita,nuevito_valorcito)
            self.__tamano += 1
            self.__raiz.factorEquilibrio = 0
    #Recorre el árbol hasta colocar el nodo en donde corresponde
    def _agregar(self, nuevita_clavecita,nuevito_valorcito,nodoActual):
        if nuevita_clavecita < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(nuevita_clavecita,nuevito_valorcito,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(nuevita_clavecita,nuevito_valorcito,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
                self.__tamano += 1
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(nuevita_clavecita,nuevito_valorcito,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(nuevita_clavecita,nuevito_valorcito,padre = nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
                self.__tamano += 1
    
    def actualizarEquilibrio(self,nodito: NodoArbol):
        if nodito is None:
            return
        if nodito.factorEquilibrio > 1 or nodito.factorEquilibrio < -1:
            self.reequilibrar(nodito)
            return
        if nodito.padre is not None:
            if nodito.esHijoIzquierdo():
                nodito.padre.factorEquilibrio += 1
            elif nodito.esHijoDerecho():
                nodito.padre.factorEquilibrio -= 1
        if nodito.padre is not None and nodito.padre.factorEquilibrio != 0:
            self.actualizarEquilibrio(nodito.padre)
        
    def rotarIzquierda(self, pivote:NodoArbol):
        nuevaRaiz= pivote.hijoDerecho #cambie hijo izquierdo por hijo derecho pq me parece que no tenia sentido si no.
        if nuevaRaiz is None:
        # No hay nodo para rotar a la izquierda
            return
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
        if nuevaRaiz is None:
        # No hay nodo para rotar a la izquierda
            return
        pivote.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
             nuevaRaiz.hijoDerecho.padre = pivote
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

    def buscar(self, clave): #itera sobre el arbol desde la raiz
        if self.__raiz:
            return self._buscar(clave, self.__raiz)
        else:
            return None      
        
    def _buscar(self, clave, nodito:NodoArbol): #busca y retorna el nodo sin eliminarlo
        if nodito is None:
            return None
        if clave < nodito.clave:
            if nodito.tieneHijoIzquierdo():
                return self._buscar(clave, nodito.hijoIzquierdo)
            else:
                return None
        elif clave > nodito.clave:
            if nodito.tieneHijoDerecho():
                return self._buscar(clave, nodito.hijoDerecho)
            else:
                return None
        else:
            return nodito
        
    def buscar_min(self, clave_min,clave_max): #itera sobre el nodo para buscar
        if self.__raiz:
            nodito = self._buscar_min(self.__raiz, clave_min, clave_max)
            if nodito:
                return nodito.cargaUtil
        
    # def _buscar_min(self, nodito:NodoArbol, clave_min, clave_max):  #devuelve el nodo con la menor carga util en ese rango (espero que asi sea)
    #     if nodito is None:
    #         return None
    #     if nodito.clave < clave_min:
    #         return self._buscar_min(nodito.hijoDerecho,clave_min,clave_max)
    #     if nodito.clave > clave_max:
    #         return self._buscar_min(nodito.hijoIzquierdo,clave_min,clave_max)
    #     posible_menor = self._buscar_min(nodito.hijoIzquierdo,clave_min,clave_max)
    #     return posible_menor if posible_menor else nodito

    def _buscar_min(self, nodito: NodoArbol, clave_min, clave_max):
        if nodito is None:
            return None
        #Realiza una búsqueda recursiva por los hijos izq y der
        menor_izq = self._buscar_min(nodito.hijoIzquierdo, clave_min, clave_max)
        menor_der = self._buscar_min(nodito.hijoDerecho, clave_min, clave_max)

        menorcito = None
        #menorcito es el menor valor de los hijos de un nodo. permance constante hasta que se encuentra otro menor
        if clave_min <= nodito.clave <= clave_max:
            menorcito = nodito

        if menor_izq and (menorcito is None or menor_izq.cargaUtil < menorcito.cargaUtil):
            menorcito = menor_izq

        if menor_der and (menorcito is None or menor_der.cargaUtil < menorcito.cargaUtil):
            menorcito = menor_der

        return menorcito   
    
            
    def buscar_max(self, clave_min, clave_max): #itera sobre el nodo para buscar
        if self.__raiz:
            nodito = self._buscar_max(self.__raiz, clave_min, clave_max)
            if nodito:
                return nodito.cargaUtil
    # def _buscar_max(self, nodito:NodoArbol, clave_min, clave_max): # hace lo mismo que el de arriba pero con el maximo (espero)
    #     if nodito is None:
    #         return None
    #     if nodito.clave < clave_min:
    #         return self._buscar_max(nodito.hijoIzquierdo,clave_min,clave_max)
    #     if nodito.clave > clave_max:
    #         return self._buscar_max(nodito.hijoDerecho, clave_min, clave_max)
    #     posible_mayor = self._buscar_max(nodito.hijoDerecho,clave_min,clave_max)
    #     return posible_mayor if posible_mayor else nodito
    def _buscar_max(self, nodito, clave_min, clave_max): #Mismo mecanismo recursivo que _buscar_min
        if nodito is None:
            return None

        mayor_izq = self._buscar_max(nodito.hijoIzquierdo, clave_min, clave_max)
        mayor_der = self._buscar_max(nodito.hijoDerecho, clave_min, clave_max)

        mayorcito = None
        if clave_min <= nodito.clave <= clave_max:
            mayorcito = nodito

        if mayor_izq and (mayorcito is None or mayor_izq.cargaUtil > mayorcito.cargaUtil):
            mayorcito = mayor_izq

        if mayor_der and (mayorcito is None or mayor_der.cargaUtil > mayorcito.cargaUtil):
            mayorcito = mayor_der

        return mayorcito

    def eliminar(self,clave): #itera sobre un nodo desde la raiz
        if self.__raiz:
            return self._eliminar(self.__raiz, clave)
        
    def _minimo(self,nodito:NodoArbol): #encuentra el minimo en un arbol o un sub-arbol
        actual = nodito
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual
        
    def _eliminar(self, nodito: NodoArbol, clave):
        if nodito is None:
            return None
        if clave < nodito.clave:
            nodito.hijoIzquierdo = self._eliminar(nodito.hijoIzquierdo, clave)
            if nodito.hijoIzquierdo:
                nodito.hijoIzquierdo.padre = nodito
        elif clave > nodito.clave:
            nodito.hijoDerecho = self._eliminar(nodito.hijoDerecho, clave)
            if nodito.hijoDerecho:
                nodito.hijoDerecho.padre = nodito
        else:
            if not nodito.hijoIzquierdo and not nodito.hijoDerecho:
                self.__tamano -= 1
                return None
            elif not nodito.hijoIzquierdo:
                self.__tamano -= 1
                nodito.hijoDerecho.padre = nodito.padre
                return nodito.hijoDerecho
            elif not nodito.hijoDerecho:
                self.__tamano -= 1
                nodito.hijoIzquierdo.padre = nodito.padre
                return nodito.hijoIzquierdo
            else:
                sucesor = self._minimo(nodito.hijoDerecho)
                nodito.clave = sucesor.clave
                nodito.cargaUtil = sucesor.cargaUtil
                nodito.hijoDerecho = self._eliminar(nodito.hijoDerecho, sucesor.clave)
                if nodito.hijoDerecho:
                    nodito.hijoDerecho.padre = nodito
        self.reequilibrar(nodito)
        return nodito

    def extraer(self, clave): #utilizando eliminar, muestra un nodo para despues eliminarlo
        if self.__raiz:
            nodito = self._buscar(clave, self.__raiz)
            if nodito:
                self.eliminar(clave)
                return nodito         
        else:
            return None
    def buscar_rango(self, clave1, clave2): #itera sorbe el arbol desde la raiz para buscar un rango de claves
        if clave1 > clave2:
            raise ValueError("clave 1 debe ser menor o igual a clave 2")
        if self.__raiz:
            return self._buscar_rango(self.__raiz,clave1,clave2)
    
    def _buscar_rango(self,nodito : NodoArbol, clave1, clave2): #utilizando la iteracion de arriba, busca y crea una listita con los valores que encuentre.
        if nodito is None:
            return []
        if nodito.clave < clave1:
            return self._buscar_rango(nodito.hijoDerecho, clave1, clave2)
        elif nodito.clave > clave2:
            return self._buscar_rango(nodito.hijoIzquierdo, clave1, clave2)
        else:
            resultadito = []
            if nodito.tieneHijoIzquierdo():
                resultadito.extend(self._buscar_rango(nodito.hijoIzquierdo, clave1, clave2))
            resultadito.append(nodito)
            if nodito.tieneHijoDerecho():
                resultadito.extend(self._buscar_rango(nodito.hijoDerecho, clave1, clave2))
            return resultadito
            
    
    
    



    


        
                
    
        
            
            
            