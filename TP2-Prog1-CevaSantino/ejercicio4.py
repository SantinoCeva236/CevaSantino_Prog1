def main():
    print("Candidatos:")
    print("A - Candidato del partido rojo")
    print("B - Candidato del partido verdad")
    print("C - Candidato del partido azul")
    
    eleccion = input("Ingrese la letra del candidato por el cual desea votar: ").upper()
    
    if eleccion == "A":
        print("Usted ha votado por el partido rojo.")
    elif eleccion == "B":
        print("Usted ha votado por el partido verdad.")
    elif eleccion == "C":
        print("Usted ha votado por el partido azul.")
    else:
        print("Opción errónea: Por favor ingrese una opción válida (A, B o C).")

if __name__ == "__main__":
    main()
