#solicita datos para identificar al usuario
nombre = input("ingresa tu nombre: ")
print(f"hola, {nombre} bienvenido a la calculadora de años: ")
#solicita datos para la operacion propuesta.
año_nacimiento = int (input("ingresa tu año de nacimiento: "))
año_actual = int (input("ingresa el año actual: "))
#Calculo de la edad del usuario
edad = año_actual - año_nacimiento
#Envia los resultados al usuario
print (f"hola { nombre} tu edad es {edad} años")





