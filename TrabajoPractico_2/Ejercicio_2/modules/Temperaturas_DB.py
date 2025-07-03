from modules.ArbolAVL import ArbolAVL
from datetime import datetime

class Temperaturas:
    def __init__(self):
        self._arbol = ArbolAVL()
    
    #convierte las fechas ingresadas en tipo de dato str a objeto datetime (para poder compararlas entre sí)
    def fecha_dato (self, fechita_str):
        # Convertir a objeto datetime
        fechita_obj = datetime.strptime(fechita_str, "%d/%m/%Y")

       
        return fechita_obj

    def guardar_temperatura(self, temperatura, fecha):
        nfechita = self.fecha_dato(fecha)
        self._arbol.agregar(nfechita, temperatura)
    def devolver_temperatura(self, fecha):
        nfechita = self.fecha_dato(fecha)
        muestra = self._arbol.buscar(nfechita)
        return muestra.cargaUtil
    def max_temp_rango(self, fecha1, fecha2):
        nfechita1 = self.fecha_dato(fecha1)
        nfechita2 = self.fecha_dato(fecha2)

        tmax =self._arbol.buscar_max(nfechita1, nfechita2)
        return tmax
    def min_temp_rango(self, fecha1, fecha2):
        nfechita1 = self.fecha_dato(fecha1)
        nfechita2 = self.fecha_dato(fecha2)

        tmin =self._arbol.buscar_min(nfechita1, nfechita2)
        return tmin
    def temp_extremos_rango(self, fecha1, fecha2):
        nfechita1 = self.fecha_dato(fecha1)
        nfechita2 = self.fecha_dato(fecha2)

        tmax =self._arbol.buscar_max(nfechita1, nfechita2)
        tmin =self._arbol.buscar_min(nfechita1, nfechita2)

        return (tmin, tmax)
    def borrar_temperatura(self, fecha):
        nfechita = self.fecha_dato(fecha)
        self._arbol.eliminar( nfechita)

    def devolver_temperaturas(self, fecha1, fecha2):    
        nfechita1 = self.fecha_dato(fecha1)
        nfechita2 = self.fecha_dato(fecha2)

        noditos = self._arbol.buscar_rango(nfechita1, nfechita2)

        
        return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.cargaUtil} ºC" for nodo in noditos]

    def cantidad_muestras(self):
        cant = self._arbol.devolver_tamano()
        return cant
    
    from datetime import datetime




    