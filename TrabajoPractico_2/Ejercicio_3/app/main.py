from modules.grafo import Grafo
from modules.prim import prim
#En el siguiente código, utilizamos el TAD "Grafo" implementado anteriormente para resolver la problemática planteada

grafo_aldeas = Grafo()
rutita = r''

with open (rutita, 'r') as aldeitas:
    for renglon in aldeitas:
        aldeita = renglon.split(',')
        aldea1= aldeita[0].strip()
        aldea2= aldeita[1].strip()
        aldea3=int(aldeita[2].strip())
        
        
        if len(aldeita) == 3:
            grafo_aldeas.agregarArista(aldea1, aldea2, aldea3)
          
#Aplicamos el método prim para buscar la forma más eficiente de enviar una noticia a todas las aldeas

prim(grafo_aldeas, grafo_aldeas["Peligros"])




#Para ordenar alfabéticamente las aldeas, usamos el método "sorted()"
lista_aldeas = grafo_aldeas.obtenerVertices()
lista_aldeas_ordenadas = sorted(lista_aldeas)
#Luego,nos interesa saber, para cada aldea, de quién recibe la noticia y a quién se la envía
#Como aplicamos el método prim, ésta información se encuentra en la instancia "predecesor" de cada vertice
#De este modo, mostramos las aldeas en orden alfabético y su respectivo predecesor:

for v in lista_aldeas_ordenadas:
    vertice_aldea = grafo_aldeas[v]
    if vertice_aldea.id == "Peligros":
        print(f"Aldea: {vertice_aldea.id}, Predecesor:-----, Siguientes: {vertice_aldea.siguiente}")
    else:
        print(f"Aldea: {vertice_aldea.id}, Predecesor:{vertice_aldea.predecesor.id}, Siguientes: {vertice_aldea.siguiente}")

#Finalmente, queremos conocer la distancia total o el coste total de recorrer todas las aldeas.
#Entonces realizamos la suma de todas las distancias
sumatoria = 0
for v in grafo_aldeas.obtenerVertices():
    vertice_aldea = grafo_aldeas[v]
    sumatoria = sumatoria + grafo_aldeas[v].distancia

print(f"La distancia total que recorren las palomas, sumando todos los recorridos de una aldea a otra es de {sumatoria} leguas")
