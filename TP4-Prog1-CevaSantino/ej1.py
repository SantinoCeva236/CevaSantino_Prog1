x = 0

while x < 30:
    if x == 15:
        print("La ejecución del bucle se interrumpe cuando x era", x)
        break
    
    if x == 4 or x == 6 or x == 10:
        print("El valor", x, "de x fue omitido")
        x += 1
        continue
    
    print('El valor del bucle es:', x)
    x += 1
