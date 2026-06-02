def calcular_dia_nacimiento():
    print("Te diré el día de tu nacimiento\n")

    print("Introduce tu fecha de nacimiento (pulsa Enter después de cada dato):")

    try:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anyo = int(input("Año: "))

        # Validaciones básicas
        if not (1 <= dia <= 31 and 1 <= mes <= 12 and anyo > 0):
            print("Fecha inválida")
            return

    except ValueError:
        print("Debes introducir solo números")
        return

    # Lista de días
    dias_semana = ['sábado', 'domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes']

    # Ajuste de meses y año para la fórmula
    if mes < 3:
        mes += 12
        anyo -= 1

    # Algoritmo
    o1 = ((mes + 1) * 3) // 5
    o2 = anyo // 4
    o3 = anyo // 100
    o4 = anyo // 400
    o5 = dia + (mes * 2) + anyo + o1 + o2 - o3 + o4 + 2
    o6 = o5 // 7
    dia_semana = o5 - (o6 * 7)

    print(f"\n Felicidades! Naciste un {dias_semana[dia_semana]}")

# Ejecutar programa
calcular_dia_nacimiento()
