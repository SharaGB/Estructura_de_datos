def mostrar_menu():
    print("Opciones:")
    print("1. Registrar un producto")
    print("2. Modificar un producto")
    print("3. Eliminar un producto")
    print("4. Registrar una venta")
    print("5. Mostrar inventario")
    print("6. Salir")


def registrar_producto(inventario):
    referencia = input("Ingrese la referencia del producto: ")
    nombre = input("Ingrese el nombre del producto: ")

    if referencia in inventario:
        print("La referencia ya existe en el inventario.")
        return

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")
    
    inventario[referencia] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    print("Producto registrado exitosamente.")


def modificar_producto(inventario):
    referencia = input("Ingrese la referencia del producto a modificar: ")
    nombre = input("Ingrese el nuevo nombre del producto: ")

    if referencia not in inventario:
        print("La referencia no existe en el inventario.")
        return
    print("Datos actuales:", inventario[referencia])
    
    while True:
        try:
            cantidad = input("Ingrese la nueva cantidad: ")
            if cantidad:
                cantidad = int(cantidad)
                if cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                    continue
                break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")

    while True:
        try:
            precio = input("Ingrese el nuevo precio: ")
            if precio:
                precio = float(precio)
                if precio < 0:
                    print("Error: El precio no puede ser negativo.")
                    continue
                break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")
    
    if nombre:
        inventario[referencia]["nombre"] = nombre
    if cantidad:
        inventario[referencia]["cantidad"] = int(cantidad)
    if precio:
        inventario[referencia]["precio"] = float(precio)
    print("Producto modificado exitosamente.")


def eliminar_producto(inventario):
    referencia = input("Ingrese la referencia del producto a eliminar: ")
    
    if referencia in inventario:
        del inventario[referencia]
        print("Producto eliminado exitosamente.")
    else:
        print("La referencia no existe en el inventario.")


def registrar_venta(inventario):
    referencia = input("Ingrese la referencia del producto vendido: ")
    if referencia not in inventario:
        print("La referencia no existe en el inventario.")
        return
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser un número mayor a uno.")
                continue
            if cantidad > inventario[referencia]["cantidad"]:
                print("No hay suficiente stock para realizar la venta.")
                return
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")
            continue

    inventario[referencia]["cantidad"] -= cantidad
    total = cantidad * inventario[referencia]["precio"]
    print(f"Venta registrada. Total: ${total:.2f}")
    print(f"Stock restante: {inventario[referencia]['cantidad']} del producto {inventario[referencia]['nombre']}")


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario:")
    
    for referencia, datos in inventario.items():
        print(f"Referencia: {referencia}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")


def main():
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            modificar_producto(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            registrar_venta(inventario)
        elif opcion == "5":
            mostrar_inventario(inventario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
