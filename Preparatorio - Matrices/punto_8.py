# Dada una lista de productos con atributos nombre, peso,
# categoría, llena una matriz que represente las estanterías de un almacén.
# Cada producto debe ubicarse en la sección correspondiente según su categoría.
# Solución: Agrupa los productos por categoría en vectores y
# luego llena la matriz con los vectores organizados por categoría

class Producto:
    def __init__(self, nombre, peso, categoria):
        self.nombre = nombre
        self.peso = peso
        self.categoria = categoria

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.peso}, "{self.categoria}")'


# Función para agrupar los productos por categoría
def agrupar_productos_por_categoria(lista_productos):
    categorias = {}

    for producto in lista_productos:
        if producto.categoria not in categorias:
            categorias[producto.categoria] = []
        categorias[producto.categoria].append(producto)
    return categorias


# Función para llenar la matriz con los productos agrupados por categoría
def llenar_matriz_con_productos(categorias, filas, columnas):
    matriz = []

    for categoria, productos in categorias.items():
        fila_actual = []
        for producto in productos:
            fila_actual.append(producto)
            if len(fila_actual) == columnas:
                matriz.append(fila_actual)
                fila_actual = []
        if fila_actual:
            matriz.append(fila_actual)
    return matriz


# Función para imprimir la matriz de productos
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" | ".join([str(x).center(30) for x in fila]))


def main():
    # Crear la lista de productos
    lista_productos = [
        Producto("Producto 1", 10, "A"), Producto("Producto 2", 20, "B"), Producto("Producto 3", 15, "A"),
        Producto("Producto 4", 25, "C"), Producto("Producto 5", 30, "B"), Producto("Producto 6", 35, "C"),
        Producto("Producto 7", 40, "A"), Producto("Producto 8", 45, "B"), Producto("Producto 9", 50, "C")
    ]

    # Agrupar los productos por categoría
    categorias = agrupar_productos_por_categoria(lista_productos)

    # Llenar la matriz con los productos agrupados por categoría
    matriz_productos = llenar_matriz_con_productos(categorias, 3, 3)

    print("Matriz de productos:")
    imprimir_matriz(matriz_productos)


if __name__ == "__main__":
    main()
