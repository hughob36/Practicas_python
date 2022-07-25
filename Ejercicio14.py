
lista = []
bucle = True

print()

num = int(input("Ingresa la cantidad de números de la lista: "))

print()

for i in range(num):
    poste = int(input(" Ingresa los números: "))
    lista.append(poste)

print()

while bucle:
      bucle = False
      for i in range(len(lista)-1):
          if lista[i] > lista [i+1]:
             bucle = True
             lista [i], lista [i+1] = lista[i+1], lista[i]

print()

print("\n Lista organizada.")
print()
print(lista)
print()





