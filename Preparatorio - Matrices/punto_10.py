# Se tiene un matriz con n productos y se requiere saber cuántos productos
# están en oferta. Solución cree una matriz cuadrada e incremente la
# cantidad que productos en ofertas y muestre el total

class Producto:
    def __init__(self, nombre, precio, en_oferta):
        self.nombre = nombre
        self.precio = precio
        self.en_oferta = en_oferta

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.precio}, {"En oferta" if self.en_oferta else "No en oferta"})'


# Función para contar los productos en oferta
def contar_productos_en_oferta(matriz):
    total_en_oferta = 0

    for fila in matriz:
        for producto in fila:
            if producto.en_oferta:
                total_en_oferta += 1
    return total_en_oferta


# Función para imprimir la matriz de productos
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" | ".join([str(x).center(45) for x in fila]))


def main():
    # Crear la matriz de productos (n x n)
    matriz_productos = [
        [Producto("Producto 1", 100, True), Producto("Producto 2", 200, False), Producto("Producto 3", 150, True)],
        [Producto("Producto 4", 250, True), Producto("Producto 5", 300, False), Producto("Producto 6", 350, True)],
        [Producto("Producto 7", 400, False), Producto("Producto 8", 450, True), Producto("Producto 9", 500, False)]
    ]

    print("Matriz de productos:")
    imprimir_matriz(matriz_productos)

    # Contar los productos en oferta
    total_en_oferta = contar_productos_en_oferta(matriz_productos)

    print(f"\nTotal de productos en oferta: {total_en_oferta}")


if __name__ == "__main__":
    main()
