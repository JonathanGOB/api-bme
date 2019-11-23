import paho.mqtt.client as mqtt
import json
import pyodbc


buffer = {}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("IoTCore/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #put in database
    print(msg.topic + " " + msg.payload.decode('utf-8'))
    topic = str(msg.topic.split("/"))
    message = json.load(str(msg.payload.decode('utf-8')))
    key = message.keys()[0]
    buffer[key] = message[key]
    buffer ["device"] = topic[1]
    if len(buffer) == 4 and key == "humidity":
        insert = ""
        values = ""
        for x in buffer:
            insert += x + ","
            values += buffer[x] + ","

        insert = insert[:-1]
        values = values[:-1]

        statement = "INSERT INTO "  + insert + "VALUES " + values
        print("statement: " + statement)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

