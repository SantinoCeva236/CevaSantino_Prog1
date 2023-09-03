def main():
    try:
        nombre1 = input("Ingrese el primer nombre: ")
        nombre2 = input("Ingrese el segundo nombre: ")
        
        if nombre1 and nombre2:  # Verificar que ambos nombres no estén vacíos
            if nombre1[0].lower() == nombre2[0].lower():
                print("Coincidencia: Ambos nombres comienzan con la misma letra.")
            else:
                print("No hay coincidencia: Los nombres no comienzan con la misma letra.")
        else:
            print("Error: Por favor ingrese ambos nombres.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
