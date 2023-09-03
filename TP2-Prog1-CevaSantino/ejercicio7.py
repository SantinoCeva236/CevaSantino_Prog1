def main():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        
        menor = min(numero1, numero2, numero3)
        
        print(f"El menor de los tres números es: {menor}")
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    main()
