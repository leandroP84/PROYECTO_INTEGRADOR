import requests as rq # type: ignore
from colorama import Fore , Back , Style # type: ignore
# Api key
api_key = "152ec4968869eb9cc777ecf6d47e4235"

# Variable para el nombre de la ciudad
nombre_ciudad = input(Fore.GREEN + "Ingrese el nombre de la ciudad: " + Fore.CYAN)

# Función para obtener el clima de una ciudad
def get_weather(api_key, nombre_ciudad):
    # URL para llamar a la API (usando el nombre de la ciudad)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={nombre_ciudad}&appid={api_key}&units=metric"
    
    response = rq.get(url).json()
    
    if response.get("cod") != 200:
        return {"error": f"No se encontró información para {nombre_ciudad}"}
    
    temperatura = response['main']['temp']  # Temperatura en grados Celsius
    nombre = response['name']  # Nombre de la ciudad
    
    return {
        'temperatura': temperatura,
        'nombre': nombre
    }

# Obtener datos del clima
Datos = get_weather(api_key, nombre_ciudad)

if "error" in Datos:
    print(Fore.RED + Datos["error"])
else:
    nombre = Datos['nombre']
    temperatura = Datos['temperatura']

    print(Fore.BLUE + "App Clima!")
    print("Ciudad seleccionada:", Fore.WHITE + nombre)
    print(Fore.GREEN + "Temperatura:", Fore.LIGHTYELLOW_EX, f"{temperatura}°C", Fore.WHITE)


