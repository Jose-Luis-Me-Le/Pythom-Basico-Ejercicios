"""
Hallar la potenciade a^n con numeros positivos
Hay que ingresar unos numeros por teclado y en
tonces resolver

"""
#variables
a = None
n = None
p = None

# Entrada
print("Hallar A elevado a N")
a = int(input("Ingrese el numero a Elevar(A): "))
n = int(input("Ingrese la potencia(N): "))

# Operaciones
p = a ** n


#Salida en pantalla
print("El total de la potenciacion de nuestro numero es: ",p)