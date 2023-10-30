import paho.mqtt.client as mqtt
from django.conf import settings
from myapp.models import Data

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('django/mqtt')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    data = msg.payload.decode('utf-8')
    if Data[0] == "t":
        data_instance = Data(temperature=data[1:])
    elif Data[0] == "h":
        data_instance = Data(thumidity=data[1:])
    data_instance.save()    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
mqtt.client.loop_start()

