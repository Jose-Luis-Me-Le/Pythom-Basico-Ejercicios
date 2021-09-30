"""
Ingresando dos numeros enteros por pantalla 
hayar el cociente y el residuo

"""
# variables
n1 = None
n2 = None
c = None
r = None

#Entrada
print("Ingrese numeros enteros")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

# Operaciones
c = n1 / n2
r = n1 % n2

#Salida
print("El cociente es: ",c)
print("El resto es: ", r)