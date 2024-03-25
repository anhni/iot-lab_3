import sys
from Adafruit_IO import MQTTClient
import time
from simple_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "Anh_Ni"
AIO_KEY = ""

def connected(client):
    for feed in AIO_FEED_IDs:
        client.subscribe(feed)
        print("Ket noi thanh cong voi " + feed)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    if feed_id == "nutnhan1":
        if payload == "OFF":
            writeData("Button 1 off\n")
        else: writeData("Button 1 on\n")
    if feed_id == "nutnhan2":
        if payload == "OFF":
            writeData("Button 2 off\n")
        else: writeData("Button 2 on\n")


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter_ai =5
ai_result =""
pre_result =""
while True:

    # counter_ai= counter_ai-1
    # if counter_ai<=0:
    #     counter_ai=5
    #     pre_result =ai_result
    #     ai_result = image_detector()
    #     print("AI output: ", ai_result)
    #     if pre_result != ai_result:
    #         client.publish("ai", ai_result)
    readSerial(client)
    time.sleep(1)      