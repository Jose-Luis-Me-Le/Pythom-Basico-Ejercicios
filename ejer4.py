'''
Dado el numero ingresado  que sea entero
obtener una tabla de multiplicacion
Se requiere que tenga un menu para sacar 
la multiplicacion o salir del programa 
despues imprimira la tabla
'''
while True:
    print("REALIZAR UNA TABLA DE MULTIPLICAR")
    print("1 - Imprimir la tabla de multiplicar")
    print("2 - Salir") 

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        n = int(input("Ingrese el numero para la tabla: "))
        c = 0
        while c <= 10:
           r = n * c
           print("|", n, "x", c, "=", r, "|")
           c += 1
    elif opcion == 2:
        print("==================")
        print(" Cerrando sistema" )
        print("==================")
        break
    else:
        print("==================")
        print(" OpciÓn incorrecta")
        print("==================")

