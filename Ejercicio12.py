'''
Se ingresan las medidas de frente y fondo de un terreno.
Determinar si es cuadrado o rectangular y calcular su superficie.

'''

print()

num1 = float(input("Ingrese la medida del frentre del terreno: "))

num2 = float(input("Ingrese la medida del fondo del terreno: "))

print()

if num1 == num2:
    print("El terreno es un cuadrado.")

elif num1 != num2:
     print("El terreno es un rectangulo.")

print() 

area = num1 * num2

print(f"La superficie del terreno es {area} metros cuadrados.")

print()