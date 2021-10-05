"""
Python MQTT Subscription client - No Username/Password
Thomas Varnish (https://github.com/tvarnish), (https://www.instructables.com/member/Tango172)
Written for my Instructable - "How to use MQTT with the Raspberry Pi and ESP8266"
"""
import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

mqtt = mqtt.Client()
mqtt.connect("localhost", 1883, 60)
mqtt.loop_start()
topic1 = "mesa1"  # Mesa 1



@app.route("/", methods=["GET", "POST"])
def main():
   datos = request.form.to_dict(flat=True)
   print(datos)
   #########################################
   valores1 = datos.get("mesa1")
   # Convierte  en string y busca el elemento dentro del diccionario
   # print(valores1)
   # Convierte  en string y busca el elemento dentro del diccionario

#########################################
   # MESA 1
   if valores1 == 'ON':
       dato = 1
       if dato == 1:
           color = datos.get("color")
           print(color)
           if color == '#ff0000':  # color rojo
                mqtt.publish(topic1, 1)
           

   if valores1 == 'OFF':
        mqtt.publish(topic1, 0)

   # Pass the template data into the template main.html and     return it to the user
   return render_template('index.html')

mqtt.subscribe("outTopic")


    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8181, debug=True)
