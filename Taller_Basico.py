nombre = input("ingresa tu nombre: ")
print()
print("="*90)
print(f"Bienvenido al Sistema, {nombre} ingresa un numero entre 1 a 30 para iniciar el programa deseado: ")
print("="*90)
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