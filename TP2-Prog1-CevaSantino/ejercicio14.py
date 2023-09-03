def main():
    try:
        coeficiente_a = float(input("Ingrese el coeficiente 'a' de la ecuación: "))
        coeficiente_b = float(input("Ingrese el coeficiente 'b' de la ecuación: "))
        
        if coeficiente_a == 0:
            if coeficiente_b == 0:
                print("La ecuación tiene infinitas soluciones.")
            else:
                print("La ecuación no tiene solución.")
        else:
            solucion = -coeficiente_b / coeficiente_a
            print(f"La solución de la ecuación es x = {solucion:.2f}")
    except ValueError:
        print("Error: Por favor ingrese coeficientes válidos.")

if __name__ == "__main__":
    main()
