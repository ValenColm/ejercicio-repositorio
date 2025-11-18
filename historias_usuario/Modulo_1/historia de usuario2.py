
# Lista donde se almacenarán los productos (como diccionarios)

inventario = []

def agregar_producto():
    
    #Esta función permite agregar un nuevo producto al inventario.  
    # Pide al usuario el nombre, precio y cantidad, y lo guarda como un diccionario.

    nombre = input("ingresa el nombre del producto: ")
#validamos que el precio y la cantidad sean numeros validos
    while True:
            try:
                precio = float(input("ingrese el precio del producto : "))
                cantidad = int(input("ingresa la cantidad de productos: "))
                break
            except ValueError:
                print("ERROR: debe ingresar numeros validos para precio y cantidad : ")
    #crear diccionario con los datos del producto            
    producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
            }
        #agregar producto al inventario
    inventario.append(producto)
    print(f" producto{nombre} agregado correctamente : ")
        
        
def mostrar_inventario() :

    #Muestra todos los productos guardados en el inventario Si no hay productos, muestra un mensaje.       
            
    if not inventario:
        print("")
        print("El inventario esta vacio.")
        print("")
    else: 
        print("inventario: ")
        for producto in inventario:
            print(f"producto: {producto["nombre"]}|precio: {producto["precio"]}")

def calcular_estadistica():

    #Calcula y muestra el valor total del inventario y la cantidad total de productos registrados.
        
    if len(inventario) == 0:
        print("no hay productos para calcular estadistica")
        return 
    valor_total = 0
    cantidad_total = 0
            
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_total += producto["cantidad"]
                
    print("ESTADISTICA: ")
    print(f"valor total del inventario: {valor_total}")
    print(f"Cantidad total del inventario: {cantidad_total}")
                    
    #Muestra el menú principal y gestiona las opciones del usuario.
    

while True:
    print("===MENU PRINCIPAL===")
    print("1.AGREGAR PRODUCTO")
    print("2.MOSTRAR PRODUCTO")
    print("3.CALCULAR ESTADISTICA")
    print("4. SALIR")
    
    opcion = input("seleccione una opcion (1-4): ")
    
# validacion de las opciones if, elif, else     
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadistica()
    elif opcion == "4":
        print ("saliendo del programa.")
        break
    else:
        print("opcion invalida por favor, ingrese un numero del 1 al 4.")
#inicio del programa            

    
    # Esta semana aprendimos a crear un programa modular en Python,
    # usando funciones, bucles, condicionales y listas de diccionarios
    # para simular un sistema de inventario básico y funcional.