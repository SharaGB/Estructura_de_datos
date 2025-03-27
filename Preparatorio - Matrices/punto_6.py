# Dada una matriz que representa las estanterías de un supermercado, donde
# cada celda contiene un objeto Producto con atributos nombre, precio,
# disponibilidad (booleano), escribe un algoritmo que filtre y devuelva
# una nueva matriz con solo los productos disponibles.
# Solución: Recorre la matriz original, copiando a una nueva matriz únicamente
# los Producto cuyo atributo disponibilidad sea true.

class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.precio}, {"Disponible" if self.disponibilidad else "No disponible"})'


# Función para filtrar los productos disponibles
def filtrar_productos_disponibles(matriz):
    matriz_filtrada = []

    for fila in matriz:
        fila_filtrada = []
        for producto in fila:
            if producto.disponibilidad:
                fila_filtrada.append(producto)
        if fila_filtrada:
            matriz_filtrada.append(fila_filtrada)
    return matriz_filtrada


# Función para imprimir la matriz de productos
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" | ".join([str(x).center(42) for x in fila]))


def main():
    # Crear la matriz de productos
    matriz_productos = [
        [ Producto("Producto 1", 100, True), Producto("Producto 2", 200, False), Producto("Producto 3", 300, True)],
        [Producto("Producto 4", 400, True), Producto("Producto 5", 500, False), Producto("Producto 6", 600, True)],
        [Producto("Producto 7", 700, False), Producto("Producto 8", 800, True), Producto("Producto 9", 900, True)]
    ]

    print("Matriz de productos:")
    imprimir_matriz(matriz_productos)

    # Filtrar los productos disponibles
    matriz_filtrada = filtrar_productos_disponibles(matriz_productos)

    print("\nMatriz de productos disponibles:")
    imprimir_matriz(matriz_filtrada)


if __name__ == "__main__":
    main()
