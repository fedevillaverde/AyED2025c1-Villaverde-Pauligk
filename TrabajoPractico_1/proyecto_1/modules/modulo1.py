import random as r

def randint_list(cantidad):
    listarda =[]
    for i in range(cantidad):
        valor= r.randint(0,10000000)
        listarda.append(valor)
    return listarda

def ordenamientoburbuja(lista):
    #Realiza tantas pasadas como pares de items tenga la lista
    for num_lista in range(len(lista)-1,0,-1):

        #En cada pasada, realiza una iteración menos, ya que deja los valores más grandes al final
        for i in range(num_lista):
            if lista[i] > lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp

    return lista

listita= randint_list(500)
una_lista=ordenamientoburbuja(listita)
print(una_lista)
                