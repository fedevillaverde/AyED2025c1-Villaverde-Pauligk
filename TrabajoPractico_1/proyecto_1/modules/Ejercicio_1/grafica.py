from matplotlib import pyplot as plt
from random import randint
from tiempo import medir_tiempos
from Ordenamientos import ordenamientoburbuja, ordenamientoRapido_Nueva, radix_sort

def graficar_tiempos(lista_metodos_ord):
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)


    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()



metodos_de_ordenamiento = [ordenamientoburbuja, ordenamientoRapido_Nueva, radix_sort]
graficar_tiempos(metodos_de_ordenamiento)
