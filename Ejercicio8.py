# Hacer un programa que pida un caracter e indique si es una vocal o no.

print()

caracter = input("Indique un caracter: ").lower()

print()

while caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
      print(f"La letra:'{caracter}' es una vocal")
      print()
      caracter = input("Indique otro caracter: ").lower()

      print()
   
else:
    print("El caracter no es una vocal")

print()

print("Fin del programa.")

print()
      
   