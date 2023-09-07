from flask import Flask, request, render_template, redirect, session, jsonify
from flask_mqtt import Mqtt

from readwrite import readfile, writefile

notifications = False
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['MQTT_BROKER_URL'] = '192.168.11.2'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 5
# app.config['MQTT_USERNAME'] = 'jujutsu'
# app.config['MQTT_PASSWORD'] = 'jujutsu'
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_TLS_CA_CERTS'] = './emqxsl-ca.crt'
app.config['MQTT_LOG_LEVEL'] = 'logging.DEBUG' 


Session(app)
mqtt_client = Mqtt(app)

keys = {"josh": "josh123"}


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected')
        mqtt_client.subscribe("motion")
    else:
        print("Couldn't connect. Error Code:", rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(topic=message.topic, payload=message.payload.decode('utf-8'))

    writefile(data)
    print(f'Message received on topic {data["topic"]}: with payload: {data["payload"]}')


@app.post("/message")
def publish():
    request_data = request.get_json()
    result = mqtt_client.publish(topic=request_data['topic'], payload=request_data["msg"])

    return jsonify({'code': result[0]})


@app.route("/login", methods=["GET", "POST"])
def login():

    """
    Handles user authentication 

    """
    if request.method == "POST":
        if keys.get(request.form["username"]) == None:
            return render_template("login.html",message="User does not exist")
        elif keys.get(request.form["username"]) != request.form['password']:
            return render_template('login.html', message="Invalid Password")
        else:
            session['name'] = request.form['username']
            return redirect("/")
        
    return render_template('login.html')


@app.route("/logout")
def logout():

    """
    Logs the user out and clears session data

    """

    session["name"] = None

    return redirect("/login")


@app.route("/", methods=['GET', 'POST'])
def home():
    """ Returns the user homepage"""

    if not session.get("name"):
        redirect("/login")
        
    logs = readfile()
    return render_template("home1.html", logs=logs)


@app.route("/activity/", methods=["GET"])
def activity():
   
   date = request.args.get("picker")

   activity = readfile(date)

   return(render_template("home2.html", activity=activity))
