def main():
    try:
        edad_computadora = int(input("Ingrese el número de años que tiene su computadora: "))
        
        if edad_computadora <= 2:
            print("La computadora es nueva.")
        else:
            print("La computadora es vieja.")
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()