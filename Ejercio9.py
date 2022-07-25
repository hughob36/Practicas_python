'''
Hacer un programa que simule un cajero automático con un saldo de $1000 
y tendrá el siguiente menú de opciones :
1- Ingresar dinero en la cuenta.
2- Retirar dinero de la cuenta.
3- Mostrar dinero disponible.
4- Salir.

'''
print()

saldo = 1000
total = saldo
print()

print("\tMENU:")
print("1- Ingresar dinero.")
print("2-Retirar dinero de la cuenta.")
print("3- Mostrar dinero de la cuenta.")
print("4- Salir")

print()

opciones = int((input("Digite el número de la operación que desea realizar ->" )))

print()

if opciones == 1:
    nuevomonto = float(input(("Ingrese el monton: ")))
    if nuevomonto >= 0:
        total = saldo + nuevomonto
        print(f"Su saldo es: {total}")
    else:
         print("debe ingresar un valor positivo.")

if opciones == 2:    
    nuevomonto = float(input("Ingrese cuanto quiera retirar: "))
    if nuevomonto <= saldo:
        total = saldo - nuevomonto
        print(f"Su saldo es: {total}")
    else:
        print("El monto que quiere retirar supera su saldo.")

if opciones == 3:
    print(f"Su saldo es: {saldo}")

if opciones == 4:
    print("Gracias por usar este programa.")

elif  opciones <= 0 or opciones >= 5:
     print("La opcion tipeada no corresponde a ninguna de la barra del menu")

print()                    
    
    

