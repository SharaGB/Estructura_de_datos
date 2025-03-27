# Realice un algoritmo que llene una matriz de 10 * 10.
# Sumar las columnas e imprimir que columna tuvo la máxima suma y la suma de esa columna.
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


def suma_columnas(matriz):
    suma_columnas = []

    for i in range(len(matriz[0])):
        sum_column = 0
        for fila in matriz:
            sum_column += fila[i]
        suma_columnas.append(sum_column)

    max_suma = max(suma_columnas)
    # Ajustar para que la posición sea más intuitiva (comenzando en 1)
    posicion = suma_columnas.index(max_suma) + 1
    return suma_columnas, posicion, max_suma


def main():
    matriz = generar_matriz(10, 10)
    imprimir_matriz(matriz)
    suma_columnas_vector, posicion, max_suma = suma_columnas(matriz)
    print(f"La suma de cada columna es: {suma_columnas_vector}")
    print(f"La columna con la máxima suma es la columna {posicion} con una suma de {max_suma}")


if __name__ == "__main__":
    main()
