'''
Ordenamiento burbuja. Ordenar la lista de menor a mayor. 

'''

lista = [45,16,185,489,19,356,97,14]
nro = 0

while nro < len(lista)-1: 
    for i in range(0 , len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista [i+1] = lista[i+1], lista[i]
    nro +=1

print(lista)             

        