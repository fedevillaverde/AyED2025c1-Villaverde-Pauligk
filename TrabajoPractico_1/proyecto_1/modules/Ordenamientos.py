import random as r

#Defino una función que crea una lista con la cantidad de elementos dada
def randint_list(cantidad, menor, mayor):
    listarda =[]
    for i in range(cantidad):
        valor= r.randint(menor,mayor)
        listarda.append(valor)
    return listarda

# 1_ ordenamiento por burbuja
def ordenamientoburbuja(lista):
    #Realiza tantas pasadas como pares de items tenga la lista
    for num_lista in range(len(lista)-1,0,-1):

        #En cada pasada, realiza una iteración menos, ya que deja los valores más grandes al final
        for i in range(num_lista):
            #compara los items adyacentes y los ordena, desplazando al más grande al final de la lista
            if lista[i] > lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
    return lista

    
# 2_ ordenamiento rápido
#Devuelve una lista ordenada usando "ordenamientoRapido()"
def ordenamientoRapido_Nueva(lista):
    n_lista = lista.copy()
    ordenamientoRapido(n_lista)
    return n_lista
#Ordena una lista
def ordenamientoRapido(lista):
   ordenamientoRapidoAuxiliar(lista,0,len(lista)-1)

def ordenamientoRapidoAuxiliar(lista,primero,ultimo):
   #Utilizamos ésta función auxiliar para acercarnos al caso base
   if primero<ultimo:

       pivote = particion(lista,primero,ultimo)
       #Una vez conocido el pivote, volvemos a llamar a la función recursiva  para que ordene la lista a la derecha
        # y a la izquierda de éste

       ordenamientoRapidoAuxiliar(lista,primero,pivote-1)
       ordenamientoRapidoAuxiliar(lista,pivote+1,ultimo)

def particion (lista, primero, ultimo):

    marc_I = primero +1
    marc_D = ultimo
    
    ValorPivote = lista[primero]

    stop = False
    
    while not stop:
        #Mueve el marcador de la izquierda hasta encontrar a uno que sea mayor al pivote
        while marc_I <= marc_D and lista[marc_I]<=ValorPivote:
            marc_I +=1
        #Mueve el marcador de la derecha hasta encontrar a uno que sea menor al pivote
        while marc_D >= marc_I and lista[marc_D] >= ValorPivote:
            marc_D -=1
        if marc_D<marc_I:
            stop =True
        else:
            temp = lista[marc_I]
            lista[marc_I]=lista[marc_D]
            lista[marc_D] = temp
    #cambia la ubicación del pivote
    lista[primero] = lista[marc_D]
    lista[marc_D]  = ValorPivote

    return marc_D


# 3_ Ordenamiento por residuos
def counting_sort(lista, lugar):
    
    contador = [0] * 10

    # Contar cuántas veces aparece cada dígito en el lugar actual (unidades, decenas, etc)
    for numero in lista:
        digito = (numero // lugar) % 10
        contador[digito] += 1

    # Convertir el conteo en posiciones acumuladas
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    salida = [0] * len(lista)

    # Colocar los números en su posición ordenada (de derecha a izquierda)
    i = len(lista) - 1
    while i >= 0:
        digito = (lista[i] // lugar) % 10
        posicion = contador[digito] - 1
        salida[posicion] = lista[i]
        contador[digito] -= 1
        i -= 1

    # Copiar la salida en la lista original
    for i in range(len(lista)):
        lista[i] = salida[i]

def radix_sort(lista):
    # Encontrar el número más grande (para saber cuántos dígitos tiene)
    maximo = max(lista)

    # Empezar en las unidades (1, 10, 100, ...)
    lugar = 1
    while maximo // lugar > 0:
        counting_sort(lista, lugar)
        lugar *= 10
    
    return lista



#Para probar si los algoritmos funcionan, creo una lista con las características solicitadas
listita= randint_list(500, 10000, 999999)
#tomo de referencia una lista ordenada con el método sorted
lista_ordenada = sorted(listita)
metodo1 = ordenamientoburbuja(listita)
metodo2 = ordenamientoRapido_Nueva(listita)
metodo3 = radix_sort(listita)
if metodo1 == lista_ordenada:
    print("el ordenamiento de burbuja funciona")
else:
    print("el ordenamiento de burbuja no funciona")
if metodo2 == lista_ordenada:
    print("el ordenamiento rapido funciona")
else:
    print("el ordenamiento rapido no funciona")
if metodo3 == lista_ordenada:
    print("el ordenamiento por residuos funciona")
else:
    print("el ordenamiento por residuos no funciona")





                