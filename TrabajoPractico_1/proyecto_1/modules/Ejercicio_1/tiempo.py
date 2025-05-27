from random import randint
import time

#Ingresa el método a testear junto con una lista de los diferentes tamaños
def medir_tiempos(metodo_ord, tamanos):
    #En ésta lista se irán agregando los tiempos
    tiempos_ord_selecc = []

    for n in tamanos:
        # datos = []
        # for _ in range(n):
        #     datos.append(randint(1, 10000))
        #Crea listas con valores aleatorios con las cantidades solicitadas
        datos = [randint(1, 10000) for _ in range(n)]
        
        #mide el tiempo al inicio
        inicio = time.perf_counter()
        metodo_ord(datos)
        #mide el tiempo al final del ordenamiento
        fin = time.perf_counter()
        #se agrega a la lista la diferencia de los tiempos
        tiempos_ord_selecc.append(fin - inicio)
        
        print(f"Tiempo de ordenamiento por seleccion para n={n}: {fin - inicio:.6f} segundos")
    
    #devuelve la lista con los tiempos
    return tiempos_ord_selecc



if __name__ == '__main__':
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    medir_tiempos(      tamanos)
    