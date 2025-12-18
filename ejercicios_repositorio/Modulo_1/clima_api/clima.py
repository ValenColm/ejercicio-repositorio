import requests


api_key = "8cdab3b3230f711f68b9dd71f6200e5a"

print("=== CONSULTA DEL CLIMA ===")
print('si deseas cerrar el programa , escribe: "salir"')

while True:
    ciudad = input("ingresa la ciudad que deseas ver el clima: ").strip()
    
    
    if not ciudad:
        print("Error: no puedes dejar este campo vacio")
        continue
    
    if ciudad.lower() == "salir":
        print("saliendo del programa")
        break
    
    if ciudad.replace(" ", "").isnumeric():
        print("Error: no puedes ingresar numeros.")
        continue
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print("Error al conectar con el servidor. verifica tu internet") 
        continue
    
    if response.status_code == 404:
        print(f"Error: '{ciudad}' no fue encontada. revisa la ortografia.")
        continue
    
    if response.status_code != 200:
        print(f"Error inesperado: {response.status_code}")
        continue
    
    temperatura = data['main']['temp']
    descripcion = data['weather'][0]['description']
    humedad = data['main']['humidity']
    
    print(f"clima en {ciudad}: {descripcion} ")
    print(f"temperatura : { temperatura} °C")
    print(f"humedad: {humedad}%")
    
else:
    print("error al obtener los datos ", response.status_code)
