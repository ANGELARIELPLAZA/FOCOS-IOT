
import paho.mqtt.client as mqtt
from flask import Flask, render_template, request

app = Flask(__name__)

client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.connect("localhost", 1883, 60)

@app.route('/')
def hello_world():
    client.subscribe("outTopic")  # Subscribe to the topic “digitest/test1”, receive any messages published on it
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    print("")  # Print a received msg
    client.loop_forever()  # Start networking daemon
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
