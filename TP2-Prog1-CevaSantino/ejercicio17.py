def main():
    dia_semana = input("Ingrese un día de la semana: ").lower()
    
    if dia_semana == "lunes":
        print("¡Es el comienzo de la semana!")
    elif dia_semana == "viernes":
        print("¡Es viernes, casi llegamos al fin de semana!")
    elif dia_semana == "sabado" or dia_semana == "domingo":
        print("¡Es fin de semana, a relajarse!")
    else:
        print("¡A laburar!")

if __name__ == "__main__":
    main()
