# Realice un algoritmo que llene una matriz de 5 * 5 y determine la
# posición [fila ,columna] del número mayor almacenado en la matriz.
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
    for fila in matriz:
        print(" | ".join([str(x).center(3) for x in fila]))


def encontrar_maximo(matriz):
    max_valor = matriz[0][0]
    posicion = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                posicion = (i, j)

    # Ajustar posición comenzando en 1
    posicion = (posicion[0] + 1, posicion
                [1] + 1)  # (fila, columna)
    return max_valor, posicion


def main():
    matriz = generar_matriz(5, 5)
    imprimir_matriz(matriz)
    max_valor, posicion = encontrar_maximo(matriz)
    print(f"\nEl número mayor almacenado en la matriz es: {max_valor} en la posición {posicion}")


if __name__ == "__main__":
    main()
