from random import randint
import time
from lista_doble_enlazada import ListaDobleEnlazada
from matplotlib import pyplot as plt
# A partir de la función provista por la catedra para graficar los algoritmos de ordenamiento.
# Graficamos el tiempo que tardaban los métodos invertir, copiar y len en función del tamaño de la lista

# definimos tamaños de lista para aplicar a todos y luego compararlos
sizes = [1, 10, 100, 200, 500, 700, 1000]

#Creamos la función que mide el tiempo que tarda cada método para cada tamaño de lista
#y devuelve una lista con éstos intervalos de tiempo
def tiempos_copiar (tamanos):
    tiempos = []

    for i in tamanos:
        lista = ListaDobleEnlazada()
        # for n in range(i):
        #     lista.agregar_al_final(randint(0,100))
        n = 0
        while n < i :
            lista.agregar_al_final(randint(0,100))
            n+=1

       

        inicio = time.perf_counter()
        lista.copiar()
        
        fin = time.perf_counter()
        
        
        tiempos.append(fin - inicio)
    return tiempos

def tiempos_invertir (tamanos):
    tiempos = []

    for i in tamanos:
        lista = ListaDobleEnlazada()

        n = 0
        while n < i :
            lista.agregar_al_final(randint(0,100))
            n+=1

        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        
       
        tiempos.append(fin - inicio)

    return tiempos

def tiempos_len (tamanos):
    tiempos = []

    for i in tamanos:
        lista = ListaDobleEnlazada()
    
        n = 0
        while n < i :
            lista.agregar_al_final(randint(0,100))
            n+=1

        inicio = time.perf_counter()
        len(lista)
        fin = time.perf_counter()
        
       
        tiempos.append(fin - inicio)
    return tiempos


def graficar(tiempos_metodos):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    
    plt.figure(figsize=(10, 6))
    for (nombre, metodo )in tiempos_metodos.items():
        print(f"Graficando método: {nombre}")
        plt.plot(tamanos, metodo, marker='o', label=nombre)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos ')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

#definimos listas con los tiempos de cada método, aplicando las funciones desarrolladas anteriormente
copiar = tiempos_copiar(sizes)
invertir= tiempos_invertir(sizes)
len = tiempos_len(sizes)

#Finalmente, graficamos todo para poder comparar
tiempitos = {"copiar":  copiar, "invertir":invertir, "len":len}
print(type(tiempitos))
graficar(tiempitos)




