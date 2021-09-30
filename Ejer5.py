
"""
Hallar la raiz cuadrada de un numero entero
r = a ^(1/n)
Introduciendo los valores por teclado

"""

#variables
a = None
n = None
r = None

# Entrada
a = int(input("Introduzca el numero que hay que sacar la raiz: "))
n = int(input("Intruzca la raiz que queremos sacar: "))

# Operaciones
r = a ** (1/n)

#Salida
print("La raiz es: ",r)