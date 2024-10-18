import requests as rq # type: ignore
from colorama import Fore , Back , Style # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()
# Api key
# api_key = "152ec4968869eb9cc777ecf6d47e4235"
api_key=os.getenv("API_KEY")
print(api_key)
# Variable para el nombre de la ciudad

seleccion = 0

#comienzo del menú
print ("\nBienvenido a la App del Clima TirameElBit.")

#bucle de selección
while seleccion != 5 :
    print ("Por favor ingrese un número para acceder a las funciones.\n")
    print (Fore.LIGHTBLUE_EX +"1. Consultar el clima Actual de una ciudad \n2. Consultar el pronóstico del clima \n3. Ver Historial de Consultas \n4. Cambiar las unidades de temperatura \n5. Salir del programa. \n")
    seleccion = int(input("Su selección: "))

    #validación
    if (seleccion < 1)  or (seleccion >5):
        seleccion = int(input("Por favor ingrese un número válido: "))

    #salidas a funciones
    if seleccion == 1:
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
                    print(Fore.GREEN + "La temperatura actual es de: " + "Temperatura:", Fore.LIGHTYELLOW_EX, f"{temperatura}°C", Fore.WHITE)
                    #variables
                pass
    if  seleccion == 2:
        pass
    if seleccion == 3:
        pass
    if  seleccion == 4:
        pass
    
    #salida del programa
    if seleccion == 5:
        print ("Adiós.")
        break


