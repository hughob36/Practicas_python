'''
Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par
o si ambos lo son.

'''

print()

a = int((input("Escribe un número: ")))
b = int((input("Escribe otro número: ")))

print()
 
if a % 2 == 0 and b % 2 == 0 :
    print(f"Ambos números: {a} y {b} son pares.") 

elif a % 2 == 0:
     print(f"El número {a} es par.")

elif b % 2 == 0:
     print(f"El número {b} es par.")  

else:
    print("Ambos números NO son pares.")       
