import paho.mqtt.client as mqtt
import json
import threading
import urllib.request
import time
import datetime

schema = {
    "device_id": None,
    "humidity": None,
    "pressure": None,
    "temperature": None,
    "timestamp": None,
}

timestamps = []
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
    timestamps.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def computing():
    #print(schema)
    #Format the data to put in the schema
    if messages:
        print(schema)
        msg = messages.pop()
        timestamp = timestamps.pop()
        topic = msg.topic.split("/")
        schema["device_id"] = topic[1]
        schema["timestamp"] = timestamp
        message = msg.payload.decode('utf-8')
        message = json.loads(message)
        keys = message.keys()
        key = list(keys)[0]
        schema[key] = message[key]

        #Sends data if complete and resets the schema if not. Removes the start incompletion data
        if key == "humidity" and all(v is not None for v in schema.values()):
            #print("POST to api")
            request = urllib.request.Request("http://127.0.0.1:5000/Api/V1/CapturedData")
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            data = json.dumps(schema)
            dataBytes = data.encode('utf-8')
            request.add_header('Content-length', len(dataBytes))
            try:
                response = urllib.request.urlopen(request, dataBytes)

            except Exception as e:
                print(e)
            print(schema)
            resetSchema(schema)

        elif key == "humidity" and any(v is not None for v in schema.values()):
            resetSchema(schema)

#add components if needed for the thread
def computingFunctionThread():
    print("starting thread")
    while True:
        computing()



#resets the schema
def resetSchema(schema):
    for (key, value) in schema.items():
        schema[key] = None

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
def main():
    threadmqtt = threading.Thread(target=client.loop_forever)
    threadcomputing = threading.Thread(target=computingFunctionThread)
    threadmqtt.start()
    threadcomputing.start()

if __name__ == '__main__':
    main()

