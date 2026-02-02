# list=[3, 7, 2, 9, 5]
# mayor=list[0]
# for i in list:
#     if i > mayor:
#         mayor=i
# print(mayor)





#texto=input("ingresa una palabra :")

#textos= texto.lower().strip()

#if textos ==textos[::-1]:
#    print("true")
#else:
#   print("false")    
    

    
        
        
#for i in range(1, 101):
#   if i % 3 == 0 and i % 5 == 0:
#        print("fizz buzz")
#   elif i % 3 == 0:
#        print("fizz")
#   elif i % 5 == 0:
#       print("buzz")
#   else:
#       print(i)
    
    
#ordena una lista con bubble sord
def burbuja(lista):
    # Recorre la lista desde el índice 0 hasta el penúltimo índice
    for i in range(0, len(lista)-1):
        # Para cada i, recorre los pares adyacentes desde 0 hasta len(lista)-i-2
        # (porque los últimos i elementos ya están en su lugar tras i iteraciones)
        for j in range(0, len(lista)-i-1):
            # Si el elemento actual es mayor que el siguiente, los intercambia
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
lista=[8, 3, 10, 25, 5, 7, 9, 45, 76, 89, 1, 4]
print('lista enviada:', lista)
burbuja(lista)
print('lista ordenada:' ,lista)

