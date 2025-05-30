from modules.grafo import Grafo
from modules.prim import prim
grafo_aldeas = Grafo()
rutita = r'C:\Users\alumno\Documents\Pauligk\AyED2025c1-Villaverde-Pauligk\TrabajoPractico_2\aldeas.txt'
with open (rutita, 'r') as aldeitas:
    for renglon in aldeitas:
        aldeita = renglon.split(',')
        aldea1= aldeita[0].strip()
        aldea2= aldeita[1].strip()
        aldea3=int(aldeita[2].strip())
        print('aldeita:',aldeita)
        
        if len(aldeita) == 3:
            grafo_aldeas.agregarArista(aldea1, aldea2, aldea3)
          
prim(grafo_aldeas, grafo_aldeas.obtenerVertice('Peligros'))
for v in grafo_aldeas:
    print(v)