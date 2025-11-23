from archivos import guardar_csv, cargar_csv

inventory = [
    {"name": "escoba", "price": 15.0, "quantity": 50900},
    {"name": "puerta", "price": 20.0, "quantity": 30000},
    {"name": "puerta", "price": 25.0, "quantity": 1000},
    {"name": "cama", "price": 30.0, "quantity": 50000},
]

def mostrar_inventario(inventario):
    print("inventario de productos")
    for productos in inventario:
        print(f"name: {productos['name']}, price: {productos['price']}, quantity: {productos['quantity']}")
    print()


def agregar_producto(inventory):
    name = input("ingrese el nombre del producto: ")
    
    try:
        price = float(input("ingrese el precio del producto: "))
        quantity = int(input("ingrese la cantidad de productos: "))
    except ValueError:
        print("debe ingresar numeros validos")
        return 
    
    if price <= 0 or quantity <= 0:
        print("precio y cantidad deben ser positivos")
        return

    inventory.append({
        "name": name,
        "price": price,
        "quantity": quantity,
    })
    
    print("producto agregado correctamente")


def buscar_producto(inventory):
    name = input("ingresa el nombre del producto que deseas encontrar:")
    for productos in inventory:
        if productos["name"].lower() == name.lower():
            print("producto encontrado: ")
            print(f"name: {productos['name']}, price: {productos['price']}, quantity: {productos['quantity']}")
            return productos
    return None


def actualizar_producto(inventory, new_price=None, new_quantity=None):
    
    name = input("ingresa el nombre del producto que deseas actualizar : ")
    for productos in inventory:
        if productos["name"].lower() == name.lower():
            new_name = input("Ingresa el nuevo nombre del producto:")
            try:
                new_price = float(input("ingresa el nuevo precio: "))
                new_quantity = int(input("Ingresa la nueva cantidad del producto: "))
            except ValueError:
                print("INGRESA UN VALOR VALIDO")
                return

            if new_price < 0 or new_quantity < 0:
                print("precio y cantidad deben ser positivos.")
                return

            productos["price"] = new_price
            productos["quantity"] = new_quantity
            productos["name"] = new_name

            print("producto actualizado correctamente.\n")
            return
    
    print("producto no encontrado.")


def eliminar_producto(inventory):
    title = input("Ingresa el nombre del producto que vas a eliminar: ")
    
    for productos in inventory:
        if productos["name"].lower() == title.lower():
            inventory.remove(productos)
            print("producto eliminado correctamente")
            return

    print("producto no encontrado en el sistema")


def calcular_estadisticas(inventory):
    if not inventory:
        print("No hay productos para calcular estadísticas")
        return

    valor_total = sum(p["price"] * p["quantity"] for p in inventory)
    cantidad_total = sum(p["quantity"] for p in inventory)
    producto_mas_caro = max(inventory, key=lambda p: p["price"])
    producto_mayor_stock = max(inventory, key=lambda p: p["quantity"])

    return {
        "valor_total": valor_total,
        "cantidad_total": cantidad_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }


def menu():
    while True:
        print("menu principal")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        try:
            opcion = int(input("seleccione una opcion (1-9): "))
        except ValueError:
            print("ERROR NUMERO INGRESADO NO VALIDO")
            continue

        if opcion == 1:
            agregar_producto(inventory)
        elif opcion == 2:
            mostrar_inventario(inventory)
        elif opcion == 3:
            buscar_producto(inventory)
        elif opcion == 4:
            actualizar_producto(inventory)
        elif opcion == 5:
            eliminar_producto(inventory)
        elif opcion == 6:
            calculado = calcular_estadisticas(inventory)
            print(
                f"cantidad total: {calculado['cantidad_total']} | "
                f"producto más caro: {calculado['producto_mas_caro']['name']} | "
                f"producto con mayor stock: {calculado['producto_mayor_stock']['name']} | "
                f"valor total: {calculado['valor_total']}"
            )
        elif opcion == 7:
            ruta = input("Ingresa la ruta del archivo: ")
            guardar_csv(inventory, ruta)
        elif opcion == 8:
            ruta = input("Ingresa la ruta del archivo: ")
            cargar_csv(ruta, inventory)
        elif opcion == 9:
            print("saliendo del programa.")
            break
        else:
            print("opcion invalida por favor, ingrese un numero del 1 al 9.")
