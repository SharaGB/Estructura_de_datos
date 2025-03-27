# Realice un algoritmo que llene una matriz de 5 * 5.
# Calcular la suma de cada fila y almacenarla en un vector, la suma de
# cada columna y almacenarla en otro vector.
from random import randint


def generar_matriz(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(randint(1, 100))
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def suma_filas(matriz):
    suma_filas = []

    for fila in matriz:
        suma_filas.append(sum(fila))
    return suma_filas


def suma_columnas(matriz):
    suma_columnas = []

    for i in range(len(matriz[0])):
        sum_column = 0
        for fila in matriz:
            sum_column += fila[i]
        suma_columnas.append(sum_column)
    return suma_columnas


def main():
    matriz = generar_matriz(5, 5)
    imprimir_matriz(matriz)
    print(f"La suma de cada fila es: {suma_filas(matriz)}")
    print(f"La suma de cada columna es: {suma_columnas(matriz)}")


if __name__ == "__main__":
    main()
