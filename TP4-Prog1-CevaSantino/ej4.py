def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4 y no divisible por 100, a menos que sea divisible por 400.
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def main():
    try:
        año_inicio = int(input("Ingrese el año de inicio: "))
        año_fin = int(input("Ingrese el año de fin: "))

        print("Años bisiestos y múltiplos de 10 en el rango:")
        for year in range(año_inicio, año_fin + 1):
            if es_bisiesto(year) and year % 10 == 0:
                print(year)
    except ValueError:
        print("Ingrese años válidos (números enteros).")

if __name__ == "__main__":
    main()
