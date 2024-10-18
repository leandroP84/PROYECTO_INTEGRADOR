import requests as rq
from colorama import Fore , Back , Style

# Api key 
api_key = "152ec4968869eb9cc777ecf6d47e4235"

# Esta Variable deberian usarla para guardar el nombre de la variable en los inputs.
nombre_ciudad = ""


#Esta funcion lo que hace es getear una ciudad y tambien el reporte de tiempo
def get_wheater(api_key , lat , lon): # Recibe la api_key y la Latitud y Longitud 
    
    #Como recibe la LAT y LON estaba pensando en presetear algunos Países si encuentran una mejor solucion me avisan
    # Argentina_mendoza = -32.89084 , -68.82717
    
    
    # Esta es la url para llamar a la Api.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
    response = rq.get(url).json()
    
    temperatura = response['main'] # Lista con datos climatologicos
    nombre = response['name'] # Nombre de la Región

    #Esto retorna un diccionario , que se accede con el nombre de la variable y corchetes
    return {
        
        'temperatura' : temperatura,
        'nombre':nombre
    }
    
    
#Datos tiene el diccionario que se retorna en la linea 26-30
Datos = get_wheater(api_key, "-32.89084" , "-68.82717")    

nombre = Datos['nombre']


print(Fore.BLUE + "App Clima! ")
print(  "País seleccionado: " , Fore.WHITE + nombre)
print( Fore.GREEN + "Datos: " ,Fore.LIGHTYELLOW_EX, Datos['temperatura'],Fore.WHITE)



# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

