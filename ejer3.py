'''
Hacer un menu de opciones del 1 al 4 y la accion 
salir para salir del programa. Al introducir un numero 
del 1 al 4 , nos saldra la estacion del año que le 
pertenezca y al poner la opcion salir , salir del programa 
'''
while True:
    print("ESTACIONES DEL AÑO")
    print("------------------")
    print("- Ingrese del 1 hasta el cinco para saber las estaciones del año: ")
    print("- 5 para salir")
#Entrada
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("==========")
        print("  PRIMAVERA  ")
        print("==========")
    elif opcion == 2:   
        print("==========")
        print("  VERANO ")
        print("==========")
    elif opcion == 3:   
        print("==========")
        print(" OTOÑO  ")
        print("==========")
    elif opcion == 4:   
        print("==========")
        print("  INVIERNO  ")
        print("==========")
    elif opcion == 5:   
        print("==========")
        print("Cerrando sistema")
        print("==========")
        break
    else:   
        print("==========")
        print("Opción incorrecta")
        print("==========")            
