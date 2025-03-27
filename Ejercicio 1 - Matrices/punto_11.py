# Se tiene una matriz con las calificaciones de un N grupo de personas, con 5 exámenes diferentes, cree un programa que
# a. Muestre el promedio de cada uno de los estudiantes
# b. Los estudiantes que obtuvieron la mejor calificación en la nota 3
# c. Cuáles fueron los estudiantes que obtuvieron la mejor nota en el examen 1 y 5
# d. Cuáles de las notas obtuvo el promedio más alto

def generar_matriz_calificaciones(estudiantes, examenes):
    matriz = []

    for i in range(estudiantes):
        fila = []
        for j in range(examenes):
            calificacion = float(input(f"Introduce la calificación del estudiante {i + 1} para el examen {j + 1}: "))
            fila.append(calificacion)
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def promedio_estudiantes(matriz):
    promedios = []

    for i in matriz:
        promedio = sum(i) / len(i)
        promedios.append(promedio)
    return promedios


def mejor_calificacion_nota(matriz, nota):
    mejor_calificacion = float('0.0')
    estudiantes = []

    # Encontrar la mejor calificación en la nota especificada
    for fila in matriz:
        if fila[nota - 1] > mejor_calificacion:
            mejor_calificacion = fila[nota - 1]

    # Encontrar los estudiantes que obtuvieron la mejor calificación
    for i in range(len(matriz)):
        if matriz[i][nota - 1] == mejor_calificacion:
            estudiantes.append(i + 1)

    return estudiantes, mejor_calificacion


def mejor_calificacion_examenes(matriz, examenes):
    resultados = {}

    for examen in examenes:
        estudiantes, mejor_calificacion = mejor_calificacion_nota(matriz, examen)
        resultados[examen] = (estudiantes, mejor_calificacion)
    return resultados


def nota_con_promedio_mas_alto(matriz):
    promedios_notas = []
    num_notas = len(matriz[0])

    for i in range(num_notas):
        suma = 0
        for fila in matriz:
            suma += fila[i]
        promedio = suma / len(matriz)
        promedios_notas.append(promedio)

    max_promedio = max(promedios_notas)
    nota_mas_alta = promedios_notas.index(max_promedio) + 1

    return nota_mas_alta, max_promedio


def main():
    estudiantes = int(input("Introduce el número de estudiantes: "))
    examenes = 5

    matriz_calificaciones = generar_matriz_calificaciones(estudiantes, examenes)

    print("Matriz de calificaciones:")
    imprimir_matriz(matriz_calificaciones)

    # a. Promedio de cada uno de los estudiantes
    promedios = promedio_estudiantes(matriz_calificaciones)
    for i, promedio in enumerate(promedios, start=1):
        print(f"El promedio del estudiante {i} es: {promedio:.2f}")

    # b. Estudiantes con la mejor calificación en la nota 3
    estudiantes_nota_3, mejor_nota_3 = mejor_calificacion_nota(matriz_calificaciones, 3)
    print(f"Los estudiantes con la mejor calificación en la nota 3, son: {estudiantes_nota_3} con una calificación de {mejor_nota_3}")

    # c. Estudiantes con la mejor calificación en el examen 1 y 5
    examenes_a_verificar = [1, 5]
    mejores_calificaciones = mejor_calificacion_examenes(matriz_calificaciones, examenes_a_verificar)
    for examen, (estudiantes, calificacion) in mejores_calificaciones.items():
        print(f"Los estudiantes con la mejor calificación en el examen {examen}, son: {estudiantes} con una calificación de {calificacion}")

    # d. Nota con el promedio más alto
    nota_mas_alta, promedio_mas_alto = nota_con_promedio_mas_alto(
        matriz_calificaciones)
    print(f"La nota con el promedio más alto es la nota {nota_mas_alta} con un promedio de {promedio_mas_alto:.2f}")


if __name__ == "__main__":
    main()
