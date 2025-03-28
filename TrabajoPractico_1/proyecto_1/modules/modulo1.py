def ordenamientoburbuja(lista):
    for num_lista in range(len(lista)-1,0,-1):
        for i in range(num_lista):
            if lista[i] > lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
    return lista
listita=[3,5,8,4,18,9,13,1,56,97,77,68,21,11]
una_lista=ordenamientoburbuja(listita)
print(una_lista)
                