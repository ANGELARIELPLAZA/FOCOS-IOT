import os
from flask import Flask, render_template, redirect, flash, request, url_for
from datetime import timedelta, datetime
from time import time
from flask_mqtt import Mqtt
 

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = "localhost"
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] =20

mqtt = Mqtt(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('on_connect client : {} userdata :{} flags :{} rc:{}'.format(client, userdata, flags, rc))
    mqtt.subscribe("outTopic")

#@mqtt.on_subscribe()
#def handle_subscribe(client, userdata, mid, granted_qos):
#    print('on_subscribe client : {} userdata :{} mid :{} granted_qos:{}'.format(client, userdata, mid, granted_qos))


@mqtt.on_message()
def handle_message(client, userdata, message):
    print('on_message client : {} userdata :{} message.topic :{} message.payload :{}'.format(
        client, userdata, message.topic, message.payload.decode()))

@mqtt.on_disconnect()
def handle_disconnect(client, userdata, rc):
    print('on_disconnect client : {} userdata :{} rc :{}'.format(client, userdata, rc))
    

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)