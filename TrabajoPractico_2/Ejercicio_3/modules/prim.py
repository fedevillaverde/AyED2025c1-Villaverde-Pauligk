from modules.ColaPrioridad import monticulo
from modules.grafo import Grafo
from modules.vertice import Vertice
import sys
def prim (Grafito:Grafo, inicio):
    cp = monticulo()
    for v in Grafito:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in Grafito])
    while not cp.estaVacia():
        verticeActual = cp.eliminar()[1]
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                cp.decrementarClave(verticeSiguiente, nuevoCosto)
    