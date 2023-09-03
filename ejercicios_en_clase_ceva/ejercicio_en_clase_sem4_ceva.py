# Solicitar al usuario el corrimiento
corrimiento = int(input("Ingrese la cantidad de lugares a mover las letras (corrimiento): "))

# Crear una cadena con el alfabeto
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

# Solicitar al usuario 5 mensajes y encriptarlos
for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i + 1}: ")
    mensaje_encriptado = ""

    for letra in mensaje:
        if letra.isalpha():  # Solo encriptar letras, ignorar otros caracteres
            mayuscula = letra.isupper()  # Verificar si la letra es mayúscula
            letra = letra.lower()  # Convertir a minúscula para hacer el corrimiento
            if letra in alfabeto:
                indice = (alfabeto.index(letra) + corrimiento) % 27  # Calcular el nuevo índice
                letra_encriptada = alfabeto[indice]  # Obtener la letra encriptada
                if mayuscula:
                    letra_encriptada = letra_encriptada.upper()  # Si era mayúscula, convertir a mayúscula nuevamente
                mensaje_encriptado += letra_encriptada
        else:
            mensaje_encriptado += letra  # Mantener caracteres no alfabéticos sin cambios

    # Imprimir el mensaje encriptado
    print(f"Mensaje {i + 1} encriptado: {mensaje_encriptado}")
