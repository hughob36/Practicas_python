'''
Ejercicio número 1.
Ecuación matemática, el programa pide 3 valores a, b y c y resuelve la operación. Imprime el valor 
de la ecuación.

'''
print()

a = float ( input ( "Ingrese el valor para a->  "))
b = float ( input ( "Ingrese el valor para b->  "))
c = float ( input ( "Ingrese el valor para c->  ")) 

Operación_mat = (a ** 3 * (b **2 - 2 * a * c))/(2 * b)

print()

print ( f" El resultado de la ecuación es:  {Operación_mat}")

print()

print("Fin del programa.")

print()