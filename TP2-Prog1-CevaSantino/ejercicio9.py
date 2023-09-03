def main():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M/F): ").upper()

    if (sexo == "F" and nombre.lower() < 'm') or (sexo == "M" and nombre.lower() > 'n'):
        grupo = "A"
    else:
        grupo = "B"
    
    print(f"Usted pertenece al grupo {grupo}.")

if __name__ == "__main__":
    main()