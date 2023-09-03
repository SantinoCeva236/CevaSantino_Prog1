def main():
    try:
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))
        
        if numero1 <= 0 or numero2 <= 0:
            print("Error: Por favor ingrese números enteros positivos.")
        else:
            mayor = max(numero1, numero2)
            menor = min(numero1, numero2)
            
            if mayor % menor == 0:
                print(f"El mayor número ({mayor}) es múltiplo del menor número ({menor}).")
            else:
                print(f"El mayor número ({mayor}) no es múltiplo del menor número ({menor}).")
    except ValueError:
        print("Error: Por favor ingrese números enteros válidos.")

if __name__ == "__main__":
    main()