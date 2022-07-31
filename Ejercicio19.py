'''
Crear un programa en Python que tenga 3 o 4 funciones.
- Suma, 3 parámetros, devuelve la suma de los 3.
- Resta, 2 parámetros, devuelve la resta de los dos.
- Producto, 4 parámetros devuelve el producto de los 4.
- Imprimir, texto y valor, devuelve la impresión de los valores pasados. 
'''

num1 = 0
num2 = 0
num3 = 0
num4 = 0 


def suma(num1,num2,num3):
    var_suma = num1 + num2 +num3
    return var_suma


def resta(num1 , num2):
    var_resta = num1 - num2
    return var_resta

def producto(num1,num2,num3,num4):
    var_producto = num1*num2*num3*num4
    return var_producto          

print()
print("\t MENU:")
print("1- Sumar 3 parámetros")
print("2- Restar 2 parámetros.")
print("3- Multiplicar 4 parámetros.")
print()


opci = int(input("opción: "))
print()

if opci == 1:
    num1 = float(input("Ingresa el primer número: "))
    num2= float(input("Ingresa el segundo número: "))
    num3= float(input("Ingresa el tercer número: "))
    print()
    print(f"El total de la suma es: {suma(num1,num2,num3)}")

elif opci == 2:
     num1 = float(input("Ingresa el primer número: "))    
     num2 = float(input("Ingresa el sagundo número: ")) 
     print()
     print(f"El total de la resta es: {resta(num1,num2)}")

elif opci == 3:
    num1 = float(input("Ingresa el primer número: "))     
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    num4 = float(input("Ingresa el cuarto número: "))
    print()
    print(f"El resultado del producto es: {producto(num1,num2,num3,num4)}")

else:
    print("La opción tipeada es incorrecta.")    
print()

print("\t Gracias por usar este programa.")
print()