"""
Dados dos numeros diferentes , devolver el mayor.Se requiere
introducir pot teclado dos numeros y el sistema hace la operacion
"""
#variables
n1 = None
n2 = None
n_mayor = None

#Entrada
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

#Procesamiento3

if n1 > n2:
   n_mayor = n1
   print("El numero mayor es: ", n_mayor)
elif n2 > n1:
    n_mayor = n2
    print("El numero mayor es: ", n_mayor) 
    #Salida
   #  print("El numero mayor es: ", n_mayor)
