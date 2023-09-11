while True:
    # Mostrar el menú de opciones
    print("Menú de opciones de la empresa de turismo:")
    print("1. Ver paquetes de viaje")
    print("2. Reservar un paquete de viaje")
    print("3. Consultar itinerario de viaje")
    print("4. Contactar al servicio al cliente")
    print("0. Salir del programa")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Por favor, ingrese el número de la opción que desea: ")

    if opcion == "1":
        print("Opción 1 seleccionada: Ver paquetes de viaje")
        # Aquí puedes agregar la lógica para mostrar los paquetes de viaje disponibles.
    elif opcion == "2":
        print("Opción 2 seleccionada: Reservar un paquete de viaje")
        # Aquí puedes agregar la lógica para permitir al usuario reservar un paquete de viaje.
    elif opcion == "3":
        print("Opción 3 seleccionada: Consultar itinerario de viaje")
        # Aquí puedes agregar la lógica para consultar el itinerario de un viaje.
    elif opcion == "4":
        print("Opción 4 seleccionada: Contactar al servicio al cliente")
        # Aquí puedes agregar la lógica para permitir al usuario contactar al servicio al cliente.
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido de opción.")
