from modules.ColaPrioridad import monticulo
from modules.grafo import Grafo
from modules.vertice import Vertice
import sys
#A continuación se desarrolla el método prim

def prim (Grafito:Grafo, inicio):
    #Crea una cola de prioridad
    cp = monticulo()
    #Para vector del grafo, se le asigna una distancia infinita y un predecesor None
    for v in Grafito:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    #El vector del inicio tiene uuna distancia 0 
    inicio.asignarDistancia(0)
    #Se construye un montículo con tuplas (distancia al vertice, vertice)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in Grafito])

    #Mientras la cola de prioridad no esté vacía (tenga elementos para explorar)
    while not cp.estaVacia():
        
        verticeActual = cp.eliminar()[1]
        #Para cada vértice vecino a VA
        for verticeSiguiente in verticeActual.obtenerConexiones():
            #se calcula el nuevo costo
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)

            #Si VN no fue explorado y la ponderación entre VA y VN es menor a la distancia de VN
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                verticeActual.asignarSiguiente(verticeSiguiente.id)
                #Actualiza el valor de la clave del vertice en el montículo y actualiza el orden de éste
                cp.decrementarClave(verticeSiguiente, nuevoCosto)
    