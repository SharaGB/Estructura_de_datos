# Dada una matriz que representa un teatro, donde cada celda
# contiene un objeto Asiento con atributos número, fila, precio,
# implementa un algoritmo para ordenar los asientos dentro de cada fila
# según el precio en orden ascendente.

class Asiento:
    def __init__(self, numero, fila, precio):
        self.numero = numero
        self.fila = fila
        self.precio = precio

    def __repr__(self):
        return f'Asiento({self.numero}, {self.fila}, {self.precio})'


# Función para ordenar los asientos por precio
def ordenar_asientos_por_precio(matriz):
    for fila in matriz:
        fila.sort(key=lambda asiento: asiento.precio)


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def main():
    # Crear la matriz de asientos
    matriz_asientos = [
        [Asiento(1, 'A', 50.0), Asiento(2, 'A', 30.0), Asiento(3, 'A', 40.0)],
        [Asiento(1, 'B', 20.0), Asiento(2, 'B', 60.0), Asiento(3, 'B', 10.0)],
        [Asiento(1, 'C', 70.0), Asiento(2, 'C', 50.0), Asiento(3, 'C', 80.0)]
    ]

    print("Matriz de asientos antes de ordenar:")
    imprimir_matriz(matriz_asientos)

    # Ordenar los asientos por precio
    ordenar_asientos_por_precio(matriz_asientos)

    print("\nMatriz de asientos después de ordenar:")
    imprimir_matriz(matriz_asientos)


if __name__ == "__main__":
    main()
