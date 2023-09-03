def main():
    try:
        cantidad_lapices = int(input("Ingrese la cantidad de lápices: "))
        
        costo_por_lapiz = 60
        costo_total = cantidad_lapices * costo_por_lapiz
        
        if cantidad_lapices >= 1000:
            descuento = costo_total * 0.07
            costo_total -= descuento
            print(f"Se aplicó un descuento del 7%: ${descuento:.2f}")
        
        print(f"El costo total es: ${costo_total:.2f}")
    except ValueError:
        print("Error: Por favor ingrese una cantidad válida.")

if __name__ == "__main__":
    main()
