# Realice un algoritmo que llene una matriz de 8 * 8,
# que almacene la suma de las filas y la suma de las columnas en un vector.
# Imprimir el vector resultante.
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
    matriz = generar_matriz(8, 8)
    imprimir_matriz(matriz)
    
    suma_filas_vector = suma_filas(matriz)
    suma_columnas_vector = suma_columnas(matriz)
    
    print(f"La suma de cada fila es: {suma_filas_vector}")
    print(f"La suma de cada columna es: {suma_columnas_vector}")
    
    vector_resultante = suma_filas_vector + suma_columnas_vector
    print(f"El vector resultante es: {vector_resultante}")


if __name__ == "__main__":
    main()
