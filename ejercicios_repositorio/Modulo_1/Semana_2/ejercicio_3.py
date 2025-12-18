#impuestos

def impuesto(precio, iva=19):
     """Devuelve el precio final con IVA incluido."""
     return precio * (1 + iva / 100)

 # Ejemplo:
print(impuesto(100))       
print(impuesto(200, 10))   


#PROMEDIO SEGURO

def promedio(numeros):
     "Devuelve el promedio de una lista o 0 si está vacía."
     if len(numeros) == 0:
         return 0
     return sum(numeros) / len(numeros)

# Ejemplo:
print(promedio([4, 6, 8]))  
print(promedio([]))



#CONTAR VOCALES

def contar_vocales(texto):
    """Cuenta el número de vocales en un texto."""
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




