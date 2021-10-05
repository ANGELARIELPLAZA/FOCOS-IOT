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
   # Pass the template data into the template main.html and 	return it to the user
   return render_template('index.html')


    

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8181, debug=True)
