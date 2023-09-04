from machine import Pin
import time
import network
import urequests as requests
# import requests
import json
import webrepl

counter = 0
answer = 0

ssid = "geneva"  # input your wifi SSID
pw = "3limmat9"  # input your wifi password

url = "http://iotplotter.com/api/v2/feed/074991343117201320"
headers = {'api-key': '16ca7242763868d85e108be1ca8fbe80a6f07c8208'}
payload = {}  # The variable to send to IoTPlotter
payload["data"] = {}  # A dictionary containing the data to send to IoTPlotter
payload["data"]["GRAPH_NAME"] = []  # Creates a list for sending values

# Main code
webrepl.start(password="1234")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
print(wifi.scan())
wifi.connect(ssid, pw)
print(wifi.scan())
print(wifi.status(), wifi.isconnected())


led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(500)
    counter += 10
    print(counter, wifi.isconnected(), wifi.ifconfig())

    if(wifi.isconnected()):

        # Appends three values for the graph 'GRAPH_NAME':
        payload["data"]["GRAPH_NAME"].append({"value": 50.00 + counter})
        result = requests.post(url, headers=headers, data=json.dumps(payload))
        print(result, counter)