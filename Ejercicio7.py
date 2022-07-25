# Hacer un programa que pida 3 números y determine cuál es el mayor.

print()

num1 = float((input("Ingrese un número: ")))
num2 = float((input("Ingrese un segundo número: ")))
num3 = float((input("Ingrese un tercer número: ")))

print()

if num1 >= num2 and num1 >= num3:
    print("El número mayor es: ", num1)

elif num1 <= num2 and num2 >= num3:
     print(f"El número mayor es: {num2}")   

elif num1 <= num3 and num2 <= num3:
     print(f"El número mayor es: {num3}")    

print()

print("Fin del programa.")      