# Tienes dos matrices de objetos Producto, una para cada tienda, con
# atributos nombre, precio, stock. Escribe un algoritmo que fusione ambas
# matrices sumando el stock de los productos idénticos. Los productos que
# no son idénticos los debe agregar en la matriz resultante

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.precio}, {self.stock})'


# Función para fusionar las matrices de productos
def fusionar_matrices(matriz1, matriz2):
    productos_dict = {}

    # Agregar productos de la primera matriz al diccionario
    for fila in matriz1:
        for producto in fila:
            if producto.nombre in productos_dict:
                productos_dict[producto.nombre].stock += producto.stock
            else:
                productos_dict[producto.nombre] = Producto(producto.nombre, producto.precio, producto.stock)

    # Agregar productos de la segunda matriz al diccionario
    for fila in matriz2:
        for producto in fila:
            if producto.nombre in productos_dict:
                productos_dict[producto.nombre].stock += producto.stock
            else:
                productos_dict[producto.nombre] = Producto(producto.nombre, producto.precio, producto.stock)

    # Convertir el diccionario de productos en una lista
    productos_list = list(productos_dict.values())

    # Crear la matriz resultante
    matriz_resultante = []
    fila_actual = []

    for producto in productos_list:
        fila_actual.append(producto)
        if len(fila_actual) == len(matriz1[0]):
            matriz_resultante.append(fila_actual)
            fila_actual = []

    if fila_actual:  # Agregar la última fila si no está vacía
        matriz_resultante.append(fila_actual)

    return matriz_resultante


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def main():
    # Crear la primera matriz de productos
    matriz1 = [
        [Producto("Producto 1", 100, 10), Producto("Producto 2", 200, 20)],
        [Producto("Producto 3", 300, 30), Producto("Producto 4", 400, 40)]
    ]

    # Crear la segunda matriz de productos
    matriz2 = [
        [Producto("Producto 2", 200, 5), Producto("Producto 3", 300, 15)],
        [Producto("Producto 5", 500, 25), Producto("Producto 6", 600, 35)]
    ]

    print("Matriz 1:")
    imprimir_matriz(matriz1)

    print("\nMatriz 2:")
    imprimir_matriz(matriz2)

    # Fusionar las matrices de productos
    matriz_fusionada = fusionar_matrices(matriz1, matriz2)

    print("\nMatriz fusionada:")
    imprimir_matriz(matriz_fusionada)


if __name__ == "__main__":
    main()
