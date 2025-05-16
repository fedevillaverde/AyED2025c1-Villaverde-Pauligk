class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.__clave = clave
        self.__cargaUtil=valor
        self.__hijoIzquierdo=izquierdo
        self.__hijoDerecho=derecho
        self.__padre=padre
        self.__factorEquilibrio = 0
    @property
    def clave(self):
        return self.__clave
    @property
    def cargaUtil(self):
        return self.__cargaUtil
    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo
    @property
    def hijoDerecho(self):
        return self.__hijoDerecho
    @property
    def padre(self):
        return self.__padre
    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio
    @factorEquilibrio.setter
    def factorEquilibrio(self,nuevito_valorcito):
        self.__factorEquilibrio = nuevito_valorcito
    @hijoIzquierdo.setter
    def hijoIzquierdo(self,hijoIzquierdo):
        self.__hijoIzquierdo=hijoIzquierdo
    @hijoDerecho.setter
    def hijoDerecho(self,hijoDerecho):
        self.__hijoDerecho=hijoDerecho
    @padre.setter
    def padre(self,padre):
        self.__padre=padre
    def tieneHijoIzquierdo(self):
        return self.__hijoIzquierdo
    def tieneHijoDerecho(self):
       return self.__hijoDerecho
    def esHijoIzquierdo(self):
        return self.__padre and self.__padre.hijoIzquierdo == self
    def esHijoDerecho(self):
        return self.__padre and self.__padre.hijoDerecho == self
    def esRaiz(self):
        return not self.__padre
    def esHoja(self):
        return not (self.__hijoDerecho or self.__hijoIzquierdo)
    def tieneAlgunHijo(self):
        return self.__hijoDerecho or self.__hijoIzquierdo
    def tieneAmbosHijos(self):
        return self.__hijoDerecho and self.__hijoIzquierdo
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.__clave=clave
        self.__cargaUtil=valor
        self.__hijoIzquierdo=hizq
        self.__hijoDerecho=hder
        if self.tieneHijoIzquierdo():
            self.__hijoIzquierdo=self
        if self.tieneHijoDerecho():
            self.__hijoIzquierdo = self