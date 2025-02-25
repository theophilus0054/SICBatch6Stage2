import network
import urequests as request
import dht
from machine import Pin, ADC
import utime as time

# Connect to Wi-Fi
# Set According to your Wi-Fi
ssid = "" 
password = ""

# Set According to your Ubidots Token and label
ubidots_token = ""
device_label = ""

# Set According to your Flask Server
url_flask = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi!")

url_ubidots = "http://industrial.api.ubidots.com/api/v1.6/devices/" + device_label
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": ubidots_token
}

# Initiate DHT11 sensor on GPIO19
sensor = dht.DHT11(Pin(19))

# Initiate PIR sensor on GPIO5
pir_sensor = Pin(5, Pin.IN)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        motion = 1 if pir_sensor.value() == 1 else 0
        
        data = {
            "temperature": temp,
            "humidity": hum,
            "motion": motion,
        }

    # Comment Out Flask Code if you want to use Flask
        # Send data to Flask server
        # Set According to your Flask Server Url
        # response = request.post(url_flask, json=data)
        # print(response.text)
        # response.close()
        
    # Comment Ubidots Code if you don't want to use Ubidots
        # Send data to Ubidots
        response2 = request.post(url_ubidots, json=data, headers=headers)
        print(response2.text)
        response2.close()
        
    except Exception as e:
        print("Error:", e)
    
    time.sleep(7)