def main():
    usuario_correcto = "Gwenevere"
    contrasena_correcta = "excalibur"
    
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
    else:
        print("Acceso denegado.")

if __name__ == "__main__":
    main()
