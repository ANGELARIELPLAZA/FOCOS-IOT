import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

mqtt = mqtt.Client()
mqtt.connect("localhost", 1883, 60)
mqtt.loop_start()
topic1 = "mesa1"  # Mesa 1
topic2 = "mesa2"  # Mesa 2
topic3 = "mesa3"  # Mesa 3
topic4 = "mesa4"  # Mesa 4
topic5 = "tubo"   # tubo led


@app.route("/", methods=["GET", "POST"])
def main():
   datos = request.form.to_dict(flat=True)
   print(datos)
   #########################################
   valores1 = datos.get("mesa1")
   # Convierte  en string y busca el elemento dentro del diccionario
   # print(valores1)
   # Convierte  en string y busca el elemento dentro del diccionario
   valores2 = datos.get("mesa2")
   # print(valores2)
   # Convierte  en string y busca el elemento dentro del diccionario
   valores3 = datos.get("mesa3")
   # print(valores3)
   # Convierte  en string y busca el elemento dentro del diccionario
   valores4 = datos.get("mesa4")
   # print(valores4)
   # Convierte  en string y busca el elemento dentro del diccionario
   valores5 = datos.get("tubo")
   # print(valores4)
#########################################
   # MESA 1
   if valores1 == 'ON':
       dato = 1
       if dato == 1:
           color = datos.get("color")
           print(color)
           if color == '#ff0000':  # color rojo
                mqtt.publish(topic1, 1)
           if color == '#008f39':  # color Green
                mqtt.publish(topic1, 2)
           if color == '#0000ff':  # color Blue
                mqtt.publish(topic1, 3)
           if color == '#ff00ff':  # color magenta
                mqtt.publish(topic1, 4)
           if color == '#ffaa00':  # color amarrillo
                mqtt.publish(topic1, 5)
           if color == '#ffffff':  # color blanco
                mqtt.publish(topic1, 6)

   if valores1 == 'OFF':
        mqtt.publish(topic1, 0)
#########################################
    # MESA 2
   if valores2 == 'ON':
        dato = 1
        if dato == 1:
            color = datos.get("color")
            print(color)
            if color == '#ff0000':  # color rojo
                mqtt.publish(topic2, 1)
            if color == '#008f39':  # color Green
                mqtt.publish(topic2, 2)
            if color == '#0000ff':  # color Blue
                mqtt.publish(topic2, 3)
            if color == '#ff00ff':  # color magenta
                mqtt.publish(topic2, 4)
            if color == '#ffaa00':  # color amarrillo
                mqtt.publish(topic2, 5)
            if color == '#ffffff':  # color blanco
                mqtt.publish(topic2, 6)

   if valores2 == 'OFF':
        mqtt.publish(topic2, 0)
#########################################
    # MESA 3
   if valores3 == 'ON':
        dato = 1
        if dato == 1:
            color = datos.get("color")
            print(color)
            if color == '#ff0000':  # color rojo
                mqtt.publish(topic3, 1)
            if color == '#008f39':  # color Green
                mqtt.publish(topic3, 2)
            if color == '#0000ff':  # color Blue
                mqtt.publish(topic3, 3)
            if color == '#ff00ff':  # color magenta
                mqtt.publish(topic3, 4)
            if color == '#ffaa00':  # color amarrillo
                mqtt.publish(topic3, 5)
            if color == '#ffffff':  # color blanco
                mqtt.publish(topic3, 6)
            
   if valores3 == 'OFF':
        mqtt.publish(topic3, 0)

#########################################
    # MESA 4
   if valores4 == 'ON':
        dato = 1
        if dato == 1:
            color = datos.get("color")
            print(color)
            if color == '#ff0000':  # color rojo
                mqtt.publish(topic4, 1)
            if color == '#008f39':  # color Green
                mqtt.publish(topic4, 2)
            if color == '#0000ff':  # color Blue
                mqtt.publish(topic4, 3)
            if color == '#ff00ff':  # color magenta
                mqtt.publish(topic4, 4)
            if color == '#ffaa00':  # color amarrillo
                mqtt.publish(topic4, 5)
            if color == '#ffffff':  # color blanco
                mqtt.publish(topic4, 6)

   if valores4 == 'OFF':
        mqtt.publish(topic4, 0)
#########################################
    # TUBO
   if valores5 == 'ON':
        dato = 1
        if dato == 1:
            color = datos.get("color")
            print(color)
            if color == '#ff0000':  # color rojo
                mqtt.publish(topic5, 1)
            if color == '#008f39':  # color Green
                mqtt.publish(topic5, 2)
            if color == '#0000ff':  # color Blue
                mqtt.publish(topic5, 3)
            if color == '#ff00ff':  # color magenta
                mqtt.publish(topic5, 4)
            if color == '#ffaa00':  # color amarrillo
                mqtt.publish(topic5, 5)
            if color == '#ffffff':  # color blanco
                mqtt.publish(topic5, 6)

   if valores5 == 'OFF':
        mqtt.publish(topic5, 0)
#########################################
   # Pass the template data into the template main.html and 	return it to the user
   return render_template('index.html')

client.subscribe("ESP8266Client")


    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8181, debug=True)
