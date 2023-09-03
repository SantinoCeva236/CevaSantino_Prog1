def main():
    try:
        edad = int(input("Ingrese su edad: "))
        
        if edad < 4:
            precio = 0
        elif edad >= 4 and edad <= 18:
            precio = 500
        else:
            precio = 1000
        
        print(f"El precio de la entrada es: ${precio}")
    except ValueError:
        print("Error: Por favor ingrese una edad válida.")

if __name__ == "__main__":
    main()
