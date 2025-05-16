class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.__clave = clave
        self.__cargaUtil=valor
        self.__hijoIzquierdo=izquierdo
        self.__hijoDerecho=derecho
        self.__padre=padre
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
    @hijoIzquierdo.setter
    def hijoIzquierdo(self,hijoIzquierdo):
        self.__hijoIzquierdo=hijoIzquierdo
    @hijoDerecho.setter
    def hijoDerecho(self,hijoDerecho):
        self.__hijoDerecho=hijoDerecho
    @padre.setter
    def padre(self,padre):
        self.__padre=padre
    