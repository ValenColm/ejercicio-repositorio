

#ejercicio 1
with open("frutas.txt", "w") as file:
        for i in range (1,6):       
            fruits =  input("ingresa una fruta : ")
            file.write(fruits+  "\n")
            
#ejercicio 2
with open ("frutas.txt", "r") as file:
        lineas = file.readlines()
        print(f"cantidad de lineas:", len(lineas))
        
#ejercicio 3
palabra = ("ingresa una palabra a buscar").lower()

with open ("frutas.txt", "r") as file:
    for linea in file:
        if palabra in linea.lower():
            print("encontrado en :", {linea})
            
#ejercicio 4
while True:
    tarea = input("Escribe una tarea (o 'salir'): ")
    if tarea.lower() == "salir":
        break
    with open("tareas.txt", "a") as file:
        file.write(tarea + "\n")

# Mostrar todas
with open("tareas.txt", "r") as file:
    print(file.read())
    
    
#ejercicio 5
with open("pares.txt", "w") as file:
    for n in range (1,101):
        if n  % 2 == 0:
            file.writable(str(n) + "\n" ) 
            
            
            
#ejercicio 5
with open("nombres.txt", "r") as file:
    with open("MAYUSCULA.txt", "w") as salida:
        for linea in file:
            salida.write(linea.upper())

