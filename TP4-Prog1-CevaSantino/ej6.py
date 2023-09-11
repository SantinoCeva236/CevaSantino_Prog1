# Crear una lista de números
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Número que queremos encontrar
numero_objetivo = 50

# Utilizar un bucle for para buscar el número objetivo
for numero in numeros:
    if numero == numero_objetivo:
        print(f"¡Encontré el número {numero_objetivo}!")
        break

# Si el bucle se completa sin encontrar el número, se ejecutará este mensaje
else:
    print(f"El número {numero_objetivo} no se encontró en la lista.")

