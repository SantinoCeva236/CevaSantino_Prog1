def main():
    # Solicitar al usuario que ingrese la fecha en el formato deseado
    fecha_input = input("Ingrese la fecha en el formato día, DD/MM: ")

    # Dividir la entrada en día y fecha
    try:
        dia_semana, fecha = fecha_input.split(', ')
        dia, mes = fecha.split('/')
    except ValueError:
        print("Error en el formato de fecha.")
        return

    # Definir los días de la semana y sus niveles correspondientes
    dias_semana = {
        'lunes': 'inicial',
        'martes': 'intermedio',
        'miércoles': 'avanzado',
        'jueves': 'práctica hablada',
        'viernes': 'inglés para viajeros'
    }

    # Convertir el día y el mes a enteros
    try:
        dia = int(dia)
        mes = int(mes)
    except ValueError:
        print("Error en el formato de día o mes.")
        return

    dia_semana_lower = dia_semana.lower()
    nivel = dias_semana.get(dia_semana_lower)

    if not nivel:
        print("Día de la semana inválido.")
        return

    if dia > 31 or mes > 12:
        print("Fecha inválida.")
        return

    if nivel in ['inicial', 'intermedio', 'avanzado']:
        # Preguntar si hubo exámenes
        hubo_examenes = input("¿Hubo exámenes en este nivel? (Si/No): ").lower()

        if hubo_examenes == "si":
            try:
                aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
                no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
                total_alumnos = aprobados + no_aprobados
                porcentaje_aprobados = (aprobados / total_alumnos) * 100
                print(f"El porcentaje de aprobados es: {porcentaje_aprobados:.2f}%")
            except ValueError:
                print("Entrada inválida para la cantidad de alumnos.")
    elif nivel == 'práctica hablada':
        try:
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
            if asistencia > 50:
                print("Asistió la mayoría.")
            else:
                print("No asistió la mayoría.")
        except ValueError:
            print("Entrada inválida para el porcentaje de asistencia.")
    elif nivel == 'inglés para viajeros':
        if (dia, mes) == (1, 1) or (dia, mes) == (1, 7):
            print("Comienzo de nuevo ciclo")
            try:
                cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
                ingreso_total = cantidad_alumnos * arancel
                print(f"Ingreso total en $: {ingreso_total:.2f}")
            except ValueError:
                print("Entrada inválida para la cantidad de alumnos o el arancel.")
        else:
            print("No es el comienzo de un nuevo ciclo.")

if __name__ == "__main__":
    main()
