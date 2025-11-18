#EJERCICI  FIZZ BUZZ
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif  i % 5 == 0:
        print("buzz") 
    else :
        print(i)
        
        
#segundo ejercicio
numeros = [3, -1, 0, 7, -5, 0, 12, -8] 


positivos = []
negativos = []
cero = []

for num in numeros :
    if num > 0 :
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
    else :
        cero.append(num)
        
print (f"numeros positivos:", [positivos])
print (f"numeros negativos:", [negativos])
print (f"cero:", [cero]) 


# tercer ejercicio
def contar_vocales (texto):
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    texto = texto.lower()
    for letra in texto:
        if letra in conteo :
            conteo [letra] +=1
            
    return conteo
print (contar_vocales ("hola, como estas cabezon"))
print(contar_vocales(" "))
print (contar_vocales ("AEIOU aeiou"))


# cuarto ejercicio

tareas = [
    {"titulo": "ejercios", "completada": True},
    {"titulo": "python", "completada": True},
    {"titulo": "ejercicios 2", "completada": False}
]

def agregar_tarea(titulo):
    tarea = {"titulo": titulo, "completada": False}
    tareas.append(tarea)
    print("Tarea agregada correctamente.")
    
    
def completar_tareas(indice):
    if 0<= indice < len(tareas):
        tareas[indice] ["completada"]= True
        print("tarea marcada como completada")
    else:
        print("indice olvidado.")
        
def mostrar_tareas():
    print("\n=== LISTA DE TAREAS ===")
    if not tareas:
        print("No hay tareas aún.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. {tarea['titulo']} - {estado}")
    print()
    
    
while True:
    print("1. Agregar tareas")
    print("2. Marcar tareas como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
        
    opcion = input("elige una opcion: " )
        
    if opcion == "1":
        titulo = input("titulo de nueva tarea que deseas agregar: ").strip()
        if titulo:
            agregar_tarea(titulo)
        else:
            print ("el titulo no puede estra vacio")
            
    elif opcion == "2":
        try:
            indice = int(input("Índice de la tarea a completar: "))
            completar_tareas(indice)
        except ValueError:
                print("Por favor ingresa un número válido.")

    elif opcion == "3":
            mostrar_tareas()

    elif opcion == "4":
            print("¡Hasta luego!")
            break

    else:
            print("Opción inválida, Intenta otra vez.")
