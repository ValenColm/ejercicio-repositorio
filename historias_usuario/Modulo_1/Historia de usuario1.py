#Solicitar al usuario los datos del producto
name = input("Ingresa el nombre del producto que compraste => ")
price = input("Ingresa el precio del producto que compraste => ")
quantity = input("Ingresa la cantidad del producto que compraste => ")

#Verificar que el precio y la cantidad sean números válidos
if price.isdigit() and quantity.isdigit():
    #Convertir los valores a enteros para realizar operaciones matemáticas
    price = int(price)
    quantity = int(quantity)
    #Calculo del costo total del producto.
    costo_total = price * quantity
    #Mostrar los datos del producto y resultado del calculo
    print(f"Producto = {name} | Precio = {price} | Cantidad = {quantity} | Costo Total = {costo_total}")

#Mostrar un mensaje de error, si los valores ingresados son invalidos.
else:
    print("Error: Ingresa solo números válidos para precio y cantidad.")








print( 13 + 10 )
print(19 +20 )
print(40 + 30 )
print( 4 + 5)
print( 38 + 45)
print( 35 + 35)
