
# numeros = [1, 2, 3, 4, 5]
# for n in numeros:
#     if n == 3:
#         print("Saltando el número 3")
#         continue # Pasa a la siguiente iteración
#     print(n)


coders = []
print(coders)

amaount = int(input("cuantos users va a agregar: "))

while amaount != 0 :

    name = input("ingresa tu nombre:¨")
    lastname = input("ingresa tu apellido: ")
    age = input("ingresa tu edad: ")
    email = input("ingresa tu email: ")

    coder = {
        "nombre": name,
        "apellido": lastname,
        "edad": age,
        "email": email,}

    coders.append(coder)
    amaount -= 1

    print(coders)


