# Inicializar contadores
pares_total = 0
impares_total = 0

# Solicitar números hasta que se ingrese 0
while True:
    numero = int(input("Ingrese un número entero positivo (0 para salir): "))
    
    if numero == 0:
        break
    
    # Inicializar contadores para el número actual
    pares = 0
    impares = 0
    
    # Calcular la cantidad de dígitos pares e impares en el número
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito del número
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10  # Eliminar el último dígito del número
    
    # Informar la cantidad de dígitos pares e impares en el número actual
    print(f"Dígitos pares: {pares}, Dígitos impares: {impares}")
    
    # Actualizar los contadores totales
    pares_total += pares
    impares_total += impares

# Informar la cantidad total de dígitos pares e impares
print(f"\nTotal de dígitos pares: {pares_total}")
print(f"Total de dígitos impares: {impares_total}")
