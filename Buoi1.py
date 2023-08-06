# import sys
# from Adafruit_IO import MQTTClient
# import time
# import random
# from Buoi1_2 import *
# # from Buoi2 import *
# from Buoi2_2 import *


# AIO_FEED_ID = ["button1", "button2"]
# AIO_USERNAME = "AlexLam"
# AIO_KEY = "aio_GIAp39XLzD22LPeq2X0MQMibRlru"

# def connected(client):
#     print("Ket noi thanh cong ...")
#     for topic in AIO_FEED_ID:    
#         client.subscribe(topic)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe thanh cong ...")

# def disconnected(client):
#     print("Ngat ket noi ...")
#     sys.exit (1)

# def message(client , feed_id , payload):
#     print("Nhan du lieu: " + payload + " feed:" + feed_id)
#     if feed_id == "button1":
#         if payload == "ON":
#             sendCommand("0")
#         else:
#             sendCommand("1")

#     if feed_id == "button2":
#         if payload == "ON":
#             sendCommand("2")
#         else:
#             sendCommand("3")


# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()
# counter = 10 # Thiết kế State machine để kiểm soát tốt hơn đợt nghỉ giữa các vòng lặp
# counter_ai = 15
# previous_ai = ""
# ai_result = ""

# while True:

#     print("Starting..... counter", counter)
#     counter = counter - 1
#     counter_ai = counter_ai - 1

#     if counter_ai <= 0:
#         counter_ai = 15
#         previous_ai != ai_result
#         #ai_result = get_detection()
#         #client.publish("ai", ai_result)
#         client.publish("sensor1",readTemperature()/100)

#     # if counter <= 0:
#     #     counter = 10
#     #     client.publish("sensor1", random.randint(10, 50))

#     # if counter == 5:
#     #     client.publish("sensor2", random.randint(10, 50))

#     # if counter == 3:
#     #     client.publish("sensor3", random.randint(10, 50))

#     #readSerial(client)
#     time.sleep(0.1)


print("Python IoT")
print("Bài UI.py")

from Adafruit_IO import MQTTClient
from UI import *
import random
import time

AIO_USERNAME = "AlexLam"
AIO_KEY = "aio_GIAp39XLzD22LPeq2X0MQMibRlru"

def connected(client):
    print("Ket noi thanh cong ...")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed: " + feed_id)

def randomValue(type):
    value = 0
    if type == 0:
        value = round(random.randint(20, 80)/30, 2)
    elif type == 1:
        value = round(random.randint(1, 1500), 0)
    else:
        value = round(random.randint(100, 1400) / 100, 2)
    return value

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_background()
counter_sensor = 10
sensor_type = 0

def On():
    global client
    client.publish("button1", "ON")

def Off():
    global client
    client.publish("button1", "OFF")

buttonOn.config(command=On)
buttonOff.config(command=Off)

while True:

    counter_sensor = counter_sensor - 1
    if counter_sensor <= 0:
        counter_sensor = 10
        if sensor_type == 0:
            labelAMONIAValue.config(text=str(randomValue(0)))
            sensor_type = 1
        elif sensor_type == 1:
            labelTDSValue["text"] = str(randomValue(1))
            sensor_type = 2
        else:
            labelPHValue.config(text=str(randomValue(2)))
            sensor_type = 0

    window.update()
    time.sleep(0.1)