def mostrar_menu():
    print("Opciones:")
    print("1. Ingresar repuesto")
    print("2. Mostrar inventario")
    print("3. Vender repuesto")
    print("4. Eliminar repuesto")
    print("5. Salir")


def ingresar_repuesto(inventario):
    referencia = input("Ingrese la referencia del repuesto: ")

    if referencia in inventario:
        print("La referencia ya existe en el inventario.")
        return


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario:")

    for referencia, datos in reversed(list(inventario.items())):
        print(f"Referencia: {referencia}, Marca: {datos['marca']}, Precio: ${datos['precio']:.2f}, Cantidad: {datos['cantidad']}")


def vender_repuesto(inventario):
    referencia = input("Ingrese la referencia del repuesto vendido: ")

    if referencia not in inventario:
        print("La referencia no existe en el inventario.")
        return


def eliminar_repuesto(inventario):
    referencia = input("Ingrese la referencia del repuesto a eliminar: ")

    if referencia in inventario:
        del inventario[referencia]
        print("Repuesto eliminado exitosamente.")
    else:
        print("El repuesto no está en el inventario.")
    mostrar_inventario(inventario)


def main():
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_repuesto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            vender_repuesto(inventario)
        elif opcion == "4":
            eliminar_repuesto(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
