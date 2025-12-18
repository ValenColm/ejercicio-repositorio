#ejercicio 1
while True:
    try:
        temperatura = float(input("introduce la temperatura : "))
        print(" elige un opcion ")
        print("1 - convertir a grado celsius")
        print("2 - convertir a grados  farenheit")
        opcion=input("elige una opcion")
        
        if opcion == 1:
            resultado = (temperatura - 32) * 5/9 
            print(f"{temperatura} °f eauivalente a {resultado: .2f}")
        elif opcion == 2:
            resultado = (temperatura * 9/5) + 32
            print(f"{temperatura} °c equivalente a {resultado: .2f}")
        else:
            raise ValueError("opcion invalida")
        break
    except ValueError:
        print("Error: ingresa valores numericos y una opcion valida : ")
        
        
#ejercicio 2
while True:
    try:
        num1 = float(input("ingresa el primer numero"))
        num2 = float(input("ingresa el segundo numero"))
        resultado = num1 / num2
        print(f"resultado: {resultado}")
        break
        
    except ValueError:
        print("Error: debes ingresar solo numeros")
        
    except ZeroDivisionError:
        print("no puedes dividir por cero")
        
    except Exception as e :
        print("ERROR INESPERADO")    
    
        
        
        
#EJERCICIO 3

import random
import math

num = random.randint(1, 100)
print("numero generado:", num)

print("Raiz cuadrado:" , math.sqrt(num))
print("al cuadrado:", math.pow(num, 2))
print("redondeo hacia arriba:", math.ceil(num))
print("redondeo hacia abajo:", math.floor(num))


#ejercicio 4

from datetime import datetime, date
hoy = date.today()
print("fecha actual:", hoy)

nac =input("ingresa tu fecha de nacimiento (AAAA-MM-DD): ")

try:
    fecha_nac = datetime.strptime(nac, "%Y-%M-%D").date()
    
    edad = hoy.year - fecha_nac.year
    dias = (hoy - fecha_nac).days
    
    print("edad:", edad)
    print("dias vividos:", dias)
    
except ValueError:
    print("formato incorrecto.")
    
    
    
#ejercicio 5



def contar_vocales (texto):
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in texto:
        if letra in conteo :
            conteo [letra] +=1
            
    return conteo

def invertir(texto):
    return texto[::-1]


def contar_palabras(texto):
    return len(texto.split())


def es_palindromo(texto):
    t = texto.replace(" ", "").lower()
    return t == t[::-1]




texto = input("Ingresa un texto: ")

print(contar_vocales(texto))
print(invertir(texto))
print(contar_palabras(texto))
print("¿Es palíndromo?:", es_palindromo(texto))



#ejercicio 6

def sumar (a, b): return a + b
def restar(a, b): return a - b
def multiplicar( a, b): return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")
    return a / b

def mostrar_menu():
    print("\n1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    opcion = input("elige una opcion")
    
    while True:
        mostrar_menu()
        if opcion == "5": break

    a = float(input("A: "))
    b = float(input("B: "))

    try:
        if opcion == "1": print(sumar(a, b))
        elif opcion == "2": print(restar(a, b))
        elif opcion == "3": print(multiplicar(a, b))
        elif opcion == "4": print(dividir(a, b))
        else: print("Opción inválida")
    except Exception as e:
        print("Error:", e)
        
#ejercicio 6

def mostrar_menu():
    print("\n--- Gestor de Notas ---")
    print("1) Agregar nota")
    print("2) Ver notas")
    print("3) Buscar nota")
    print("4) Eliminar nota")
    print("5) Salir")


def agregar_nota():
    nota = input("Escribe la nota: ")
    with open("notas.txt", "a") as f:
        f.write(nota + "\n")


def ver_notas():
    with open("notas.txt", "r") as f:
        print("\n--- Todas las notas ---")
        print(f.read())


def buscar_nota():
    palabra = input("palabra a buscar: ")
    with open("notas.txt", "r") as f:
        for linea in f:
            if palabra.lower() in linea.lower():
                print("Encontrada:", linea)


def eliminar_nota():
    borrar = input("Texto exacto a eliminar: ")

    with open("notas.txt", "r") as f:
        lineas = f.readlines()

    with open("notas.txt", "w") as f:
        for linea in lineas:
            if linea.strip() != borrar:
                f.write(linea)


while True:
    mostrar_menu()
    op = input("Elige: ")

    if op == "1": agregar_nota()
    elif op == "2": ver_notas()
    elif op == "3": buscar_nota()
    elif op == "4": eliminar_nota()
    elif op == "5": break
    
    else:
        print("Opción inválida")
        
        
        


    