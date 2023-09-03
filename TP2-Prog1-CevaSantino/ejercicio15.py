import math

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

def main():
    opcion = input("¿Desea calcular el área de un triángulo (T) o un círculo (C)? ").upper()
    
    if opcion == "T":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    elif opcion == "C":
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    else:
        print("Opción inválida. Por favor, seleccione T para triángulo o C para círculo.")

if __name__ == "__main__":
    main()
