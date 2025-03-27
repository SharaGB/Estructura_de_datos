# Realice un algoritmo que almacene números en una matriz de 6 * 6.
# Imprimir la suma de los números almacenados en la matriz.
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


def suma_matriz(matriz):
    suma = sum([sum(i) for i in matriz])
    return suma


def main():
    matriz = generar_matriz(6, 6)

    imprimir_matriz(matriz)
    print(f"\nLa suma de los números almacenados en la matriz es: {suma_matriz(matriz)}")


if __name__ == "__main__":
    main()
