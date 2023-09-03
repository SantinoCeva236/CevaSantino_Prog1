def main():
    try:
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        nota4 = float(input("Ingrese la cuarta nota: "))
        
        promedio = (nota1 + nota2 + nota3 + nota4) / 4
        
        if promedio >= 6:
            print(f"El alumno ha aprobado el curso con un promedio de {promedio:.2f}.")
        else:
            print(f"El alumno ha reprobado el curso con un promedio de {promedio:.2f}.")
    except ValueError:
        print("Error: Por favor ingrese notas válidas.")

if __name__ == "__main__":
    main()
