import json
from datetime import datetime, timedelta

# Abrir el archivo JSON
with open('myfile.json', 'r') as f:
    # Cargar el contenido del archivo JSON en una variable
    ourjson = json.load(f)

# Acceder a los datos del archivo JSON
nombre = ourjson['nombre']
apellido = ourjson['apellido']
codigo_seccion = ourjson['codigo_seccion']
sede = ourjson['sede']

# Imprimir los datos del archivo JSON
print("Nombre: ", nombre)
print("Apellido: ", apellido)
print("Código de Sección: ", codigo_seccion)
print("Sede: ", sede)

# Extraer el valor del token y la fecha de vencimiento
token = ourjson['token']
expiration_date = datetime.strptime(ourjson['expiration_date'], '%Y-%m-%d')

# Obtener la fecha y hora actual
now = datetime.now()

# Calcular el tiempo restante hasta la fecha de vencimiento
time_remaining = expiration_date - now

# Imprimir el valor del token y el tiempo restante
print("Token: ", token)
print("Tiempo restante antes de que caduque: ", time_remaining)




