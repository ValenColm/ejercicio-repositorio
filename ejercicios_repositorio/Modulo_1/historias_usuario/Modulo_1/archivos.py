import csv

def guardar_csv(ruta, inventory):
    "Guarda el inventario en un archivo CSV."
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"✔ Inventario guardado correctamente en {ruta}")

    except Exception as e:
        print(f"❌ Error al guardar CSV: {e}")


def cargar_csv(ruta, inventario_actual):
    """Carga productos desde CSV con validaciones."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)

            if encabezado != ["name", "price", "quantity"]:
                print("❌ El encabezado del CSV no es válido.")
                return inventario_actual

            productos_cargados = []
            filas_invalidas = 0

            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    productos_cargados.append({
                        "name": nombre,
                        "price": precio,
                        "quantity": cantidad
                    })

                except ValueError:
                    filas_invalidas += 1

        # Si no cargó nada
        if not productos_cargados:
            print("❌ No se cargaron productos válidos.")
            return inventario_actual

        print(f"Se cargaron {len(productos_cargados)} productos. Filas inválidas: {filas_invalidas}")

        opcion = input("¿Deseas sobrescribir el inventario actual? (S/N): ").strip().lower()

        if opcion == "s":
            print("✔ Inventario sobrescrito.")
            return productos_cargados

        else:
            print("✔ Inventario fusionado (por nombre).")
            fusionar_inventarios(inventario_actual, productos_cargados)
            return inventario_actual

    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
        return inventario_actual

    except UnicodeDecodeError:
        print("❌ Error de codificación del archivo CSV.")
        return inventario_actual


def fusionar_inventarios(actual, nuevos):
    """Fusiona productos por nombre. Suma cantidades y actualiza precio usando el del CSV."""
    for nuevo in nuevos:
        encontrado = False

        for p in actual:
            if p["name"].lower() == nuevo["name"].lower():
                p["quantity"] += nuevo["quantity"]
                p["price"] = nuevo["price"]
                encontrado = True
                break

        if not encontrado:
            actual.append(nuevo)