def main():
    print("Bienvenido a la pizzería Bella Napoli!")
    eleccion = input("¿Desea una pizza vegetariana o no vegetariana? (V/N): ").upper()
    
    if eleccion == "V":
        ingredientes_disponibles = ["Pimiento", "Tofu"]
        tipo_pizza = "vegetariana"
    elif eleccion == "N":
        ingredientes_disponibles = ["Peperoni", "Jamón", "Salmón"]
        tipo_pizza = "no vegetariana"
    else:
        print("Opción inválida. Por favor, seleccione V para vegetariana o N para no vegetariana.")
        return
    
    print("\nIngredientes disponibles:")
    for index, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{index}. {ingrediente}")
    
    try:
        eleccion_ingrediente = int(input("\nSeleccione un ingrediente adicional (número): "))
        
        if eleccion_ingrediente >= 1 and eleccion_ingrediente <= len(ingredientes_disponibles):
            ingrediente_elegido = ingredientes_disponibles[eleccion_ingrediente - 1]
            print("\n¡Excelente elección!")
            print(f"Su pizza {tipo_pizza} lleva los siguientes ingredientes: Mozzarella, Tomate, {ingrediente_elegido}")
        else:
            print("Opción inválida. Por favor, seleccione un número válido.")
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()