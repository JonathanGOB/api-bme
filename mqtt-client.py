import paho.mqtt.client as mqtt
import json
import threading
import urllib.request

schema = {
    "device_id": None,
    "humidity": None,
    "pressure": None,
    "temperature": None,
    "timestamp": None,
}

messages = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("IoTCore/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #appends the data to the messages
    messages.append(msg)

def computing():
    print(schema)
    #Format the data to put in the schema
    msg = messages.pop()
    topic = msg.topic.split("/")
    schema["device_id"] = topic[1]
    message = json.load(str(msg.payload.decode('utf-8')))
    key = message.keys()[0]
    schema[key] = message[key]

    #Sends data if complete and resets the schema if not. Removes the start incompletion data
    if message[key] == "humidity" and not all(schema.values()):
        print("POST to api")
        request = urllib.request.Request("http://127.0.0.1:5000/Api/V1/CapturedData")
        request.add_header('Content-Type', 'x-www-form-urlencoded; charset=utf-8')
        data = json.dumps(schema)
        dataBytes = data.encode('utf-8')
        request.add_header('Content-length', len(dataBytes))
        response = urllib.request.urlopen(request, dataBytes)
        print(response)
        resetSchema()

    elif messages[key] == "humidity" and all(schema.values()):
        resetSchema()

#resets the schema
def resetSchema():
    schema = {
        "device_id": None,
        "humidity": None,
        "pressure": None,
        "temperature": None,
        "timestamp": None,
    }

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
def main():
    threadmqtt = threading.Thread(target=client.loop_forever())
    threadmqtt.start()


if __name__ == '__main__':
    main()

