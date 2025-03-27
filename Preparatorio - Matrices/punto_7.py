# En una escuela, los estudiantes están organizados en una matriz, donde
# cada celda contiene un objeto Estudiante con atributos nombre,
# calificación. Escribe un algoritmo que agrupe a los estudiantes en
# diferentes matrices según su calificación (A, B, C, etc.).
# Solución: Crea matrices separadas para cada rango de calificaciones y
# asigna a cada Estudiante a la matriz correspondiente según su calificación.


class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __repr__(self):
        return f'Estudiante("{self.nombre}", "{self.calificacion}")'


# Función para agrupar a los estudiantes por calificación
def agrupar_estudiantes_por_calificacion(matriz):
    grupos = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'F': []
    }

    for fila in matriz:
        for estudiante in fila:
            if estudiante.calificacion in grupos:
                grupos[estudiante.calificacion].append(estudiante)

    # Convertir listas en matrices
    for calificacion in grupos:
        grupos[calificacion] = convertir_a_matriz(grupos[calificacion], len(matriz[0]))

    return grupos


# Función para convertir una lista en una matriz
def convertir_a_matriz(lista, longitud_fila):
    matriz = []
    fila_actual = []

    for item in lista:
        fila_actual.append(item)
        if len(fila_actual) == longitud_fila:
            matriz.append(fila_actual)
            fila_actual = []
    if fila_actual:
        matriz.append(fila_actual)
    return matriz


# Función para imprimir los grupos de estudiantes
def imprimir_grupos(grupos):
    for calificacion, matriz in grupos.items():
        print(f"Calificación {calificacion}:")
        for fila in matriz:
            print(" | ".join([str(x).center(26) for x in fila]))
        print()


def main():
    # Crear la matriz de estudiantes
    matriz_estudiantes = [
        [Estudiante("Alice", "A"), Estudiante("Bob", "B"), Estudiante("Charlie", "C")],
        [Estudiante("David", "A"), Estudiante("Eve", "B"), Estudiante("Frank", "D")],
        [Estudiante("Grace", "C"), Estudiante("Heidy", "F"), Estudiante("Ivan", "A")]
    ]

    print("Matriz de estudiantes:")
    for fila in matriz_estudiantes:
        print(" | ".join([str(x).center(26) for x in fila]))

    # Agrupar a los estudiantes por calificación
    grupos = agrupar_estudiantes_por_calificacion(matriz_estudiantes)

    print("\nGrupos de estudiantes por calificación:")
    imprimir_grupos(grupos)


if __name__ == "__main__":
    main()
