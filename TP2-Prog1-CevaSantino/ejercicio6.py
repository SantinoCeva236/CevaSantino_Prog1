def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        anio = int(input("Ingrese un año: "))
        
        if es_bisiesto(anio):
            print(f"{anio} es un año bisiesto.")
        else:
            print(f"{anio} no es un año bisiesto.")
    except ValueError:
        print("Error: Por favor ingrese un año válido.")

if __name__ == "__main__":
    main()
