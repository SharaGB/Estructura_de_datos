# Realice un algoritmo que llene una matriz de 5 * 5
# que almacene toda la matriz en un vector. Imprimir el vector resultante.
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


def matriz_a_vector(matriz):
    vector = []

    for fila in matriz:
        for elemento in fila:
            vector.append(elemento)
    return vector


def main():
    matriz = generar_matriz(5, 5)
    imprimir_matriz(matriz)
    vector = matriz_a_vector(matriz)
    print(f"El vector resultante es: {vector}")


if __name__ == "__main__":
    main()
