import paho.mqtt.client as mqtt
import json
import threading
import urllib.request
import time
import datetime
import AzureSQLDatabase

devices = ["ESP1", "ESP2"]
deviceobjects = []
timestamps = []
messages = []
conn = AzureSQLDatabase.AzureSQLDatabase()


class ESP:
    name = None
    schema = {
        "device_id": None,
        "humidity": None,
        "pressure": None,
        "temperature": None,
        "timestamp": None,
    }

    def __init__(self, name):
        self.name = name

    def add_to_schema(self, rescource, subject):
        self.schema[subject] = rescource

    def reset_schema(self):
        self.schema = {
        "humidity": None,
        "pressure": None,
        "temperature": None,
        "timestamp": None,
    }

    def get_name(self):
        return self.name

    def get_schema(self):
        return self.schema

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for device in devices:
        print("IoTCore/" + device)
        client.subscribe("IoTCore/" + device + "/#")
        deviceobjects.append(ESP(device))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # appends the data to the messages
    messages.append(msg)
    timestamps.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def computing():
    # print(schema)
    # Format the data to put in the schema
    if messages:
        msg = messages.pop()
        topic = msg.topic.split("/")
        device_id = topic[1]
        timestamp = timestamps.pop()
        for device in deviceobjects:
            if device.get_name() == device_id:
                print(device.get_name())
                device.add_to_schema(timestamp, "timestamp")
                message = msg.payload.decode('utf-8')
                message = json.loads(message)
                keys = message.keys()
                key = list(keys)[0]
                device.add_to_schema(message[key], key)


                # Sends data if complete and resets the schema if not. Removes the start incompletion data
                if key == "humidity" and all(v is not None for v in device.get_schema().values()):
                    # sql query
                    try:
                        conn.query(
                            "insert into CaptureData (device_id, pressure, temperature, timestamp, humidity) values (?, ?, ?, ?, ?)",
                            [device.get_name(),
                            device.get_schema()['pressure'], device.get_schema()['temperature'],
                            device.get_schema()['timestamp'], device.get_schema()['humidity']])
                        conn.commit()
                        print(device.get_schema())
                    except Exception as e:
                        print(e)

                    device.reset_schema()

                elif key == "humidity" and any(v is not None for v in device.get_schema().values()):
                    device.reset_schema()


# add components if needed for the thread
def computingFunctionThread():
    print("starting thread")
    while True:
        computing()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.21.1.10", 1883, keepalive=60)


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
