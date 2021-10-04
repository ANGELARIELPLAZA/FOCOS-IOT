import paho.mqtt.client as mqtt
import time

# Create client instance and connect to localhost
mqtt = mqtt.Client()
mqtt.connect("localhost", 1883, 60)

# Publish message to topic/iopi and set pin 1 on bus 1 to on
mqtt.publish("mesa1", 0)
time.sleep(2)




   