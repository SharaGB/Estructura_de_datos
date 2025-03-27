# Se tiene una matriz 5*12 la cual cada fila corresponde a cada vendedor y sus
# ventas en el año, se requiere sumar por fila e identificar cuál de todos los
# vendedores vendió mas en el año, debe mostrar el nombre y valor de la venta.
# Solución: recorra una matriz 5* 12 y suma cada fila y
# las compara para saber cuál de los vendedores vendió mas

class Vendedor:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas

    def __repr__(self):
        return f'Vendedor("{self.nombre}", {self.ventas})'


# Función para sumar las ventas por fila e identificar al mejor vendedor
def mejor_vendedor(matriz, vendedores):
    max_ventas = 0
    mejor_vendedor = None

    for i, fila in enumerate(matriz):
        suma_ventas = sum(fila)
        if suma_ventas > max_ventas:
            max_ventas = suma_ventas
            mejor_vendedor = vendedores[i]

    return mejor_vendedor, max_ventas


# Función para imprimir la matriz de ventas
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" | ".join([str(x).center(5) for x in fila]))

def main():
    # Crear la lista de vendedores
    vendedores = [
        Vendedor("Vendedor 1", []),
        Vendedor("Vendedor 2", []),
        Vendedor("Vendedor 3", []),
        Vendedor("Vendedor 4", []),
        Vendedor("Vendedor 5", [])
    ]

    # Crear la matriz de ventas (5 filas, 12 columnas)
    matriz_ventas = [
        [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700],
        [200, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800],
        [300, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900],
        [400, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000],
        [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100]
    ]

    print("Matriz de ventas:")
    imprimir_matriz(matriz_ventas)

    # Identificar al mejor vendedor
    mejor, ventas = mejor_vendedor(matriz_ventas, vendedores)

    print(f"\nEl mejor vendedor es {mejor.nombre} con ventas totales de {ventas}")


if __name__ == "__main__":
    main()
