def main():
    try:
        a = float(input("Ingrese el valor de 'a': "))
        b = float(input("Ingrese el valor de 'b': "))
        
        print("Operaciones disponibles:")
        print("1. Sumar (a + b)")
        print("2. Multiplicar (a * b)")
        print("3. Restar (a - b)")
        print("4. Dividir (a / b)")
        
        operacion = int(input("Seleccione una operación (1/2/3/4): "))
        
        if operacion == 1:
            resultado = a + b
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == 2:
            resultado = a * b
            print(f"El resultado de la multiplicación es: {resultado}")
        elif operacion == 3:
            resultado = a - b
            print(f"El resultado de la resta es: {resultado}")
        elif operacion == 4:
            if b != 0:
                resultado = a / b
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No es posible dividir entre 0.")
        else:
            print("Opción inválida. Por favor, seleccione una operación válida (1/2/3/4).")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
