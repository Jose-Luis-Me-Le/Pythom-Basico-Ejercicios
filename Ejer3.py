"""
Dado el valor de un producto, ingresando el valor por el teclado,
hallar el IGV(18%) y el precio de venta

"""
#variables
vv = None
igv = None
pv = None

# Entrada
vv = float(input("Ingrese el valor de venta: "))

# Operaciones
igv = vv *0.18
pv = vv + igv


#Salida
print("El IGV es: ",igv)
print("El precio de venta es: ",pv)