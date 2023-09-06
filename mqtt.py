import paho.mqtt.client as mqtt
import time
import pytz
from gpiozero import MotionSensor, LED
import requests
from datetime import datetime

tz_gh = pytz.timezone('Africa/Accra') 

pir = MotionSensor(27)
webhook_url = "https://maker.ifttt.com/trigger/Motion/json/with/key/oYNmTH4HE1AQDZ1shbuIyOVkM34RqaecmllxGXZhYVa"
yellow_led = LED(4)


while Connected != True:
    time.sleep(0.1)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

def send_message():
    today = datetime.utcnow()

    now = today.strftime("%d/%m/%Y %H:%M:%S")

    message = f'Motion Detected'
    client.publish("motion", f"{message}")
    # print("message sent")


def motion_function():
    yellow_led.on()
    print("Motion Detected At Your Front-Door")

    response = requests.post(webhook_url)
    send_message()
    if response.status_code == 200:
        print("Webhook trigger sent successfully")
    else:
        print("Webhook trigger failed", response.status_code)
    

def no_motion_function():
    yellow_led.off()
    print("Motion Stopped")


Connected = False  

client = mqtt.Client()
client.on_connect = on_connect
client.connect("197.255.72.183", 1883, 60)
client.loop_start()  

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function





# try:
#         today = datetime.utcnow()

#         now = today.strftime("%d/%m/%Y %H:%M:%S")

#         message = f'Motion Detected at your door'
#         client.publish("motion", f"{now} : {message}")
#         # print("message sent")
#         print(today)
#         time.sleep(1)

# except KeyboardInterrupt:
#     client.disconnect()
#     client.loop_stop()
