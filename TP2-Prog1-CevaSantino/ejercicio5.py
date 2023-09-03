def es_vocal(letra):
    vocales = "AEIOUaeiou"
    return letra in vocales

def main():
    letra = input("Ingrese una letra: ")
    
    if len(letra) == 1:
        if es_vocal(letra):
            print("Es vocal.")
        else:
            print("No es vocal.")
    else:
        print("Error: Solo debe ingresar un carácter.")

if __name__ == "__main__":
    main()
