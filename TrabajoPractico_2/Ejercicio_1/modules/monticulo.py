
class monticulo:
    def __init__(self):
        self.__listaMonticulo = [0]
        self.__tamanoActual = 0
    @property
    def listaMonticulo(self):
        return self.__listaMonticulo
    @listaMonticulo.setter
    def listaMonticulo(self,listaMonticulo):
        self.__listaMonticulo=listaMonticulo
    @property
    def tamanoActual(self):
        return self.__tamanoActual
    @tamanoActual.setter
    def tamanoActual(self,tamanoActual):
        self.__tamanoActual=tamanoActual
        
    #Infiltra elementos hasta que se cumpla el criterio de orden del monticulo
    def infiltrarArriba(self, i):
        while i//2>0:
            if self.__listaMonticulo[i] < self.__listaMonticulo[i//2]:
                tmp = self.__listaMonticulo[i//2]
                self.__listaMonticulo[i//2] = self.__listaMonticulo[i]
                self.__listaMonticulo[i] = tmp
            i = i//2
    #Inserta los elementos al final, manteniendo la estructura. Utiliza el método infiltrarArriba para 
    #mantener el orden
    def insertar(self, valor):
        self.__listaMonticulo.append(valor)
        self.__tamanoActual+=1
        self.infiltrarArriba(self.tamanoActual)
    
    def __len__(self):
        return self.__tamanoActual
    
    def __iter__(self):
        for i in range(1, self.__tamanoActual + 1):
            yield self.__listaMonticulo[i]


    
    # #Indica cual es el hijo mínimo de determinado elemento
    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2 
            else:
                return i * 2 + 1
                




    def infiltrarAbajo (self,i):
        while (2*i) < self.__tamanoActual:
            hm=self.hijoMin(i)
            if self.__listaMonticulo[i].riesgo >= self.__listaMonticulo[hm].riesgo:
                tmp=self.__listaMonticulo[i]
                self.__listaMonticulo[i]= self.__listaMonticulo[hm]
                self.__listaMonticulo[hm] = tmp
            i=hm

    def eliminar (self):
        #Guarda el valor de la raíz
        pacienteAtendido = self.__listaMonticulo[1]
        #Ahora, la raíz es igual al último elemento
        self.__listaMonticulo[1] = self.__listaMonticulo[self.__tamanoActual]
        #Cambia el tamano del monticulo y elimina el último elemento (pasó a la raíz para conservar la estructura)
        self.__tamanoActual -=1
        self.__listaMonticulo.pop()
        #Usa el método infiltrar abajo para conservar el orden
        self.infiltrarAbajo(1)
        return pacienteAtendido



    
    def construirMonticulo(self,lista):
        i=len(lista)//2
        listaMonticulo= [0] + lista[:]
        self.tamanoActual=len(lista)
        while (i>0):
            self.infiltrarAbajo(i)
        i-=1
        
      