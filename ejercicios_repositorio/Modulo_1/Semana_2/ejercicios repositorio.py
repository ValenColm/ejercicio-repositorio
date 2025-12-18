

#  1. ejercicio diccionario 

persona = {
    "nombre": "valentina",
    "edad": "19",
    "ciudad": "bello",
}
print(persona["ciudad"])


# 2. ejercicio diccionario

libro = {
    "titulo" : "el retrato de dorian gray",
    "autor" : "oscar wilde",
    "año" : "1890",
}

campos = ["titulo", "autor", "año"]     
print(campos)

for valor in libro.values ():
    print(valor)
    

#3. ejercicios

coche ={
    "marca": "audi",
    "modelo": "Q5",
    "año": "2008",
}

for clave, valor in coche.items():
    print(f"clave: {clave}, valor; {valor}")



#4. ejercicio

config = {
    "tema": "claro",
    "idioma": "español",
    "tamaño_fuente": "15",
}

print(config.get("tema"))


#5. ejercicio final

curso_python ={
    "nombre_curso" : "thompson",
    "duracion_curso ": "10_meses",
    "estudiantes" : "3",
    "activo" : "True",
    "nivel del curso": "principiante",
}

print(list(curso_python.keys()))
print(list(curso_python.values()))

for clave, valor in curso_python.items():
    print(f"{clave}: {valor}")
    
nivel = curso_python.get("nivel", "principiante")
print("nivel del curso:",nivel)



# EJERCICIO DE LISTAS
frutas= ["mango", "piña", "cereza", "mora", "maracuya"]
print(frutas[3])



frutas.append("fresa")
frutas.append("pera")
print(frutas)


frutas.sort()
print(frutas)



numeros =[3, 1, 2]
numeros.insert(1, 99)
numeros.remove(1)
numeros.append(7)
numeros.sort(reverse=True)
print(numeros)



mi_lista = [10, "hola", (1, 2, "e",4)]
print(mi_lista[2][2])



#EJERCICIOS DE TUPLAS"

colores = ("rojo","verde", "amarillo")
print(colores[1])


try:
    colores[0]="amarillo"
except TypeError as e:
    print("error:", e)
    
    
t = (1, 2, 3)
lista = list(t)
lista.append(4)
t = tuple(lista)
print(t)


mi_tupla = ("a", "b", [1, 2, 3])
mi_tupla[2].append(4)
print(mi_tupla)


numeros = (4, 2, 7, 2, 9, 2)
print(numeros.count(2))
print(numeros.index(7))





#impuestos

def impuesto(precio, iva=19):
    "Devuelve el precio final con IVA incluido."
    return precio * (1 + iva / 100)

# Ejemplo:
print(impuesto(100))       
print(impuesto(200, 10))   


#PROMEDIO SEGURO

def promedio(numeros):
    """Devuelve el promedio de una lista o 0 si está vacía."""
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Ejemplo:
print(promedio([4, 6, 8]))  
print(promedio([]))



#CONTAR VOCALES

def contar_vocales(texto):
    "Cuenta el número de vocales en un texto."
    texto = texto.lower()
    contador = 0
    for letra in texto:
        if letra in "aeiou":
            contador += 1
    return contador

# Ejemplo:
print(contar_vocales("Hola Mundo"))  


#PALIMDROMO

import unicodedata

def limpiar_tildes(cadena):
    """Elimina tildes de una cadena."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )

def es_palindromo(texto):
    """Verifica si el texto es palíndromo (sin importar espacios ni tildes)."""
    texto = limpiar_tildes(texto.lower().replace(" ", ""))
    return texto == texto[::-1]

# Ejemplo:
print(es_palindromo("Anita lava la tina"))   # True
print(es_palindromo("Hola"))                 # False


#PASSWORD FUERTE

def es_fuerte(password):
    """Verifica si la contraseña es fuerte."""
    if len(password) < 8:
        return False
    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_num = any(c.isdigit() for c in password)
    return tiene_mayus and tiene_minus and tiene_num

# Ejemplo:
print(es_fuerte("Hola1234"))  # True
print(es_fuerte("hola"))      # False


#FIBONACCI
def fib(n):
    """Devuelve los primeros n números de Fibonacci."""
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

# Ejemplo:
print(fib(6))  # [0, 1, 1, 2, 3, 5]



#BUSCAR MAXIMO

def top2(nums):
    """Devuelve los dos valores máximos distintos."""
    nums = list(set(nums))  # elimina duplicados
    nums.sort(reverse=True)
    if len(nums) < 2:
        return nums[0], None
    return nums[0], nums[1]

# Ejemplo:
print(top2([3, 7, 7, 5, 9, 2]))  # (9, 7)


#TICKET
def total_ticket(*precios, propina=0):
    """Calcula el total del ticket con propina."""
    subtotal = sum(precios)
    total = subtotal * (1 + propina / 100)
    return total

# Ejemplo:
print(total_ticket(100, 50, 25, propina=10))  # 192.5



#FILTRAR POR KWARGS

def filtrar_alumnos(alumnos, **criterios):
    """Filtra alumnos que cumplan con todos los criterios."""
    resultado = []
    for alumno in alumnos:
        if all(alumno.get(k) == v for k, v in criterios.items()):
            resultado.append(alumno)
    return resultado

# Ejemplo:
alumnos = [
    {"nombre": "Ana", "curso": "JS", "activo": True},
    {"nombre": "Luis", "curso": "Python", "activo": True},
    {"nombre": "Mia", "curso": "JS", "activo": False}
]
print(filtrar_alumnos(alumnos, curso="JS", activo=True))
# [{'nombre': 'Ana', 'curso': 'JS', 'activo': True}]


#CLOSURE CONTADOR

def contador(inicio=0):
    """Crea una función contador que incrementa cada vez que se llama."""
    def inc():
        nonlocal inicio
        inicio += 1
        return inicio
    return inc

# Ejemplo:
c = contador(5)
print(c())  
print(c())  
print(c())  


#LAMBDA

personas = [("Ana", 25), ("Luis", 30), ("Mia", 20)]
ordenadas = sorted(personas, key=lambda x: x[1])
print(ordenadas)




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