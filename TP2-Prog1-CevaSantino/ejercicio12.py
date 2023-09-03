def main():
    try:
        anio_actual = int(input("Ingrese el año actual: "))
        anio_objetivo = int(input("Ingrese un año cualquiera: "))
        
        if anio_actual > anio_objetivo:
            diferencia = anio_actual - anio_objetivo
            print(f"Han pasado {diferencia} años desde el año {anio_objetivo}.")
        elif anio_actual < anio_objetivo:
            diferencia = anio_objetivo - anio_actual
            print(f"Faltan {diferencia} años para llegar al año {anio_objetivo}.")
        else:
            print("Los años son iguales.")
    except ValueError:
        print("Error: Por favor ingrese años válidos.")

if __name__ == "__main__":
    main()
