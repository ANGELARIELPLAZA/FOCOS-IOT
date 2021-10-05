
import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.connect("localhost", 1883, 60)


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("outTopic")  # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    print("")  # Print a received msg












@app.route('/')
def hello_world():
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    # client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
