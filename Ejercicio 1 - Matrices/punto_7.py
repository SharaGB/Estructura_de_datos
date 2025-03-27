# Realice un algoritmo que llene una matriz de 5 * 6
# y que imprima cuantos de los números almacenados son ceros,
# cuántos son positivos y cuantos son negativos.
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


def ceros_positivos_negativos(matriz):
    ceros = 0
    num_positivo = 0
    num_negativo = 0

    for i in matriz:
        for j in i:
            if j == 0:
                ceros += 1
            elif j > 0:
                num_positivo += 1
            else:
                num_negativo += 1

    print(f"Ceros: {ceros}")
    print(f"Números positivos: {num_positivo}")
    print(f"Número negativos: {num_negativo}")


def main():
    matriz = generar_matriz(5, 6)
    imprimir_matriz(matriz)
    ceros_positivos_negativos(matriz)


if __name__ == "__main__":
    main()
