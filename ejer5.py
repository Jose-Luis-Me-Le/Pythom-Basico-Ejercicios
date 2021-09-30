while True:
    print("INGRESO AL CINE ")
    print("================")
    print("1 - Terror")
    print("2 - Accion")
    print("3 - Aventuras")
    print("4 - Salir")

    opcion = int(input("Ingrese una opcion:"))

    if opcion == 1:
        edad = int(input("Ingrese su edad"))

        if edad >= 18 and edad <= 55:
            print("==============")
            print("Puede ingresar")
            print("==============")
        else:
            print("=================")
            print("No puede ingresar")
            print("=================")

    elif opcion == 2:
        edad = int(input("Ingrese su edad:"))

        if edad >= 10:
            print("==============")
            print("Puede ingresar")
            print("==============")
        else:
            print("=================")
            print("No puede ingresar")
            print("=================")
    elif opcion == 3:
        edad = int(input("Ingrese la edad:"))

        if edad >= 4:
            print("==============")
            print("Puede ingresar")
            print("==============")
        else:
            print("=================")
            print("No puede ingresar")
            print("=================")
    elif opcion == 4:
        print("================")
        print("Cerrando sistema")
        print("================")
        break
    else:
        print("=================")
        print("Opcion incorrecta")
        print("=================")    


