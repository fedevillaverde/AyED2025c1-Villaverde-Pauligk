from modules.paciente import paciente as pac
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
        
    #infiltra elementos hasta que se cumpla el criterio del monticulo
    def infiltrarArriba(self, i):
        while i//2>0:
            if self.__listaMonticulo[i].riesgo > self.__listaMonticulo[i//2].riesgo:
                tmp = self.__listaMonticulo[i//2]
                self.__listaMonticulo[i//2] = self.__listaMonticulo[i]
                self.__listaMonticulo[i] = tmp
            i = i//2
    def insertar(self, valor):
        self.__listaMonticulo.append(pac.valor)
        self.__tamanoActual+=1
        self.infiltrarArriba(self.tamanoActual)
    def hijoMin (self,i):
        if i*2 +1 > self.__tamanoActual:
            return i*2
        else:
            if self.__listaMonticulo[i*2].riesgo < self.__listaMonticulo[i*2+1].riesgo:
                return i*2
            else:
                if self.__listaMonticulo[i*2].horaLlegada > self.__listaMonticulo[i*2+1].horaLLegada:
                    return i*2+1
                else:
                    return i*2
    def infiltrarAbajo (self,i):
        while (2*i) < self.__tamanoActual:
            hm=self.hijoMin(i)
            if self.__listaMonticulo[i].riesgo >= self.__listaMonticulo[hm].riesgo:
                tmp=self.__listaMonticulo[i]
                self.__listaMonticulo[i]= self.__listaMonticulo[hm]
                self.__listaMonticulo[hm] = tmp
        i=hm
            
    
      