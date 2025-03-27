# Dada una matriz y sus dimensiones hacer los siguientes métodos
# a. El máximo número de la matriz lo muestre y su posición
# b. El menor número de la matriz lo muestre y su posición
# c. Imprima toda la columna donde se encuentra el mayor valor
# d. Toda la fila en que se encuentra el máximo elemento
from random import randint


def generar_matriz(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(randint(-100, 100))
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def maximo_matriz(matriz):
    max_valor = matriz[0][0]
    posicion = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                posicion = (i, j)

    # posicion = (posicion[0] + 1, posicion[1] + 1)
    return max_valor, posicion


def minimo_matriz(matriz):
    min_valor = matriz[0][0]
    posicion = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < min_valor:
                min_valor = matriz[i][j]
                posicion = (i, j)

    # posicion = (posicion[0] + 1, posicion[1] + 1)
    return min_valor, posicion


def imprimir_columna(matriz, col):
    for mtrz in matriz:
        print(mtrz[col])


def imprimir_fila(matriz, fila):
    print(matriz[fila])


def main():
    matriz = generar_matriz(5, 6)
    imprimir_matriz(matriz)

    max_valor, pos_max = maximo_matriz(matriz)
    min_valor, pos_min = minimo_matriz(matriz)

    print(f"El máximo número de la matriz es {max_valor} en la posición {pos_max[0] + 1, pos_max[1] + 1}")
    print(f"El menor número de la matriz es {min_valor} en la posición {pos_min[0] + 1, pos_min[1] + 1}")

    print("Columna donde se encuentra el mayor valor:")
    imprimir_columna(matriz, pos_max[1])

    print("Fila donde se encuentra el mayor valor:")
    imprimir_fila(matriz, pos_max[0])


if __name__ == "__main__":
    main()
