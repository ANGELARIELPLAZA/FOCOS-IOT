# Importa las clases y funciones necesarias de Flask, así como otros módulos
from flask import Flask, render_template, url_for, request, redirect, make_response
import random
import json
from time import time

# Inicializa una instancia de Flask
app = Flask(__name__)

# Define la ruta principal ('/') y permite tanto GET como POST
@app.route('/', methods=["GET", "POST"])
def main():
    # Renderiza la plantilla 'index.html' cuando se accede a la ruta principal
    return render_template('index.html')

# Define la ruta '/data' que también acepta GET y POST
@app.route('/data', methods=["GET", "POST"])
def data():
    # Genera datos aleatorios para la temperatura y la humedad
    Temperature = random.random() * 100  # Genera un valor de temperatura entre 0 y 100
    Humidity = random.random() * 55      # Genera un valor de humedad entre 0 y 55

    # Crea una lista con el tiempo actual (en milisegundos), la temperatura y la humedad
    data = [time() * 1000, Temperature, Humidity]

    # Convierte la lista de datos en un JSON y crea una respuesta HTTP con ese contenido
    response = make_response(json.dumps(data))

    # Especifica que el tipo de contenido de la respuesta es JSON
    response.content_type = 'application/json'

    # Devuelve la respuesta al cliente
    return response

# Ejecuta la aplicación Flask si este archivo se ejecuta como el programa principal
if __name__ == "__main__":
    # Configura la aplicación para que se ejecute en el host '0.0.0.0' en el puerto 5000 con modo debug activado
    app.run(host='0.0.0.0', port=5000, debug=True)

