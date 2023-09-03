def main():
    try:
        horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
        salario_por_hora = float(input("Ingrese el salario por hora: "))
        
        jornada_minima = 48
        horas_extras = max(0, horas_trabajadas - jornada_minima)
        salario_total = (horas_trabajadas * salario_por_hora) + (horas_extras * salario_por_hora * 1.10)
        
        if horas_extras > 0:
            print(f"Usted trabajó {horas_extras:.2f} horas extras.")
        
        print(f"Su salario total es: ${salario_total:.2f}")
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
