lista = []
cantidad = 5
i = 1

print()

while cantidad > 0:
      numero = int(input("Ingresar #"+ str(i) +" : "))
      i += 1
      lista. append (numero)
      cantidad -= 1 

print()

print("\t MENU:")
print("1- Sumar números de la lista.")
print("2- Sacar promedio de los números de la lista.")
print("3- Número maximo de la lista.")
print("4- Menor número de la lista.")

print()

opcion = int(input("Ingrese la opcion de menu que desea realizar con la lista: ")) 

print()

if opcion == 1:
    suma = lista [0] + lista [1] + lista [2] + lista [3] + lista [4]
    print (f"La suma de los números de la lista es: {suma}")

elif opcion == 2:
     promedio = (lista [0] + lista [1] + lista [2] + lista [3] + lista [4]) / 5
     print(f"El promedio de los números de la lista es: {promedio}")

elif opcion == 3:
     maximo = max(lista)
     print(f"El número maximo de la lista es: {maximo} ")

elif opcion == 4:
     minimo = min(lista)
     print(f"El número minimo de la lista es: {minimo}")

else:
     print("La opcion elegida no corresponde a ninguna del menu.")

print()
