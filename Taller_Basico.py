import random
nombre = input("ingresa tu nombre: ")
print()
print("="*94)
print(f"Bienvenido al Sistema, {nombre} ingresa un numero entre 1 a 30 para iniciar el programa deseado: ")
print("="*94)
opcion = int(input("""
    1-Hola usuario: saluda al usuario con su nombre y edad.
    2-Suma de dos números.
    3-Calculo de Área de un triángulo.
    4-Conversor de grados Celsius a Fahrenheit.
    5-Tipo de dato: usar type() para mostrar el tipo de variables usadas anteriormente.
    6-Verifica si el usuario es mayor de edad y calcula su edad y cuanto tendra en 10 años.
    7-Verifica si el numero es negativo o positivo
    8-Par o impar.
    9-Calculadora básica con +, -, *, /.
    10-Clasificador de notas (Excelente, Aprobado, Reprobado).
    11-Comparador de tres números: mayor y menor.
    12-Contar del 1 al 10.
    13-Sumatoria del 1 al n.
    14-Tabla de multiplicar.
    15-Contador regresivo con while.
    16-Adivina el número (usar random).
    17-Sumar hasta que el usuario escriba
    18- Lista de frutas.
    19-Agregar y eliminar frutas.
    20-Buscar un elemento en la lista.
    21-Lista de números y promedio.
    22-Números pares: guardar solo los pares.
    23-Eliminar duplicados.  
    24-Sistema de calificaciones.
    25-Carrito de compras.
    26-Cajero automático.
    27-Gestión de estudiantes (mini base de datos).
    28-Calculadora avanzada (usar funciones).
    29-Agenda de contactos (lista de diccionarios).                      

	


"""))
if(opcion == 1):
    nombre = input("ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Hola, {nombre}, Tienes {edad} Años")

elif(opcion == 2):

    #pedir al usuario el primer numero
    num1 = int(input("ingresa el primer numero: "))
    #pedir al usuario el segundo numero
    num2 = int(input("ingresa el segundo numero: "))
    #calcular la suma de ambos numeros
    suma = num1 + num2
    #mostrar el resultado de la suma
    print (f"la suma de, {num1} y {num2} es: {suma} ")

elif(opcion == 3):

    #pedir la base de triangulo al usuario
    base = float(input("introduce la base del triangulo en metros: "))
    #pedir al usuario la altura de triangulo
    altura = float(input("introduce la altura del triangulo en metros: "))
    #calcular el area del triangulo
    area = (base * altura) / 2
    #mostrar el resultado al usuario
    print (f"el area del trianfulo es igual a {area} m")

elif(opcion == 4):

    #pedir al usuario que ingrese la temperatura a grados celsius
    celsius = float(input("introduce la temperatura en grados celsius: "))
    #calcular la temperatura en farenheit
    farenheit = (celsius * 9/5) + 32
    #mostrar el resultado
    print(f"{celsius} equivale a {farenheit} grados farenheit")

elif(opcion == 5):
    texto = "A"
    entero = 1
    flotante = 1.5
    booleano = True
    #consulta los tipos de variables usados anteriormente
    print(type(texto), type(entero), type(nombre), type(flotante), type(booleano))
 
elif(opcion == 6):
    #solicita datos para identificar al usuario
    nombre = input("ingresa tu nombre: ")
    print(f"hola, {nombre} Bienvenido a la calculadora de edad: ")
    #solicita datos para la operacion propuesta.
    año_nacimiento = int (input("ingresa tu año de nacimiento: "))
    año_actual = int (input("ingresa el año actual: "))
    #Calculo de la edad del usuario
    edad = año_actual - año_nacimiento
    #Envia los resultados al usuario
    print (f"hola { nombre} tu edad es {edad} años")
    
    #Verificar si es mayor o menor de edad
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

    edad_futura = edad + 10
    print (f"en 10 años tendras {edad_futura} años:")

elif(opcion == 7):
    #Pedir al usuario un número
    numero = float(input("ingresa un numero"))
    #Verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("el numero es positivo")
    elif numero < 0:
        print("el numero es negativo")
    else :
        print("el numero es cero")

elif(opcion == 8):
   #Pedir al usuario un número entero
    numero = int(input("Ingresa un número entero: "))

    #Verificar si es par o impar
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.") 

elif(opcion == 9):
    #Pedir los dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    #Pedir la operación a realizar
    operacion = input("Ingresa la operación (+, -, *, /): ")

    #Usar condicionales para ejecutar la operación correspondiente
    if operacion == "+":
        print(f"El resultado de la suma es: {num1 + num2}")
    elif operacion == "-":
        print(f"El resultado de la resta es: {num1 - num2}")
    elif operacion == "*":
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"El resultado de la división es: {num1 / num2}")
        else:
            print("Error: no se puede dividir entre cero.")
    else:
        print("Operación no válida.")

elif(opcion == 10 ):
    #pedir la nota al estudiante 
    nota = float("ingresa tu nota (0 a 5): ")
    #clasificar segun el valor
    if nota >= 4.5:
        print ("excelente")
    if nota <= 3.5:
        print("excelente")
    else:
        print ("preprobado")

