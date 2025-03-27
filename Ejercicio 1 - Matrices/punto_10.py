# Llene los elementos en una matriz de m*n de tipo cadena,
# mediante un método va averiguar la cantidad de dígitos que hay en cada posición
# y los va a guardar en otra matriz, se deben mostrar las dos matrices

def generar_matriz_cadenas(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            cadena = input(
                f"Introduce una cadena para la posición ({i}, {j}): ")
            fila.append(cadena)
        matriz.append(fila)
    return matriz


def contar_digitos(cadena):
    contador = 0

    for caracter in cadena:
        if caracter.isdigit():
            contador += 1
    return contador


def generar_matriz_digitos(matriz_cadenas):
    filas = len(matriz_cadenas)
    columnas = len(matriz_cadenas[0])
    matriz_digitos = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            num_digitos = contar_digitos(matriz_cadenas[i][j])
            fila.append(num_digitos)
        matriz_digitos.append(fila)
    return matriz_digitos


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


def main():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    print("**** Introduce las cadenas para la matriz ****")
    matriz_cadenas = generar_matriz_cadenas(filas, columnas)

    matriz_digitos = generar_matriz_digitos(matriz_cadenas)

    print("Matriz de cadenas:")
    imprimir_matriz(matriz_cadenas)

    print("Matriz de dígitos:")
    imprimir_matriz(matriz_digitos)


if __name__ == "__main__":
    main()
