import requests as rq # type: ignore
from colorama import Fore , Back , Style # type: ignore
import os
from dotenv import load_dotenv
import json  # Librería para trabajar con datos en formato JSON
from datetime import datetime  # Librería para manejar fechas y horas

load_dotenv()
# Api key
api_key=os.getenv("API_KEY")
units = "metric"  # Establecer la unidad de temperatura como Celsius
# Función para obtener el clima de una ciudad
# Función para obtener el clima actual
def get_current_weather(api_key, city, country, units):
    # Formar la URL para la consulta del clima actual con los parámetros de ciudad, país y unidad métrica
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units={units}"
    # Hacer una solicitud GET a la API y convertir la respuesta a JSON
    response = rq.get(url).json()

    # Verificar si la respuesta contiene los datos principales del clima y el nombre de la ciudad
    if 'main' in response and 'name' in response:
        temperatura = response['main']  # Obtener los datos de temperatura
        nombre = response['name']  # Obtener el nombre de la ciudad

        # Devolver un diccionario con los datos necesarios
        return {
            'temperatura': temperatura,
            'nombre': nombre
        }
    else:
        return None  # Si no se encuentra la información, devolver None

# Función para obtener el pronóstico del clima
def get_forecast_weather(api_key, city, country, units):
    # Formar la URL para consultar el pronóstico con los parámetros de ciudad, país y unidad métrica
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&units={units}&appid={api_key}"
    # Hacer una solicitud GET a la API y convertir la respuesta a JSON
    response = rq.get(url).json()

    # Verificar si la respuesta contiene una lista de pronósticos
    if 'list' in response:
        # Devolver los primeros 5 períodos del pronóstico
        return response['list'][:5]
    else:
        return None  # Si no se encuentra el pronóstico, devolver None

# Función para guardar los datos consultados en un historial
def save_to_history(city, country, data):
    history = []  # Inicializar una lista para el historial

    # Verificar si existe un archivo de historial y cargar los datos si está presente
    if os.path.exists('weather_history.json'):
        with open('weather_history.json', 'r') as f:
            history = json.load(f)
    
    # Agregar una nueva entrada al historial con los datos actuales y la marca de tiempo
    history.append({
        'city': city,
        'country': country,
        'data': data,
        'timestamp': datetime.now().isoformat()  # Guardar la fecha y hora actuales
    })
    
    # Guardar el historial actualizado en el archivo JSON
    with open('weather_history.json', 'w') as f:
        json.dump(history, f)

# Función para imprimir los datos del clima actual
def print_clima_actual(datos):
    if datos:
        nombre = datos['nombre']  # Obtener el nombre de la ciudad
        print(Fore.BLUE + "ClimaApp")  # Título de la aplicación con color
        print("Ciudad seleccionada: ", Fore.WHITE + nombre)  # Mostrar el nombre de la ciudad
        print(Fore.GREEN + "Datos actuales: ", Fore.LIGHTYELLOW_EX, datos['temperatura'], Fore.WHITE)  # Mostrar la temperatura actual
    else:
        print(Fore.RED + "No se pudo obtener la información del clima.")  # Mensaje de error si no se obtienen los datos
# Funcion pára imprimir el pronostico
def print_weather(datosforecast):
        
     # Si hay pronóstico, mostrar los próximos períodos
    if datosforecast:
       print(Fore.MAGENTA + "\nPronóstico para los próximos períodos:")
       for forecast in datosforecast:
            # Mostrar la fecha, temperatura y descripción del clima para cada período
            print(f"Fecha: {forecast['dt_txt']}, Temperatura: {forecast['main']['temp']}°, {forecast['weather'][0]['description']}")
    else:
        print(Fore.RED + "No se pudo obtener el pronóstico.")  # Mensaje de error si no hay pronóstico
    
# Función para visualizar el historial de consultas
def view_history():
    # Verificar si existe un archivo de historial y cargarlo
    if os.path.exists('weather_history.json'):
        with open('weather_history.json', 'r') as f:
            history = json.load(f)
        
        print(Fore.CYAN + "\nHistorial de consultas:")  # Título del historial con color
        for entry in history:
            # Mostrar los detalles de cada consulta en el historial
            print(f"Fecha: {entry['timestamp']}")
            print(f"Ciudad: {entry['city']}, País: {entry['country']}")
            print(f"Temperatura: {entry['data']['temperatura']['temp']}°")
            print("-------------------------")
    else:
        print(Fore.RED + "No hay historial disponible.")  # Mensaje de error si no hay historial

# Función principal de la aplicación
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola

        # Mostrar menú de opciones
        print(Fore.YELLOW + "1. Consultar clima actual")
        print("2. Consultar pronostico")
        print("3. Ver historial")
        print("4. Salir")
        choice = input("Elige una opción: ")  # Leer la opción del usuario
        if choice == '1':
            # Pedir al usuario que ingrese la ciudad y el país
            city = input("Escribe la ciudad:\n")
            country = input("Escribe el país:\n")
            
            # Obtener el clima actual
            datos = get_current_weather(api_key, city, country, units)

            print_clima_actual(datos)

            if datos:
                save_to_history(city, country, datos)

            input("\nPresiona Enter para continuar...")
        elif choice == '2':
            # Pedir al usuario que ingrese la ciudad y el país
            city = input("Escribe la ciudad:\n")
            country = input("Escribe el país:\n")
            
            # Obtener el pronóstico para la ciudad y el país ingresados
            datosforecast = get_forecast_weather(api_key, city, country, units)

            # Imprimir los resultados obtenidos
            print_weather(datosforecast)

            # Si se obtuvieron datos, guardarlos en el historial
            if datos:
                save_to_history(city, country, datos)

            input("\nPresiona Enter para continuar...")
        elif choice == '3':
            view_history()  # Mostrar el historial de consultas
            input("\nPresiona Enter para continuar...")
        elif choice == '4':
            break  # Salir del programa

# Ejecutar la función principal cuando se ejecute el script
if __name__ == "__main__":
    main()