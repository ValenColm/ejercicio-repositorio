
tabla = []
with open("multiplicacion.txt", "w") as f:
    try:
        num = int(input("ingresa un numero del 1 al 10 " ))
    except ValueError:
        print("solo numeros")
    for i in range (1 , 11):
        f.write(f"{num} x {i} = {num * i } \n")


                
        
        
    

    
