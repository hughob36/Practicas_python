print()

operación = (input("Introduzca la primera letra de la operacion que quiera realizar: ")).lower()

print()

num1 = float((input("Digite un número: ")))
num2 = float((input("Digite otro número: ")))

print()

if operación == "s": 
    ope = num1 + num2
    print("El valor de la suma es:", ope)
     
elif operación == "r":
     ope = num1 - num2
     print("El resultado de la resta es:", ope)

elif operación == "m":
     ope = num1 * num2
     print("El resultado de la multiplicación es:", ope)

elif operación == "d":
     ope = num1 / num2
     print("El resultado de la división es:", ope) 

else:
    print("La letra introducida no corresponde a ninguna operación matemática")        
    
    