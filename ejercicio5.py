'''
Una tineda ofrece un descuento del 15% sobre el total de la compra y un cliente desea 
saber cuánto deberá pagar finalmente por su compra.

'''

print()

CompraTotal = float((input("El total de la compra es: ")))

print()

Total_del_descuento = CompraTotal * 0.15 
Total_final_pagar = CompraTotal - Total_del_descuento

print()

print(f"Debe pagar un total de {Total_final_pagar:.2f}")

print()

print("Gracias por su compra")

print()