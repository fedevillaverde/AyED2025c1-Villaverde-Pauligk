class Nodo:
    def __init__(self, dato_inicial):
        self.__dato=dato_inicial
        self.__siguiente=None
        self.__anterior=None
    @property
    def dato(self):
        return self.__dato
    @dato.setter
    def dato(self, nuevo_dato):
        self.__dato = nuevo_dato
        
    @property
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self, n_siguiente):
        self.__siguiente=n_siguiente
        
    @property
    def anterior(self):
        return self.__anterior
    @anterior.setter
    def anterior(self, n_anterior):
        self.__anterior=n_anterior
    

        
        