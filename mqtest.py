import paho.mqtt.client as mqtt
import time
import pytz
import random

from datetime import datetime

tz_gh = pytz.timezone('Africa/Accra') 


broker = 'rff11281.ala.us-east-1.emqxsl.com'
port = 8883
topic = 'motion'
client_id = f'jujutsu-server'
username = 'jujutsu'
password = 'jujutsu'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  
        Connected = True

    else:
        print("Connection failed")

Connected = False  

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.tls_set(ca_certs='./emqxsl-ca.crt')
client.on_connect = on_connect
client.connect(broker, port, 60)
client.loop_start()  

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        today = datetime.utcnow()

        now = today.strftime("%d/%m/%Y %H:%M:%S")
        message = f'Motion Detected at your door'
        client.publish(topic, f"{now} : {message}")
        # print("message sent")
        print(message)
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
