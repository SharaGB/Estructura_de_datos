# En una librería organizada como una matriz, cada celda contiene
# un objeto Libro con atributos título, autor y precio. Escribe un
# algoritmo para encontrar el libro con el precio más alto.
# Solución: Recorre la matriz comparando el atributo precio de cada Libro
# para identificar y devolver el libro más caro.

class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __repr__(self):
        return f'Libro("{self.titulo}", "{self.autor}", {self.precio:,.3f})'


# Función para encontrar el libro con el precio más alto
def libro_mas_caro(matriz):
    libro_caro = None
    precio_maximo = 0.0

    for fila in matriz:
        for libro in fila:
            if libro.precio > precio_maximo:
                precio_maximo = libro.precio
                libro_caro = libro
    return libro_caro


# Función para imprimir la matriz de libros
def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def main():
    # Crear la matriz de libros
    matriz_libros = [
        [Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 45.000), Libro("El código Da Vinci", "Dan Brown", 60.000), Libro("It", "Stephen King", 90.000)],
        [Libro("Cincuenta sombras de Grey", "E.L. James", 55.000), Libro("Crepúsculo", "Stephenie Meyer", 50.000), Libro("Los juegos del hambre", "Suzanne Collins", 50.000)],
        [Libro("El alquimista", "Paulo Coelho", 40.000), Libro("Percy Jackson y el ladrón del rayo", "Rick Riordan", 45.000), Libro("El señor de los anillos", "J.R.R. Tolkien", 80.000)]
    ]

    print("Matriz de libros:")
    imprimir_matriz(matriz_libros)

    # Encontrar el libro con el precio más alto
    libro_caro = libro_mas_caro(matriz_libros)
    print(f"\nEl libro más caro es: {libro_caro}")


if __name__ == "__main__":
    main()
