"""
Dado dos numeros, hayar la suma ,resta, multiplicacion y division
Para hacer este ejercicio es necesario ingresar dos numeros
por teclado y despues hayar las operaciones

"""
#variables
n1 = None
n2 = None
suma = None
resta = None
multli = None
divi = None

#Entrada de dos numeros
n1 = float(input("Ingrese el numero 1: "))
n2 = float(input("Ingrese el numero 2: "))

# Operaciones
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

# Salida
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicacion es: ",multi)
print("La division es: ",divi)