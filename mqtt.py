import paho.mqtt.client as mqtt
import time
import pytz

from datetime import datetime

tz_gh = pytz.timezone('Africa/Accra') 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False  

client = mqtt.Client()
client.on_connect = on_connect
client.connect("197.255.72.187", 1883, 60)
client.loop_start()  

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        today = datetime.utcnow()

        now = today.strftime("%d/%m/%Y %H:%M:%S")

        message = f'Motion Detected at your door'
        client.publish("motion", f"{now} : {message}")
        # print("message sent")
        print(today)
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
