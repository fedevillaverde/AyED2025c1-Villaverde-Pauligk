# -*- coding: utf-8 -*-

from random import randint, choices
import datetime

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__segundoCriterio = datetime.datetime.now()
        
    @property
    def segundoCriterio(self):
       return self.__segundoCriterio
   
    

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    @property
    def riesgo(self):
        return self.__riesgo
    @riesgo.setter
    def riesgo(self,nuevote_riesgote):
        if type(self.__riesgo) != int:
            raise TypeError("el riesgo debe ser un numero entero entre 1 y 3")
        if nuevote_riesgote not in [1,2,3]:
            raise ValueError("el riesgo debe ser un valor entero entre 1 y 3")
        self.__riesgo=nuevote_riesgote
    
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    def __lt__(self,otro):
        if self.__riesgo < otro.riesgo:
            return True
        elif self.__riesgo == otro.riesgo:
            if self.__segundoCriterio < otro.segundoCriterio:
                return True
            else:
                return False
        else:
            return False
        
        
if __name__ == "__main__":
    paciente1=Paciente()
    paciente2=Paciente()
    if paciente1>paciente2:
        print(paciente1)
    print(paciente1,paciente2)
        
        