elif(opcion == 11):


#pedir tres numeros
    a = float(input("ingresa el primer numero: "))
    b = float(input("ingresa el segundo numero: "))
    c = float(input("ingresa el tercecr numero: "))
    #identificar el mayor y el menor
    mayor = max (a , b ,c)
    menor = min (a, b ,c)
    #mostrar el reusltado
    print("el numero mayor es {mayor}")
    print("el numero menor es {menor}")


elif(opcion == 12) :
#inicializar una variable con el numero uno
    contador = 1
#repetir mientras el contador se nenor o igual a diez
    while contador <= 10:
#incrmentar el contador a uno para avanzar
        contador +=1
#mostrar el valor actual del contador
        print(contador)
   

elif(opcion == 13) :
#pedir al usuario el numro limite (n)
    n = int(input("ingresa un numero entero positivo: "))
#inicializar las variables
    contador = 1
    suma = 0
#repetir mientras el contador se menor o igual a n.
    while contador <= n :
    #aumentar el valor del contador suma
        suma += contador
    #aumentar el contador en 1
        contador += 1
        #mostrar el resultado final
        print(f"la sumatoria de 1 hasta {n} es : {suma}")


elif(opcion == 14):
    #pedir al usuario el numero del que desea ver la tabla
    numero = int(input("ingresa un numero para ver su tabla de multiplicar: "))
    #resorer los numeros del 1 al 10 con range()
    for i in range (1, 11):
    #calcular el resultado de la multiplicacion 
        resultado = numero * i
    #mostrar el resultado en un formato legible
        print(f"{numero} * {i} = {resultado}")

elif(opcion == 15):
#pedir al usuario el numero desde le cual desea iniciar la cuenta regresiva
    inicio = int(input("ingresa el numero desde el cual inicia la cuenta regresiva"))
#repetir mientras el numero sea nemor o igual a cero
    while inicio >= 0:
#mostar el numero actual      
        print("inicio")
#restar 1 al valor del inicio en cada iteracion
        inicio -= 1
#mensaje final cundo termina la cuenta    
        print("!iniciar¡")

elif(opcion == 16): 
#generar un numero aleatorio entre 1 y 10
    numero_secreto = random.randint (1 ,10)
#inicializar una variable para guardar el intento del usuario
    intento = 0
#repetir mientras el usuario no adivine el numero
    while intento != numero_secreto: 
#pedir al usuario que ingrese un numero
        intento = int(input("adivina el numero entre (1 y 10): ") )
#comprobar si el numero es correcto
        if intento < numero_secreto:
            print("demasiado bajo, intenta de nuevo")
        elif intento > numero_secreto:
            print("demasiado alto, intentalo de nuevo")
        else :
            print("correcto, adivinaste el nuemro")


elif(opcion == 17):
  suma= 0
#pedir al usuario el primer numero
  numero = float(input("ingresa un numero (0 para terminar): "))
#repetir mientras el numero no sea 0
  while numero != 0:
#acumular el valor ingresado en la variable suma
      suma += numero
#pedir otro numero al usuario
      numero = float(input("ingresa otro numero (0 para terminar): "))
#cuando el usuario ingrese 0, salir del bucle y mostrar el resultado
      print (f"la suma total de los numeros ingresados es: {suma}")

elif(opcion == 18): 
#crear una lista con varias frutas
    frutas = ["manzana, platano, pera, mango, uva"]
#recorrer la lista y mostrar cada frutas
    for fruta in frutas :
        print (fruta)


elif(opcion == 19):
#lista inicial
  frutas = ["mango","pera","cereza","piña","uva"]
#agregar una fruta nueva al final
  frutas.append("toronja")
    #eliminar una fruta de la lista
  frutas.remove("uva")
    #mostrar la lista actualizada
  print(frutas)


elif(opcion == 20): 
#lista de fruta
    fruta = ["mango","pera","guayaba","cambur","piña","uva"]
    # pedir al ususario una fruta para buscar
    buscar = input("escribe fruta para buscar:")
    #verificar si esta en la lista
    if buscar in fruta:
        print(f"{buscar} si esta en la lista")
    else:
        print(f"{buscar} no esta en la lista")


elif(opcion == 21):
        #crear una lista de nuemros
        numeros = [ 7, 6, 8, 4, 2, 6]
        #calcular el promedio
        promedio = sum(numeros) / len(numeros)
        #mostar el resultado
        print(f"el promedionde los numeros es {promedio}")


elif(opcion == 22): 
    #crear una lista de numeoro
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #crear una lista vacia para los pares
    pares=[]
    for n in numeros:
    #recorrer y agregar los pares
     if n % 2 == 0:
    #mostar los resultados
       pares.append (n)
    print(f"numeros pares : {pares}")


elif(opcion == 23):
    #Lista con elementos repetidos.
    numeros = [2, 4, 2, 6, 8, 4, 10, 8]

    #Convertir a conjunto para eliminar duplicados y volver a lista.
    sin_duplicados = list(set(numeros))

    #Mostrar la lista sin duplicados.
    print(f"Lista sin duplicados: {sin_duplicados}")


